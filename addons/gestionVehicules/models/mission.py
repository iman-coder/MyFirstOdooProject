from odoo import models, fields

class Mission(models.Model):
    _name = 'construction.mission'
    _description = 'Mission between Project and Vehicle'

    project_id = fields.Many2one('construction.project', string="Project", required=True)
    vehicle_id = fields.Many2one('fleet.vehicle', string="Vehicle", required=True)
    date = fields.Date(string="Mission Date", required=True)
    cost = fields.Float(string="Cost", required=True)

    # Optionally, you can compute or add other methods
