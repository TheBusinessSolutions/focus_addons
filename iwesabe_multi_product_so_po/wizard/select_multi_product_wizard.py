# -*- coding: utf-8 -*-
##############################################################################
#
#    Global Creative Concepts Tech Co Ltd.
#    Copyright (C) 2018-TODAY iWesabe (<http://www.iwesabe.com>).
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from datetime import datetime
from odoo import models, fields, api


class SelectMultiProduct(models.TransientModel):
	_name = 'select.multi.product'
	_description = 'add Multiple Product'

	product_ids = fields.Many2many('product.product', string='Products')
	flag_order = fields.Char('Flag Order')

	def select_products(self):
		if self.flag_order == 'so':
			order_id = self.env['sale.order'].browse(self._context.get('active_id', False))
			for product in self.product_ids:
				self.env['sale.order.line'].create({
					'product_id': product.id,
					'product_uom': product.uom_id.id,
					'price_unit': product.lst_price,
					'order_id': order_id.id
				})

		elif self.flag_order == 'po':
			order_id = self.env['purchase.order'].browse(self._context.get('active_id', False))
			for product in self.product_ids:
				self.env['purchase.order.line'].create({
					'product_id': product.id,
					'name': product.name,
					'date_planned': order_id.date_planned or datetime.today(),
					'product_uom': product.uom_id.id,
					'price_unit': product.standard_price,
					'product_qty': 1.0,
					'display_type': False,
					'order_id': order_id.id
				
				})
