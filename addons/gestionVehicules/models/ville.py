from odoo import api,fields,models

class Ville(models.Model):
    _name = "ville"
    _description = "ville en projet perssonalisé"
    
    name= fields.Char(string="Nom", required=True)
    codePostal=fields.Integer(string="Code postal" , required=True)  
    
    
