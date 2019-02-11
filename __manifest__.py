# -*- coding: utf-8 -*-
{
    'name': "website_case_history",

    'summary': """
        Case history
        """,

    'description': """
        Classification of references, case histories or portfolio with pictures, description and tags
    """,

    'author': "Alberto Carollo",
    'website': "https://www.ecobeton.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/case_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
