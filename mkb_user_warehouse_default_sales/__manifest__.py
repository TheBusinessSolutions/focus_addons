# -*- coding: utf-8 -*-
# Copyright 2020-22 Manish Kumar Bohra <manishkumarbohra@outlook.com>
{
    'name': 'Set User Default warehouse',
    'version': '1.0.0',
    'summary': 'This module is mainly use to set default warehouse name in sales order,sales order default warehouse user base,user base warehouse,company set warehouse,default warehouse',
    'description': 'This module is mainly use to set default warehouse name in sales order',
    'category': 'Warehouse',
    'author': 'Manish Bohra',
    'website': 'www.linkedin.com/in/manishkumarbohra',
    'maintainer': 'Manish Bohra',
    'support': 'manishkumarbohra@outlook.com',
    'sequence': '10',
    'license': 'OPL-1',
    'depends': ['base', 'stock', 'sale', 'sale_stock', 'sale_management'],
    'price': '0',
    'currency': 'EUR',
    'data': [
        'views/default_warehouse.xml'
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': True
}
