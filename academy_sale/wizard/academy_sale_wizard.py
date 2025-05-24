from odoo import models, fields, api
from odoo import Command

class SaleWizard(models.TransientModel):
    _name = 'academy.sale.wizard'
    _description = 'Wizard: Quick create orders for sessions students'

    def _default_session(self):
        return self.env['academy.session'].browse(self._context.get('active_id'))

    session_id = fields.Many2one('academy.session', string='Session',required=True, default=_default_session)
    students_id = fields.Many2many('res.partner', string='Students for sale order')
    session_students_ids = fields.Many2many('res.partner', string='Students in current session', related='session_id.student_ids', help='students in current session')
    session_product_id = fields.Many2one(related="session_id.course_id.product_id.product_variant_id")

    def create_sale_orders(self):
        session_product_id = self.session_product_id
        if session_product_id:
            for student in self.students_id:
                order_id = self.env['sale.order'].create({
                    'partner_id': student.id,
                    'order_line': [Command.create({
                        'product_id': session_product_id.id,
                        'price_unit': self.session_id.course_id.total_price
                    })]
                })

