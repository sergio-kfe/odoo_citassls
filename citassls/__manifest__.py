# -*- coding: utf-8 -*-
{
    'name': "citassls",

    'summary': """
        Modulo para la gestion de citas""",

    'description': """
        Modulo para gestionar citas pudiendo gestionarlas por fecha
    """,

    'author': "Sergio López",
    'website': "http://www.sistelin.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
	'views/menu.xml',
    ],
    'images': [
        'static/description/calendar.png',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
