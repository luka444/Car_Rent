from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    rent_car_ids = fields.One2many('car.rent.car', 'car_dealer_id')
    dealer = fields.Boolean(string='Is Dealer')