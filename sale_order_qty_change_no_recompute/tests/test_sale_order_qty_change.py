# Copyright 2021 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo.tests.common import Form, TransactionCase


class TestSaleOrderQtyChange(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Remove this variable in v16 and put instead:
        # from odoo.addons.base.tests.common import DISABLED_MAIL_CONTEXT
        DISABLED_MAIL_CONTEXT = {
            "tracking_disable": True,
            "mail_create_nolog": True,
            "mail_create_nosubscribe": True,
            "mail_notrack": True,
            "no_reset_password": True,
        }
        cls.env = cls.env(context=dict(cls.env.context, **DISABLED_MAIL_CONTEXT))
        cls.product_1 = cls.env["product.product"].create(
            {"name": "Test Product 1", "list_price": 25.00, "taxes_id": False}
        )
        cls.product_2 = cls.env["product.product"].create(
            {"name": "Test Product 2", "list_price": 30.00, "taxes_id": False}
        )
        pricelist = cls.env["product.pricelist"].create({"name": "Test pricelist"})
        sale_form = Form(
            cls.env["sale.order"].with_context(prevent_onchange_quantity=True)
        )
        sale_form.partner_id = cls.env.ref("base.res_partner_12")
        sale_form.pricelist_id = pricelist
        with sale_form.order_line.new() as cls.line_form:
            cls.line_form.product_id = cls.product_1
            cls.line_form.product_uom_qty = 1

    def test_sale_line_misc(self):
        self.assertEqual(self.line_form.price_unit, 25)
        self.line_form.price_unit = 10
        self.line_form.product_uom_qty = 2
        self.assertEqual(self.line_form.price_unit, 10)
        self.line_form.product_id = self.product_2
        self.assertEqual(self.line_form.price_unit, 30)
