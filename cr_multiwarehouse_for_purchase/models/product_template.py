# -*- coding: utf-8 -*-
# Part of Creyox Technologies

from odoo import fields, models,api

class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    purchase_warehouse_id = fields.Many2one('stock.warehouse',string="Purchase Warehouse")
