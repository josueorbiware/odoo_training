from odoo import fields, models


class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle registry'
    _rec_name = 'registry_number'

    certificate_title = fields.Binary(string='Título de propiedad')
    current_mileage = fields.Float(string='Millage Actual')
    first_name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellido', required=True)
    license_plate = fields.Char(string='Matrícula')
    registry_date = fields.Date(string='Fecha de registro')
    registry_number = fields.Char(string='Número de registro')
    vin = fields.Char(string='VIN', required=True)