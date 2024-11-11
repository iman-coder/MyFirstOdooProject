from odoo import models, fields

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