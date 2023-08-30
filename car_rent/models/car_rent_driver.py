from datetime import datetime, date, timedelta
from odoo import models, fields, api


class CarRentDriver(models.Model):
    _name = 'car.rent.driver'
    _description = 'Car Rent Driver'
    
    name = fields.Char(required=True)
    date_of_birth = fields.Date()
    age = fields.Integer(readonly=True,compute='_compute_age')
    driver_license_number = fields.Char(required=True)
    driver_license_valid_thru = fields.Date(required=True)  
    car_ids = fields.Many2many('car.rent.car')

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for driver in self:
            if driver.date_of_birth:
                age = today.year - driver.date_of_birth.year
                driver.age = age
            else:
                driver.age = 0

    @api.constrains('age', 'driver_license_valid_thru')
    def _check_age_license_validity(self):
        for driver in self:
            if driver.age < 18:
                raise models.ValidationError("Driver must be at least 18 years old.")
            '''
            if driver.driver_license_valid_thru and driver.driver_license_valid_thru <= date.today():
                raise models.ValidationError("Driver's license must be valid.")
            '''
            min_valid_date = date.today() + timedelta(days=30)
            
            if driver.driver_license_valid_thru and driver.driver_license_valid_thru < min_valid_date:
                raise models.ValidationError("Driver's license must be valid for at least 30 days.")