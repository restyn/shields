from odoo import models, fields, api, _


class room(models.Model):
    _name = 'room'
    _description = 'Rooms'
    _inherit = 'base'
    _inherits = {}
    _order = 'id'

    Building = fields.Many2one("building", string="Building", ondelete="set null")

    Desc = fields.Html("Description", ondelete="set null",
                       domain=[])

    Floor = fields.Char("Floor", ondelete="set null",
                        domain=[])

    Seats = fields.Integer("Seats", ondelete="set null",
                           domain=[],
                           help="Capacity of the room")

    code = fields.Char("Number / Code", required=True, ondelete="set null",
                       domain=[])

    name = fields.Char("Name", ondelete="set null",
                       domain=[])
