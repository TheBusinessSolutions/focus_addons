
{
    'name': 'Confirm/Cancel Multiple Sale and Purchase Orders',
    'version': '15.0',
    'category': 'Custom',
    'summary': 'This module streamlines order management in Odoo by enabling users to efficiently confirm or cancel multiple sales and purchase orders simultaneously, improving workflow efficiency and saving time .Confirm Multiple Sale order. Cancel Multiple Sale Order. Confirm Multiple Purchase Order. Cancel Multiple Purchase Order. Mass confirm sale order. Mass confirm purchase order. Mass cancel sale order. Mass cancel purchase order.',
    'description': """
            This module streamlines order management in Odoo by enabling users to efficiently confirm or cancel multiple sales and purchase orders simultaneously, improving workflow efficiency and saving time.
            """,

    'author': 'Mitul Bharola',
    "license": "",
    'depends': ['base','sale_management', 'purchase'],
    'data': [
        "security/ir.model.access.csv",
        "wizard/sale_purchase_wizard.xml",
    ],
    'images': [
        'static/description/banner.png',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
