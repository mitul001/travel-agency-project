{
    'name': 'travel agency',
    'version': '1.0',
    'summary': 'Manage booking, packages, destinations, and accommodations for a travel agency',
    'description': 'This module provides comprehensive management functionality for a travel agency.',
    'author': 'Mitul Patel (miup)',
    'depends': ['base'],
    'data':[
        'security/ir.model.access.csv',

        'views/travelagency_customer_view.xml',
        'views/travelagency_preference_tag_view.xml',
        'views/travelagency_menus.xml'
    ],
    'installable': True,
    'application': True,
    'license':'LGPL-3'
}

