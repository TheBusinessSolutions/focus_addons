# Copyright (C) 2019 Open Source Integrators
# Copyright (C) 2019 Serpent consulting Services
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class FSMRoute(models.Model):
    _name = "fsm.route"
    _description = "Field Service Route"

    name = fields.Char(required=True)
    fsm_person_id = fields.Many2one(comodel_name="fsm.person", string="Person")
    day_ids = fields.Many2many(comodel_name="fsm.route.day", string="Days")
    max_order = fields.Integer(
        string="Maximum Orders",
        default=0,
        help="Maximum number of orders per day route.",
    )

    def run_on(self, date):
        """
        :param date: date
        :return: True if the route runs on the date, False otherwise.
        """
        if date:
            day_index = date.weekday()
            day = self.env.ref("fieldservice_route.fsm_route_day_" + str(day_index))
            return day in self.day_ids

    def write(self, vals):
        if "fsm_person_id" in vals:
            new_person_id = vals["fsm_person_id"]
            today = fields.Date.today()

            for route in self:
                dayroutes = self.env["fsm.route.dayroute"].search(
                    [
                        ("route_id", "=", route.id),
                        ("date", ">=", today),
                    ]
                )

                dayroutes.write({"person_id": new_person_id})

                for dayroute in dayroutes:
                    orders_to_update = dayroute.order_ids.filtered(
                        lambda o: o.fsm_route_id == route and not o.is_closed
                    )
                    orders_to_update.write({"person_id": new_person_id})

        return super().write(vals)
