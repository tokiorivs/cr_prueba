# -*- coding: utf-8 -*-
from odoo import models, fields, api

class L10nCrCustom(models.Model):
    _inherit = 'account.move'

    def _get_electronic_number(self):
        return "0" * 50

    def _get_electronic_consecutive(self):
        return "0" * 20

    electronic_number = fields.Char(string="Electronic Number", readonly=False, default=_get_electronic_number)
    electronic_consecutive = fields.Char(string="Electronic Consecutive", readonly=False, default=_get_electronic_consecutive)




    