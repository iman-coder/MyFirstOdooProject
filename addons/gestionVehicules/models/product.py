from odoo import models, fields

class Product(models.Model):
    _inherit = ['product.product']  # Inherit the product model

    quantity_used = fields.Integer(string='Quantity Used')
    usage_date = fields.Date(string='Usage Date')
    project_id = fields.Many2one('project.project', string='Associated Project')