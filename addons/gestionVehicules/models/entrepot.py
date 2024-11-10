from odoo import api,fields,models

class Entrepot(models.Model):
    _name = "entrepot"
    _description = "entrepot en projet perssonalisé"

    num=fields.Integer(string="Numéro",required=True)
    ville=fields.Many2one("ville","ville")
    adresse=fields.Char(string="Adresse",required=True)

    capaciteMax=fields.Integer(string="Capacité maximal",required=True) 
    capaciteActuel=fields.Integer(string="Capacité actuel",required=True) 
    capaciteRest = fields.Integer(string="Capacité restante", compute='_compute_rest', store=True)

# calculated fields automatiqumenet calculé younes_noura
    @api.depends('capaciteMax','capaciteActuel')
    def _compute_rest(self):
        for record in self:
           record['capaciteRest'] = record.capaciteMax-record.capaciteActuel