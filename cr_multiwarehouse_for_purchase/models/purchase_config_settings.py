# -*- coding: utf-8 -*-
# Part of Creyox Technologies

from odoo import api, fields, models, _

class ResCompany(models.Model):
	_inherit = 'res.company'

	cr_allow_purchase_warehouse = fields.Boolean(string="Allow Warehouse in Purchase Order Line", default=False)


class ResConfigSettings(models.TransientModel): 
	_inherit = 'res.config.settings'

	cr_allow_purchase_warehouse = fields.Boolean(string="Allow Warehouse in Purchase Order Line", related='company_id.cr_allow_purchase_warehouse',readonly=False,)






