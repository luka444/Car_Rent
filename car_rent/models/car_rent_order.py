from odoo import fields,models,api


class CarRentOrder(models.Model):
    _name = 'car.rent.order'
    _description = 'Car Rent Order'

    customer_id = fields.Many2one('res.users', default=lambda self: self.env.user, readonly=True)
    car_id = fields.Many2one('car.rent.car')
    rent_order_number = fields.Char(required=True, copy=False, readonly=True,default=lambda self:('New'))

    @api.model
    def create(self, vals):

        if vals.get('rent_order_number', ("New")) == ("New"):
            vals['rent_order_number'] = self.env['ir.sequence'].next_by_code(
                'car.rent.order.sequence',) or ("New")
            
        res = super(CarRentOrder,self).create(vals)
        return res