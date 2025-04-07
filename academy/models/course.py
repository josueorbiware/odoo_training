from odoo import fields, models


class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course info'

    name = fields.Char('Title', required=True)
    active = fields.Boolean('Active', default=True)
    description = fields.Text('Description')
    level = fields.Selection(string='Level',selection=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')])