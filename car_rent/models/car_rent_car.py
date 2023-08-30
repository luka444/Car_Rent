from odoo import fields,models, api
from odoo.exceptions import ValidationError
import re

class CarRentCar(models.Model):
    _name = 'car.rent.car'
    _description = 'Car Rent Car'

    name = fields.Char(strinh="Name", required=True)
    model = fields.Char()
    registration_plate = fields.Char()
    tag_ids = fields.Many2many('car.rent.tag')
    
    colors = fields.Selection(
        string='Car colors',
        selection=[('black','Black'),('white','White'),('red','Red'),('blue', 'Blue'),('green', 'Green'),
        ('silver', 'Silver'),('gray', 'Gray'),('orange', 'Orange'),('yellow', 'Yellow'),('purple', 'Purple'),
        ('pink', 'Pink'),('brown', 'Brown')])
    
    image = fields.Image(string='Image')
    driver_id = fields.Many2one('car.rent.driver')
    car_dealer = fields.Many2one('res.partner')
    _sql_constraints = [
        ('unique_name', 'unique(registration_plate)', 'Plate name must be unique!'),
    ]
    
    @api.constrains('registration_plate')
    def _check_registration_plate(self):
        for car in self:
            if car.registration_plate and not self.georgian_registration_plate(car.registration_plate):
                raise ValidationError("Invalid registration plate format for Georgian EU-style registration.")
    
    def georgian_registration_plate(self,plate):
        georgian_plate = r'^[A-Z]{2}-[0-9]{3}-[A-Z]{2}$'
        
        if re.match(georgian_plate,plate):
            return True
        else:
            return False