from odoo import models, fields

class MyQualityGrade(models.Model):
    _name = 'my.quality.grade'
    _description = 'Grado de Calidad (Demo)'
    _order = 'sequence, id'

    name = fields.Char(string='Nombre', required=True, translate=True)
    code = fields.Char(string='Código Interno', required=True)
    sequence = fields.Integer(default=10, help='Para ordenar en la lista')
    description = fields.Text(string='Descripción')
