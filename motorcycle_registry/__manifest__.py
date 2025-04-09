# -*- coding: utf-8 -*-
{
    'name': "Motorcycle Registry",

    'summary': """
        Manage Registration of Motorcycles""",

    'description': """
        Motorcycle Registry
        ====================
        This Module is used to keep track of the Motorcycle Registration and Ownership
        of each motorcycled of the brand.
    """,

    'author': "Josué Vital",
    'website': "https://www.yourcompany.com",

    'category': 'Kawiil/Custom Module',
    'version': '16.0.0.1',
    'license': 'OPL-1',

    'depends': ['base'],

    'data': [
        'security/motorcycle_groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
