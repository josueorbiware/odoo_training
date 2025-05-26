from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools import date_utils


class Session(models.Model):
    _name = 'academy.session'
    _description = 'Session Info'

    name = fields.Char(string="Title", related='course_id.name', readonly=False)
    session_number = fields.Char(string="Session Number", default="S0000", copy=False, required=True, readonly=True)
    date_start = fields.Datetime(string="Start Date")
    date_end = fields.Datetime(string='End Date')
    course_id = fields.Many2one('academy.course', string="Course", required=True, ondelete='cascade')
    instructor_id = fields.Many2one('res.users', string="Instructor", required=True)
    student_ids = fields.Many2many('res.partner', string="Students")
    description = fields.Text(related='course_id.description', string="Description")
    duration = fields.Integer(string="Duration", compute='_compute_session_duration', inverse='_inverse_session_duration', readonly=False)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('session_number', ('S0000')) == ('S0000'):
                vals['session_number'] = self.env['ir.sequence'].next_by_code('session.number')
        return super().create(vals_list)

    @api.constrains('date_end', 'date_start')
    def _check_end_date(self):
        for session in self:
            if session.date_end <= session.date_start:
                raise ValidationError("End Date should be greater than Start Date")

    @api.depends('date_end', 'date_start')
    def _compute_session_duration(self):
        for session in self:
            if session.date_start and session.date_end:
                session.duration = (session.date_end - session.date_start).days + 1

    def _inverse_session_duration(self):
        for session in self:
            if session.date_start and session.duration:
                session.date_end = date_utils.add(session.date_start, days=session.duration-1)

