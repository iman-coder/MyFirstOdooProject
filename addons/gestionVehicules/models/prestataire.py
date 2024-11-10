from odoo import api, fields, models

class Prestataire(models.Model):
    _description = "Prestataire en projet perssonalisé"
    _name = "prestataire"
   
    ## principaux fields 
    name=fields.Char(string="Nom", required=True)
    prenom=fields.Char(string="Prenom", required=True)
    email=fields.Char(string="email", required=True)
    tel=fields.Char(string="Tel", required=True)
    dateNaiss=fields.Date(string="Date de naissance" ,required=True)
    cin= fields.Char(string="CIN", required=True)
    age = fields.Integer(string="Âge", compute='_compute_age', store=True)
    photo = fields.Binary(string="Photo", attachment=True,required=False)
    # Calcul de l'âge via un computed field 
    @api.depends('dateNaiss')
    def _compute_age(self):
        for record in self:
            if record.dateNaiss:
                today = fields.Date.today()
                delta = today - record.dateNaiss
                record.age = delta.days // 365
            else:
                record.age = 0



