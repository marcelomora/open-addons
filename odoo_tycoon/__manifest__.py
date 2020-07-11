# -*- coding: utf-8 -*-
{
    'name': "Odoo Tycoon",

    'summary': """
        Odoo Tycoon game
    """,

    'description': """
        Odoo first game just for fun
    """,

    'author': "Accioma",
    'website': "http://www.accioma.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Games',
    'version': '12.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock', 'crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/tycoon_game_view.xml',
        'views/game_move_views.xml',
        #  'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #  'demo': [
    #      'demo/demo.xml',
    #  ],
}
