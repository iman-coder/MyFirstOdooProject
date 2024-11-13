from odoo import models, fields

class Employee(models.Model):
    _inherit = ['hr.employee']  # Inherit the employee model

    cost_per_hour = fields.Float(string='Cost per Hour (J/H)')
    project_id = fields.Many2one('project.project', string='Assigned Project')