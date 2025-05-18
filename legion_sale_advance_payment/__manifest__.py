# -*- coding: utf-8 -*-

{
    "name": "Advance Payment Sale & Invoice",
    'version': '15.0.0.0',
    "author": "Bytelegion",
    "website": "http://www.bytelegions.com",
    'company': 'Bytelegion',
    'depends': ['base', 'sale'],
    'license': 'LGPL-3',
    "category": 'Advance Payment for sale order and invoice',

    "summary": 'Sale Order Advance Payment',
    "description": """Advance Payment on sale order and invoice""",

    'data': [
        'views/inherit_sale_order_view.xml',
        'report/sales_invoice_report.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.gif'], 
    
}

