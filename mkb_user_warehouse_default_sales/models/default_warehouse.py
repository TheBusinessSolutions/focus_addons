# -*- coding: utf-8 -*-
# Copyright 2020-22 Manish Kumar Bohra <manishkumarbohra@outlook.com>

from odoo import api, fields, models


class ResUsersInherit(models.Model):
    _inherit = 'res.users'

    default_wr = fields.Many2one(comodel_name="stock.warehouse", string="Warehouse")
    is_wr_so = fields.Boolean(string="Is Default Use in Sales")


class MKBSalesOrderInherit(models.Model):
    _inherit = 'sale.order'

    @api.onchange('company_id')
    def _onchange_company_id(self):
        if self.company_id:
            if self.user_id.is_wr_so and self.user_id.default_wr:
                self.warehouse_id = self.user_id.default_wr.id
            else:
                warehouse_id = self.env['ir.default'].get_model_defaults('sale.order').get('warehouse_id')
                self.warehouse_id = warehouse_id or self.user_id.with_company(
                    self.company_id.id)._get_default_warehouse_id().id

    @api.onchange('user_id')
    def onchange_user_id(self):
        super().onchange_user_id()
        if self.state in ['draft', 'sent']:
            if self.user_id.is_wr_so and self.user_id.default_wr:
                self.warehouse_id = self.user_id.default_wr.id
            else:
                self.warehouse_id = self.user_id.with_company(self.company_id.id)._get_default_warehouse_id().id
