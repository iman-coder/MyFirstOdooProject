from odoo import models, fields

class Product(models.Model):
    _inherit = 'product.product'# Inherit the existing product model

    quantity_used = fields.Integer(string='Quantity Used')  # New field for quantity used
    usage_date = fields.Date(string='Usage Date')  # New field for usage date
    project_id = fields.Many2one('construction.project', string='Associated Project')  # Field to link to construction.project
