# -*- coding: utf-8 -*-
from odoo import models, fields, api

class L10nCrCustom(models.Model):
    _inherit = 'account.move'

    electronic_number = fields.Char(string="Electronic Number", readonly=False, default="0012219292")
    electronic_consecutive = fields.Char(string="Electronic Consecutive", readonly=False, default="2033939")






    