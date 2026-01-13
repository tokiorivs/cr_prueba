# -*- coding: utf-8 -*-
from odoo import models, fields, api

class L10nCrCustom(models.Model):
    _inherit = 'account.move'

    electronic_number = fields.Char("Electronic Number")
    electronic_consecutive = fields.Char("Electronic Consecutive")






    