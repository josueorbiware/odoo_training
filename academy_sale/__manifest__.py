# -*- coding: utf-8 -*-
{
    'name': "academy_sale",

    'author': "Josué Vital",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Custom Modules/Tech Training',
    'version': '16.0.0.1',
    'license': 'OPL-1',

    # any module necessary for this one to work correctly
    'depends': ['base','academy','sale_management'],

    # always loaded
    'data': [
        'data/academy_sale_data.xml',
        'views/academy_sale_menuitems.xml',
        'views/course_views.xml',
        'views/product_template_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'auto_install': True,
}
