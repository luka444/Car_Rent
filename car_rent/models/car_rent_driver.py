from datetime import date, timedelta
from odoo import models, fields, api


class CarRentDriver(models.Model):
    _name = 'car.rent.driver'
    _description = 'Car Rent Driver'
    
    name = fields.Char(required=True)
    date_of_birth = fields.Date()
    age = fields.Integer(compute='_compute_age')
    driver_license_number = fields.Char()
    driver_license_valid_thru = fields.Date(string="Driver's license term")  
    car_ids = fields.One2many('car.rent.car','driver_id')

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for driver in self:
            if driver.date_of_birth:
                age = today.year - driver.year - ((today.month, today.day) < (driver.month, driver.day))
                driver.age = age
            else:
                driver.age = 0

    @api.constrains('age')
    def _check_age_license_validity(self):
        for driver in self:
            if driver.age < 18:
                raise models.ValidationError("Driver must be at least 18 years old.")
     
    @api.constrains('driver_license_valid_thru')
    def _check_driver_license_validity(self):
            '''
            if driver.driver_license_valid_thru and driver.driver_license_valid_thru <= date.today():
                raise models.ValidationError("Driver's license must be valid.")
            '''
            for driver in self:
                min_valid_date = date.today() + timedelta(days=30)
                
                if driver.driver_license_valid_thru and driver.driver_license_valid_thru < min_valid_date:
                    raise models.ValidationError("Driver's license must be valid for at least 30 days.")