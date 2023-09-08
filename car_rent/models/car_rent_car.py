import re
from odoo import fields,models, api
from odoo.exceptions import ValidationError


class CarRentCar(models.Model):
    _name = 'car.rent.car'
    _description = 'Car Rent Car'

    name = fields.Char(required=True)
    model = fields.Char()
    registration_plate = fields.Char()
    category_id = fields.Many2one('car.category')
    car_mark_id = fields.Many2one('car.mark')
    
    color = fields.Selection(
        string='Car color',
        selection=[('black','Black'),
                   ('white','White'),
                   ('red','Red'),
                   ('blue', 'Blue'),
                   ('green', 'Green'),
                   ('silver', 'Silver'),
                   ('gray', 'Gray'),
                   ('orange', 'Orange'),
                   ('yellow', 'Yellow'),
                   ('purple', 'Purple'),
                   ('pink', 'Pink'),
                   ('brown', 'Brown')])
    
    car_img = fields.Image(string='Image', max_width=590, max_height=590)
    driver_id = fields.Many2one('car.rent.driver')
    car_dealer_id = fields.Many2one('res.partner')
    
    _sql_constraints = [
        ('unique_registration_plate', 'unique(registration_plate)', 'Plate name must be unique!'),
    ]
    
    @api.constrains('registration_plate')
    def _check_registration_plate(self):
        for car in self:
            if car.registration_plate and not self.georgian_registration_plate(car.registration_plate):
                raise ValidationError("Invalid registration plate format for Georgian EU-style registration. Example: EE-999-EE")
    
    def georgian_registration_plate(self,plate):
        georgian_plate = r'^[A-Z]{2}-[0-9]{3}-[A-Z]{2}$'
        
        return  bool(re.match(georgian_plate,plate))