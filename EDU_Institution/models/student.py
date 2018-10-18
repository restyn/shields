from odoo import models, fields, api, _


class student(models.Model):
    _name = 'student'
    _description = 'Student'
    _inherit = ['mail.thread']
    _inherits = {}
    _order = 'id'

    already_partner = fields.Boolean("Already Partner", ondelete="set null",
                                       domain=[])

    birth_date = fields.Date("Birth Date", ondelete="set null",
                               domain=[])

    chosen = fields.Char("Chosen", ondelete="set null",
                           domain=[])

    contacts = fields.One2many("res.partner", "parent_id", string="Contacts", ondelete="set null",
                                 domain=[])

    emergency_contact = fields.Many2one("res.partner", string="Emergency Contact", ondelete="set null",
                                          domain=[])

    gr_no = fields.Char("GR Number", ondelete="set null",
                          domain=[])

    id_number = fields.Char("ID Card Number", ondelete="set null",
                              domain=[])

    last_name = fields.Char("Last Name", ondelete="set null",
                              domain=[])

    middle_name = fields.Char("Middle Name", ondelete="set null",
                                domain=[])

    name = fields.Char("First", required=True, ondelete="set null",
                         domain=[])

    nationality = fields.Many2one("res.country", string="Nationality", ondelete="set null",
                                    domain=[])

    partner_id = fields.Many2one("res.partner", string="Partner", ondelete="set null",
                                   domain=[])

    visa_info = fields.Char("Visa Info", ondelete="set null",
                              domain=[])
