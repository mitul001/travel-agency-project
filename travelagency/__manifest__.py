{
    'name': 'travel agency',
    'version': '1.0',
    'summary': 'Manage booking, packages, destinations, and accommodations for a travel agency',
    'description': 'This module provides comprehensive management functionality for a travel agency.',
    'author': 'Mitul Patel (miup)',
    'depends': ['base','mail'],
    'data':[
        'security/ir.model.access.csv',

        'views/travelagency_accommodation_view.xml',
        'views/travelagency_packages_view.xml',
        'views/travelagency_accommodation_type_view.xml',
        'views/travelagency_package_type_view.xml',
        'views/travelagency_customer_view.xml',
        'views/travelagency_menus.xml'
    ],
    'demo':[
        'demo/demo_package_type.xml',
        'demo/demo_accommodation_type.xml',
        'demo/demo_package.xml',
        'demo/demo_accommodation.xml',
        'demo/demo_customer.xml',
    ],
    'installable': True,
    'application': True,
    'license':'LGPL-3'
}
