from odoo import api,models, fields

class Chauffeur(models.Model):
    _description = "chauffeur en projet perssonalisé"
    _name = "chauffeur"
    _inherit = ['hr.employee']
    child_ids = fields.Many2many('hr.employee', 'parent_id', string='Direct subordinates')
    category_ids = fields.Many2many( 'hr.employee.category', 'chauffeur_category_rel', 'emp_id', 'category_id', groups="hr.group_hr_manager", string='Tags')
    
    #nos fields perssonalisés
    cin= fields.Char(string="CIN", required=True)
    prenom= fields.Char(string="Prenom", required=True)
    age = fields.Integer(string="Âge", compute='_compute_age', store=True)
    photo = fields.Binary(string="Photo", attachment=True)
    etat= fields.Selection([('Disponible','Disponible'),('En mission','En mission'),('En congé','En congé')])
    typePermis = fields.Selection([('A', 'A'), ('A1', 'A1'),('B','B'),('C', 'C'),('C1','C1')],
                                   string="Type de Permis")

    dateEmbauche= fields.Date(string="date d embauche" ,required=False)
    anciennete = fields.Integer(string="Ancienneté", compute='_compute_anciennete', store=True)

    # calculated fields automatiqumenet calculé younes_noura
    @api.depends('dateEmbauche')
    def _compute_anciennete(self):
        for record in self:
            if record.dateEmbauche:
                today = fields.Date.today()
                delta = today - record.dateEmbauche
                record.anciennete = delta.days // 365
            else:
                record.anciennete = 0
    # Calcul de l'âge via un computed field 

    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            if record.birthday:
                today = fields.Date.today()
                delta = today - record.birthday
                record.age = delta.days // 365
            else:
                record.age = 0


