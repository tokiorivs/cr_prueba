from odoo import models, fields

class L10nLatamIdentificationType(models.Model):
    _inherit="l10n_latam.identification.type"

    l10n_cr_vat_code = fields.Char()