{
    'name': 'Demo de Catálogo Personalizado',
    'version': '1.0',
    'summary': 'Ejemplo de cómo crear un catálogo y un campo Many2one',
    'description': """
        Este módulo es un ejemplo didáctico para mostrar:
        1. Cómo crear un modelo catálogo (como l10n_latam.identification.type).
        2. Cómo cargar datos por XML.
        3. Cómo crear un campo Many2one en un modelo existente.
    """,
    'author': 'Antigravity',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/catalog_data.xml',
        'views/partner_view.xml',
    ],
    'installable': True,
    'application': False,
}
