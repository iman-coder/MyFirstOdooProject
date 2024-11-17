from odoo import models, fields

class EmployeeProject(models.Model):
    _name = 'employee.project'
    _description = 'Employee Project Association'

    employee_id = fields.Many2one('hr.employee', required=True)
    project_id = fields.Many2one('construction.project', required=True)
    date = fields.Date(string='Date')
