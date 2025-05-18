from odoo import fields, api, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    restrict_operation = fields.Boolean('Restrict Operation')
    restrict_location = fields.Boolean('Restrict Location')
    allow_location_ids = fields.Many2many('stock.location')
    restrict_ware_house = fields.Boolean('Restrict warehouse')
    allowed_ware_house_ids = fields.Many2many('stock.warehouse')
    ware_house_picking_type_ids = fields.Many2many('stock.picking.type')

    @api.onchange('restrict_operation', 'restrict_location', 'restrict_ware_house')
    def ware_get(self):
        if self.restrict_ware_house == False:
            self.update({
                'allowed_ware_house_ids': None
            })
        if self.restrict_operation == False:
            self.update({
                'ware_house_picking_type_ids': None
            })
        if self.restrict_location == False:
            self.update({
                'allow_location_ids': None
            })

    @api.onchange('ware_house_picking_type_ids', 'allow_location_ids', 'allowed_ware_house_ids')
    def upgrade_module(self):
        rule = self.env.ref('warehouse_restriction_for_user.restrict_stock_picking')
        picking_ids = [rec.id.origin for rec in self.ware_house_picking_type_ids]
        location_ids = [loc.id.origin for loc in self.allow_location_ids]
        rule.domain_force = ['|', ('picking_type_id', 'in', picking_ids),
                             ('location_id', 'in', location_ids)]
