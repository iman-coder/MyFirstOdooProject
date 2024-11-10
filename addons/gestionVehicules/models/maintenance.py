from odoo import models, fields

class Maintenance(models.Model):
    _name = "maintenance"
    _inherit = "maintenance.request"

    prestataire= fields.Many2one('prestataire', string='Prestataire')
    vehicule= fields.Many2one('vehicule', string='Vehicule')
    # Related fields pour Prestataire infos
    cinPrestataire = fields.Char(related='prestataire.cin', string="CIN Prestataire")
    nomPrestataire = fields.Char(related='prestataire.name', string="Nom ")
    prenomPrestataire = fields.Char(related='prestataire.prenom', string="Prénom ")
    telPrestataire = fields.Char(related='prestataire.tel', string="Téléphone ")
    photoPrestataire = fields.Binary(related='prestataire.photo', string="Photo ")
    emailPrestataire = fields.Char(related='prestataire.email', string="Email" )
    # Related fields pour Vehicule infos
    immatricule = fields.Char(related='vehicule.immatricule', string="Immatricule")
    photo = fields.Binary(related='vehicule.photo', string="Photo")
