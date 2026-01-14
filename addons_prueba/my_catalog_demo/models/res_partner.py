from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Este es el campo Many2one que se alimenta del modelo de arriba
    quality_grade_id = fields.Many2one(
        'my.quality.grade', 
        string='Grado de Calidad',
        help='Selecciona el nivel de calidad asignado a este contacto.'
    )
