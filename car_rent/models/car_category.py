from odoo import fields, models


class CarRentTag(models.Model):
    _name = 'car.category'
    _description = 'Car Category'

    name = fields.Char(string="Category", required=True)
    
    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Category name must be unique!'),
    ]