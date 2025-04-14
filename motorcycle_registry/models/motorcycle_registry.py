from odoo import fields, models, api
from odoo.exceptions import ValidationError
import re


class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle registry'
    _rec_name = 'registry_number'

    certificate_title = fields.Binary(string='Titulo de propiedad')
    current_mileage = fields.Float(string='Millage Actual')
    first_name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellido', required=True)
    license_plate = fields.Char(string='Matrícula')
    registry_date = fields.Date(string='Fecha de registro')
    registry_number = fields.Char(string='Número de registro')
    vin = fields.Char(string='VIN', required=True)
    sequence_motorcycle = fields.Char(string="Registro de Motocicleta", default="MRN0000", copy=False, required=True, readonly=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('sequence_motorcycle', ('MRN0000')) == ('MRN0000'):
                vals['sequence_motorcycle'] = self.env['ir.sequence'].next_by_code('motorcycle.number')
        return super().create(vals_list)

    @api.constrains('vin')
    def _check_vin_format(self):
        pattern = r'^[A-Z]{2}[A-Z]{2}\d{2}[A-Z0-9]{2}\d{5}$'
        for record in self:
            if record.vin and not re.match(pattern, record.vin):
                raise ValidationError(
                    "El VIN debe seguir el formato: "
                    "2 letras (Marca) + 2 letras (Modelo) + 2 dígitos (Año) + "
                    "2 letras o dígitos (Batería) + 5 dígitos (Número de serie).\n"
                    "Ejemplos válidos: KAIN220M00023, KAUK21XL84732"
                )

    @api.constrains('license_plate')
    def _check_license_plate_format(self):
        pattern = r'^[A-Z]{1,4}\d{1,3}[A-Z]{0,2}$'
        for record in self:
            if record.license_plate and not re.match(pattern, record.license_plate):
                raise ValidationError(
                    "La matrícula debe seguir el formato:\n"
                    "- 1 a 4 letras mayúsculas\n"
                    "- 1 a 3 dígitos\n"
                    "- Opcional: 0 a 2 letras mayúsculas al final\n\n"
                    "Ejemplos válidos: KLV453, ABC1, XY123AB"
                )

    @api.constrains('vin')
    def _check_unique_vin(self):
        for record in self:
            if record.vin:
                existing = self.search([
                    ('vin', '=', record.vin),
                    ('id', '!=', record.id)
                ], limit=1)
                if existing:
                    raise ValidationError("Ya existe un registro con este VIN. Debe ser único.")