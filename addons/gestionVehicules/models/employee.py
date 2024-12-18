from odoo import api, models, fields

class Employee(models.Model):
    _description = "Employee in personalized project"
    _name = "employee"
    _inherit = ['hr.employee']
    child_ids = fields.Many2many('hr.employee', 'parent_id', string='Direct subordinates')
    category_ids = fields.Many2many('hr.employee.category', 'employee_category_rel', 'category_id', groups="hr.group_hr_manager", string='Tags')
    x_project_ids = fields.Many2many(
        'construction.project',
        'employee_project',
        'employee_id',
        'project_id',
        string='Projects',
        help='Projects associated with this employee'
    )
    # Custom fields
    cin = fields.Char(string="CIN")
    prenom = fields.Char(string="Prénom")
    typePermis = fields.Selection(
        [('A', 'Type A'), ('B', 'Type B'), ('C', 'Type C')],
        string="Type de Permis"
    )
    etat = fields.Selection(
        [('active', 'Active'), ('inactive', 'Inactive')],
        string="État"
    )
    dateEmbauche = fields.Date(string="Date d'Embauche")
    age = fields.Integer(string="Âge", compute="_compute_age")
    anciennete = fields.Integer(string="Ancienneté", compute="_compute_anciennete")
    x_coutjh = fields.Float(string="Coût Journalier/Horaire")

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
            record.x_coutjh = record.salary / record.working_hours
