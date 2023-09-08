from odoo import fields,models


class CarRentOrder(models.Model):
    _name = 'car.rent.order'
    _description = 'Car Rent Order'

    rent_order_number = fields.Char(default=lambda self: self.env['ir.sequence'].next_by_code('car.rent.order.sequence'))
    customer_id = fields.Many2one('res.users', default=lambda self: self.env.user, readonly=True)
    car_id = fields.Many2one('car.rent.car')