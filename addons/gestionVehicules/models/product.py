from odoo import models, fields

class Product(models.Model):
    _inherit = 'product.product'

    quantity_used = fields.Integer(string='Quantity Used')  
    usage_date = fields.Date(string='Usage Date')  
    x_project_id = fields.Many2one('construction.project', string='Associated Project')  
