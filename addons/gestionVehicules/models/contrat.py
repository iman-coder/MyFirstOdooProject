from odoo import models, fields, api

class Contrat(models.Model):
    _name = "contrat"
    _inherit = 'hr.contract'
    ## nos fields perssonalisés
    type = fields.Selection([
        ('cdi', 'CDI - Contrat à durée indéterminée'),
        ('cdd', 'CDD - Contrat à durée déterminée'),
        ('freelance', 'Freelance')
    ], string='Type de contrat', default='cdi')
    ## nombre de jours retants avant la fin du contrat 
    nbrJoursRest=fields.Integer(string="Nombre de jours restants ",compute="_compute_rest",store=False)
    @api.depends('date_start','date_end')
    def _compute_rest(self):
        for record in self:
           if record.date_end and record.date_start:
              record['nbrJoursRest'] = (record.date_end-record.date_start).days
           else:
              record['nbrJoursRest'] = 0

    prime=fields.Float(string="Prime" ,required=False)
    prestataire=fields.Many2one("prestataire","prestataire")
    #related fields to prestataire
    cinPrestataire = fields.Char(related='prestataire.cin', string="CIN Prestataire")
    nomPrestataire = fields.Char(related='prestataire.name', string="Nom ")
    prenomPrestataire = fields.Char(related='prestataire.prenom', string="Prénom ")
    telPrestataire = fields.Char(related='prestataire.tel', string="Téléphone ")
    photoPrestataire = fields.Binary(related='prestataire.photo', string="Photo ")
    emailPrestataire = fields.Char(related='prestataire.email', string="Email" )
