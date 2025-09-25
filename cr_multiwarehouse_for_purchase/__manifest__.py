# -*- coding: utf-8 -*-
# Part of Creyox Technologies
{
    "name": "Purchase Multi Warehouse Odoo App|| Multiple warehouse on purchase || Multiwarehouse",
    "author": "Creyox Technologies",
    "website": "https://www.creyox.com",
    "support": "support@creyox.com",
    "category": "Purchase",
    "summary": "Multi Warehouse for purchase order line",
    "description": """Multi Warehouse for purchase order line""",
    "license": "LGPL-3",
    "version": "15.0.1",
    "depends": ["base","purchase","stock"],
    "application": True,
   'data': [
        'views/purchase_config_settings_views.xml',
        'views/product_template_views.xml',
        'views/product_product_views.xml',
        'views/purchase_order_views.xml',
    ],
   
    "auto_install": False,
    "installable": True,
    "images": ["static/description/banner.png", ],
    "price": 0,
    "currency": "EUR"
}
