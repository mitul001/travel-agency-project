{
    'name': 'travel agency',
    'version': '1.0',
    'summary': 'Manage booking, packages, destinations, and accommodations for a travel agency',
    'description': 'This module provides comprehensive management functionality for a travel agency.',
    'author': 'Mitul Patel (miup)',
    'depends': ['mail','account','sale_management','website_sale'],
    'data':[
        'security/ir.model.access.csv',
        
        'data/ir_sequence_data.xml',
        'views/product_template_views.xml',
        'views/ta_customer_view.xml',
        'views/ta_menus.xml'
    ],
    'demo':[
        # 'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'license':'LGPL-3'
}
