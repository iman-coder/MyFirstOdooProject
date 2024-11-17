from odoo import api, models, fields

class Employee(models.Model):
    _description = "Employee in personalized project"
    _name = "employee"
    _inherit = ['hr.employee']
    child_ids = fields.Many2many('hr.employee', 'parent_id', string='Direct subordinates')
    category_ids = fields.Many2many('hr.employee.category', 'employee_category_rel', 'category_id', groups="hr.group_hr_manager", string='Tags')

    # Custom fields
    cin = fields.Char(string="CIN", required=True)
    prenom = fields.Char(string="Prenom", required=True)
    age = fields.Integer(string="Âge", compute='_compute_age', store=True)
    photo = fields.Binary(string="Photo", attachment=True)
    etat = fields.Selection([('Disponible', 'Disponible'), ('En mission', 'En mission'), ('En congé', 'En congé')])
    typePermis = fields.Selection([('A', 'A'), ('A1', 'A1'), ('B', 'B'), ('C', 'C'), ('C1', 'C1')],
                                  string="Type de Permis")

    dateEmbauche = fields.Date(string="Date d'embauche", required=False)
    anciennete = fields.Integer(string="Ancienneté", compute='_compute_anciennete', store=True)

    # New field for Cout J/H (Cost per Man-Day)
    cout_j_h = fields.Float(string="Cout J/H", help="Cost per Man-Day")

    # Computed field for ancienneté (years of service)
    @api.depends('dateEmbauche')
    def _compute_anciennete(self):
        for record in self:
            if record.dateEmbauche:
                today = fields.Date.today()
                delta = today - record.dateEmbauche
                record.anciennete = delta.days // 365
            else:
                record.anciennete = 0

    # Computed field for age
    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            if record.birthday:
                today = fields.Date.today()
                delta = today - record.birthday
                record.age = delta.days // 365
            else:
                record.age = 0
    
    @api.depends('salary', 'working_hours')
    def _compute_cout_j_h(self):
        for record in self:
        # Logic to calculate Cout J/H, e.g.:
            record.cout_j_h = record.salary / record.working_hours
