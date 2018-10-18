from odoo import models, fields, api, _


class building(models.Model):
    _name = 'building'
    _description = 'Building'
    _inherit = ['mail.thread']
    _inherits = {}
    _order = 'id'

    City = fields.Char("City", ondelete="set null",
                       domain=[])

    Desc = fields.Html("Description", ondelete="set null",
                       domain=[])

    State = fields.Char("State", ondelete="set null",
                        domain=[])

    Zip = fields.Char("Zip", ondelete="set null",
                      domain=[])

    address = fields.Char("Address", ondelete="set null",
                          domain=[])

    code = fields.Char("Building Code", required=True, ondelete="set null",
                       domain=[])

    name = fields.Char("Name", ondelete="set null",
                       domain=[])
