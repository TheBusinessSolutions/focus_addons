# Copyright 2024 Moduon Team S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    sale_warn_option = fields.Many2one(
        comodel_name="warn.option",
    )

    @api.onchange("sale_warn_option")
    def _onchange_sale_warn_option(self):
        if self.sale_warn != "no-message" and self.sale_warn_option:
            self.sale_warn_msg = self.sale_warn_option.name
