from odoo import models, fields

class Project(models.Model):
    _name = 'construction.project'
    _description = 'Construction Project'

    name = fields.Char(string="Project Name", required=True)
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    mission_ids = fields.One2many('construction.mission', 'project_id', string="Missions")
    employee_ids = fields.Many2many('hr.employee', string="Employees")
    product_ids = fields.Many2many('product.product', string="Products")
    vehicle_ids = fields.Many2many('fleet.vehicle', string="Vehicles")
    total_cost = fields.Float(string="Total Cost", compute='_compute_total_cost')
    active_id = fields.Many2one('some.model', string='Active')
    some_value = fields.Char("Some Value")
    exploitation_ids = fields.One2many('construction.exploitation', 'project_id', string='Exploitation Records')

    employee_ids = fields.Many2many(
        'hr.employee',
        'employee_project',
        'project_id',
        'employee_id',
        string='Employees',
        help='Employees associated with this project'
    )

    def _compute_total_cost(self):
       for record in self:
            employee_cost = sum(e.hourly_rate for e in record.employee_ids)
            product_cost = sum(p.standard_price for p in record.product_ids)
            vehicle_cost = sum(v.daily_cost for v in record.vehicle_ids)
            record.total_cost = employee_cost + product_cost + vehicle_cost

'''
class ConstructionProject(models.Model):
    _inherit = 'project.project'

    product_ids = fields.One2many('construction.product', 'project_id', string="Products")
    employee_ids = fields.One2many('hr.employee', 'project_id', string="Employees")
    vehicle_ids = fields.One2many('fleet.vehicle', 'project_id', string="Vehicles")
    total_cost = fields.Float(compute='_compute_total_cost', string="Total Cost")

    def _compute_total_cost(self):
        for project in self:
            product_cost = sum(product.daily_cost for product in project.product_ids)
            employee_cost = sum(emp.hourly_rate * 8 for emp in project.employee_ids)  # Assuming 8 hours/day
            vehicle_cost = sum(vehicle.daily_cost for vehicle in project.vehicle_ids)
            project.total_cost = product_cost + employee_cost + vehicle_cost
'''
