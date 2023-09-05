from odoo import fields, models


class CarRentTag(models.Model):
    _name = 'car.rent.tag'
    _description = 'Car rent Tag'

    name = fields.Char(string="Tags", required=True)
    color = fields.Integer(string="Tag Color")
    
    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Tag name must be unique!'),
    ]