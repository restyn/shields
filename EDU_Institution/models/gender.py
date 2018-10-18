from odoo import models, fields, api, _


class gender(models.Model):
    _name = 'gender'
    _description = 'gender'
    _inherit = 'base'
    _inherits = {}
    _order = 'id'

    name = fields.Char("Name", ondelete="set null",
                         domain=[])
