from odoo import fields,models

class CarMark(models.Model):
    _name = 'car.mark'
    _description = 'Car Mark'

    name = fields.Char()