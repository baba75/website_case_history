# -*- coding: utf-8 -*-
{
    'name': "Website Case History",

    'summary': """
        Case history
        """,

    'description': """
        Classification of references, case histories or portfolio with pictures, description and tags

        The module let you create multiple galleries, with 2 different layout (gallery and reference)
    """,

    'author': "Alberto Carollo",
    'website': "https://www.ecobeton.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/website_data.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/case_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
