# -*- coding: utf-8 -*-

{
    'name': 'Warehouse Access Control',
    'description': """Ware House Location Restriction""",
    'summary': "'Warehouse Restriction for all users  convenience  and inventory location mangaement'",
    'version': '15.0.0.0.0',
    'catagory': 'Stock',
   "author": "One Stop Odoo",
    "website": "https://onestopodoo.com/",
    "maintainer": "One Stop Odoo",
    'license': 'LGPL-3',
    'depends': ['base', 'stock', 'sale'],
    'data': [
        'security/security_groups.xml',
        'views/ware_house_user_ext.xml'
    ],
    'images': [
        'static/description/banner.gif',
        'static/description/icon.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
