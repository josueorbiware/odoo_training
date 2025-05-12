from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course info'

    name = fields.Char('Title', required=True)
    active = fields.Boolean('Active', default=True)
    description = fields.Text('Description')
    level = fields.Selection(string='Level',selection=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')])
    session_ids = fields.One2many('academy.session', string='Session', inverse_name='course_id')
    currency_id = fields.Many2one('res.currency','Currency', default=lambda self:self.env.company.currency_id.id)
    base_price = fields.Monetary('Base Price', currency_field='currency_id')
    additional_fee = fields.Monetary('Additional Fee', currency_field='currency_id')
    total_price = fields.Monetary('Total Price', currency_field='currency_id', compute='_compute_total_price', store=True)

    @api.depends('base_price', 'additional_fee')
    def _compute_total_price(self):
        for record in self:
            if record.base_price < 0:
                raise ValidationError('Base price cannot be negative')
            record.total_price = record.base_price + record.additional_fee