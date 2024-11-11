from odoo import api, fields, models

class Vehicle(models.Model):
    _inherit = 'fleet.vehicle'  # Inherit the vehicle model
    
    immatricule = fields.Char('Immatricule ')
    daily_cost = fields.Float(string='Daily Cost')
    usage_date = fields.Date(string='Usage Date')
    project_id = fields.Many2one('project.project', string='Assigned Project')
'''
class vehicule(models.Model):
    _name = "vehicule"
    _inherit = ['fleet.vehicle']
    tag_ids = fields.Many2many('fleet.vehicle.tag', 'vehicule_vehicle_tag_rel', 'vehicle_tag_id', 'tag_id','Tags', copy=False)
    
    # nos fields perssonalisé
    immatricule = fields.Char('Immatricule ')
    type= fields.Selection([('Voiture','Voiture'),('Moto','Moto'),('Camion','Camion'),('Tracteur','Tracteur'),('Velo','Velo')])
    etat= fields.Selection([('Disponible','Disponible'),('En mission','En mission'),('En reparation','En reparation'),('En panne','En panne')])
    photo = fields.Binary(string="Photo", attachment=True)
'''
    