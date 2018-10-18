from odoo import models, fields, api, _


class faculty(models.Model):
    _name = 'faculty'
    _description = 'Faculty'
    _inherit = ['mail.thread']
    _inherits = {}
    _order = 'id'

    EmerContact = fields.Many2one("res.partner", string="Emergency Contact", ondelete="set null",
                                    domain=[])

    bio = fields.Html("Instructor Bio", ondelete="set null",
                        domain=[])

    birth_date = fields.Date("BirthDate", ondelete="set null",
                               domain=[])

    gender = fields.Many2one("gender", string="Gender", ondelete="set null",
                               domain=[])

    last_name = fields.Char("Last Name", required=True, ondelete="set null",
                              domain=[])

    middle_name = fields.Char("MiddleName", ondelete="set null",
                                domain=[])

    name = fields.Char("Name", ondelete="set null",
                         domain=[])

    nationality = fields.Many2one("res.country", string="Nationality", ondelete="set null",
                                    domain=[])

    partner = fields.Many2one("res.partner", string="Partner", ondelete="cascade",
                                domain=[])

    visa = fields.Char("Visa Number", ondelete="set null",
                         domain=[])

    visainfo = fields.Char("Visa Info", ondelete="set null",
                             domain=[])
