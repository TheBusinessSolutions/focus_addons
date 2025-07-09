from odoo import fields, api, models, _
from odoo.exceptions import UserError


class ConfirmCancelSalePurchaseOrders(models.TransientModel):
    _name = 'sale.purchase.action.wizard'
    _description = 'Confirm/Cancel Multiple Orders'

    sale_order_ids = fields.Many2many('sale.order', string='Sale Order')
    purchase_order_ids = fields.Many2many('purchase.order', string='Purchase Order')
    state = fields.Selection([('confirm', 'Confirm'), ('cancel', 'Cancel')], required=True)
    is_purchase_order = fields.Boolean(default=False)

    @api.model
    def default_get(self, field_lst):
        res = super(ConfirmCancelSalePurchaseOrders, self).default_get(field_lst)
        active_model = self._context.get('active_model')
        order_ids = self._context.get('active_ids')
        if active_model == 'purchase.order':
            res['is_purchase_order'] = True
        res['sale_order_ids'] = order_ids if active_model == 'sale.order' else False
        res['purchase_order_ids'] = order_ids if active_model == 'purchase.order' else False
        return res

    def action_confirm_cancel_orders(self):
        if self._context.get('active_model') == 'sale.order':
            if self.state == 'confirm':
                if any(order.state not in ['draft', 'sent'] for order in self.sale_order_ids):
                    raise UserError(_('Please select Sale orders which is "Quotation" and "Quotation Sent" stage.'))
                for sale in self.sale_order_ids:
                    sale.action_confirm()
            else:
                if any(order.state == 'cancel' for order in self.sale_order_ids):
                    raise UserError(_('Please select Sale orders which are not cancel.'))
                for sale in self.sale_order_ids:
                    print("\n\n\n\n\n::::::::::::::;;",sale)
                    sale._action_cancel()
        else:
            if self.state == 'confirm':
                if any(order.state not in ['draft', 'sent', 'to approve'] for order in self.purchase_order_ids):
                    raise UserError(_('Please select purchase orders which is "Quotation" and "Quotation Sent" stage.'))
                for purchase in self.purchase_order_ids:
                    purchase.button_confirm()
            else:
                if any(order.state == 'cancel' for order in self.purchase_order_ids):
                    raise UserError(_('Please select purchase orders which are not cancel.'))
                for purchase in self.purchase_order_ids:
                    purchase.button_cancel()

