# -*- coding: utf-8 -*-
{
    'name': "Odoo Info",
    'summary': "Odoo Info, List Odoo's Settings and Parameters",
    'application' : True,
    'description': """
    Basic Apps what shows most actual Odoo settings.
    """,
    'author': "Myridia Company",
    'website': "https://github.com/myridia/odoo_info",
    'category': 'Info',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
  "license": "AGPL-3",
  'installable': True,
  'auto_install': True,
}

