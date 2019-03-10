# -*- coding: utf-8 -*-
{
    'name': "responsabilidadesExamen",

    'summary': """
        Control y gestion de responsabilidades de los usuarios de odoo""",

    'description': """
        Este modulo permite el control y la gestión de las responsabilidades que tendrás los usuaros en odoo
    """,

    'author': "Angel Gonzalez (examen)",
    'website': "https://github.com/kant003/responsabilidadesExamen.git",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'responsabilidades',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/responsabilidad.xml',
        'views/user.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}