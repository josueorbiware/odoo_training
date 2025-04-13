# -*- coding: utf-8 -*-
{
    'name': "Academy Learning Odoo",

    'summary': """
        Academy Learning Odoo""",

    'description': """
        This is a course learning Odoo app by Josué.
    """,

    'author': "Josué Vital Acosta",
    'website': "https://www.yourcompany.com",

    'category': 'Custom Modules/Tech Training',
    'version': '16.0.0.1',
    'license': 'OPL-1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'security/academy_groups.xml',
        'security/academy_security.xml',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/views.xml',
        'views/templates.xml',
        'demo/course_demo.xml',
    ],
    # only loaded in demonstration mode
    'application': True,
}
