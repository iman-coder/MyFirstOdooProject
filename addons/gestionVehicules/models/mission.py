from odoo import api,fields,models
from odoo.tools import plaintext2html
#notre classe d'association !
class Mission(models.Model):
    _name = "mission"
    _description = "mission en projet perssonalisé"

    dateDepart = fields.Datetime(string="Date de départ",required=True)
    dateArrive = fields.Datetime(string="Date de d arrivée",required=True)
    ## on va calculer le cout selon la distance parcouru
    distance=fields.Integer(string="Distance à parcourir (KM)" ,required=True)
    cout = fields.Float(string="Cout en MAD", compute='_compute_cout', store=True)
    etat = fields.Selection([('Accomplie','Accomplie'),('En cours','En cours'),('Annulée','Annulée')])
    
    villeDepart=fields.Many2one("ville","ville de depart")
    villeArrive=fields.Many2one("ville","ville d'arrivé")

   ## on va mettre a jour l'etat de la vehicule selon letat de la mission
    vehicule=fields.Many2one("vehicule","vehicule")
    etatVehicule=fields.Selection(related="vehicule.etat" ,string="Etat vehicule")
    
    chauffeur=fields.Many2one("chauffeur","Nom chauffeur")
    chauffeurNom=fields.Char(related="chauffeur.name",string="Nom",readonly=True)
    chauffeurPrenom=fields.Char(related="chauffeur.prenom",string="Prenom",readonly=True)
    chauffeurEmail=fields.Char(related="chauffeur.work_email",string="Email",readonly=True)
    chauffeurPhoto=fields.Binary(related="chauffeur.photo",string="Photo chauffeur",readonly=True)
    etatChauffeur=fields.Selection(related="chauffeur.etat" ,string="Etat chauffeur")

    def send_email(self, subject, body):
        # Assurez-vous que la mission a un chauffeur avec une adresse e-mail
        if self.chauffeur and self.chauffeurEmail:
            # Créez et envoyez l'e-mail
            self.env['mail.mail'].sudo().create({
                'subject': subject,
                'body_html': plaintext2html(body),
                'email_from': 'younes.khouna00@gmail.com',
                'email_to': self.chauffeurEmail,
            }).send()

    @api.depends('distance')
    def _compute_cout(self):
        for record in self:
            if record.distance:
                record.cout = record.distance * 5.7
            else:
                record.cout = 0

    @api.onchange('etat')
    def on_change_state(self):
        if self.etat == "En cours":
            self.etatVehicule = 'En mission'
            self.etatChauffeur= 'En mission'
        else:
            self.etatVehicule = 'Disponible'
            self.etatChauffeur = 'Disponible'

        
                

    @api.model
    def create(self, values):
        mission = super(Mission, self).create(values)
      
        # Mettre à jour l'état du véhicule lors de la création de la mission
        if mission.vehicule and mission.etat == 'En cours':
            mission.vehicule.write({'etat': 'En mission'})
             

        # Mettre à jour l'état du chauffeur lors de la création de la mission
        if mission.chauffeur and mission.etat == 'En cours':
            mission.chauffeur.write({'etat': 'En mission'})
            self.send_email('Nouvelle mission affectée', f'Bonjour {self.chauffeurNom} {self.chauffeurPrenom} \n Votre entreprise INSEA vous affecté une nouvelle mission pour le {self.dateDepart} , Soyez pret et bon courage ! \n KHOUNA younes,\n Responsable des Missions,\n 0689794667  ')

        return mission

    def write(self, values):
        mission = super(Mission, self).write(values)

        # Mettre à jour l'état du véhicule en fonction de la valeur de etat
        if self.vehicule and 'etat' in values:
            if values['etat'] == 'En cours':
                self.vehicule.write({'etat': 'En mission'})
                self.send_email('Nouvelle mission affectée', f'Bonjour {self.chauffeurNom} {self.chauffeurPrenom} \n Votre entreprise INSEA vous affecté une nouvelle mission pour le {self.dateDepart} , Soyez pret et bon courage ! \n KHOUNA younes, \n Responsable des Missions,\n 0689794667  ')
            elif values['etat'] == 'Accomplie':
                self.vehicule.write({'etat': 'Disponible'})
            else :
                self.vehicule.write({'etat': 'Disponible'})

        # Mettre à jour l'état du chauffeur en fonction de la valeur de etat
        if self.chauffeur and 'etat' in values:
            if values['etat'] == 'En cours':
                self.chauffeur.write({'etat': 'En mission'})
                
            elif values['etat'] == 'Accomplie':
                self.chauffeur.write({'etat': 'Disponible'})
            else :
                self.chauffeur.write({'etat': 'Disponible'})
        return mission



    