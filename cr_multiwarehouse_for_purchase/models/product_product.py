# -*- coding: utf-8 -*-
# Part of Creyox Technologies

from odoo import fields, models,api

class ProductProductInherit(models.Model):
    _inherit = 'product.product'

    purchase_warehouse_id = fields.Many2one('stock.warehouse',string="Purchase Warehouse" ,store = True , related ='product_tmpl_id.purchase_warehouse_id' )
