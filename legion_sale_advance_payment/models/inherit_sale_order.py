# -*- coding: utf-8 -*-

import time
from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    journal_id = fields.Many2one(
        'account.journal', 'Payment Journal', domain=[('type', 'in', ['bank', 'cash'])], )
    global_tax = fields.Float(string='Advance payment', readonly=False, compute='_amount_all')
    check = fields.Boolean(string="True false", default=False)

    # raise UserError('Please Select Journal From Bottom')

    @api.depends('order_line.price_total', 'global_tax')
    def _amount_all(self):
        self.check = False
        if self.global_tax >= 1:
            print('usama')
            self.check = True
        """
        Compute the total amounts of the SO.
        """
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            total = self.global_tax

            print(total)
            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'amount_total': amount_untaxed + amount_tax - total,
            })

    def _prepare_invoice(self):
        """
                Prepare the dict of values to create the new invoice for a sales order. This method may be
                overridden to implement custom invoice generation (making sure to call super() to establish
                a clean extension chain).
                """
        self.ensure_one()
        self = self.with_context(default_company_id=self.company_id.id, force_company=self.company_id.id)
        journal = self.env['account.move'].with_context(default_type='out_invoice')._get_default_journal()
        if not journal:
            raise UserError(_('Please define an accounting sales journal for the company %s (%s).') % (
                self.company_id.name, self.company_id.id))

        invoice_vals = {
            'ref': self.client_order_ref or '',
            'type': 'out_invoice',
            'narration': self.note,
            'currency_id': self.pricelist_id.currency_id.id,
            'campaign_id': self.campaign_id.id,
            'medium_id': self.medium_id.id,
            'source_id': self.source_id.id,
            'user_id': self.user_id.id,

            'global_tax': self.global_tax,
            'journal_id': self.journal_id,
            'amount_total': self.amount_total,

            'invoice_user_id': self.user_id.id,
            'team_id': self.team_id.id,
            'partner_id': self.partner_invoice_id.id,
            'partner_shipping_id': self.partner_shipping_id.id,
            'invoice_partner_bank_id': self.company_id.partner_id.bank_ids[:1].id,
            'fiscal_position_id': self.fiscal_position_id.id or self.partner_invoice_id.property_account_position_id.id,
            'journal_id': journal.id,  # company comes from the journal
            'invoice_origin': self.name,
            'invoice_payment_term_id': self.payment_term_id.id,
            'invoice_payment_ref': self.reference,
            'transaction_ids': [(6, 0, self.transaction_ids.ids)],
            'invoice_line_ids': [],
            'company_id': self.company_id.id,
        }
        return invoice_vals



class AccountInvoiceFormGlobalTax(models.Model):
    _inherit = 'account.move'

    journal_id = fields.Many2one(
        'account.journal', 'Payment Journal', domain=[('type', 'in', ['bank', 'cash'])], )
    global_tax = fields.Float(string='Advance Payment', readonly=False)

    @api.onchange('global_tax')
    def _onchange_amount_total(self):
        self.amount_total = (self.amount_untaxed + self.amount_tax) - self.global_tax
        print(self.amount_total, 'Total ')

        @api.depends('invoice_line.price_total', 'global_tax')
        def _amount_all(self):
            self.check = False
            if self.global_tax >= 1:
                print('usama')
                self.check = True
            """
            Compute the total amounts of the SO.
            """
            for order in self:
                amount_untaxed = amount_tax = 0.0
                for line in order.invoice_line_ids:
                    amount_untaxed += line.price_subtotal
                    amount_tax += line.price_tax
                total = self.global_tax

                print(total)
                order.update({
                    'amount_untaxed': amount_untaxed,
                    'amount_tax': amount_tax,
                    'amount_total': amount_untaxed + amount_tax - total,
                })

