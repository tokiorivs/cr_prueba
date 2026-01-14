{
    'name': 'Costa Rica - Extended Localization',
    'version': '1.0',
    'category': 'Accounting/Localizations',
    'summary': 'Extension for Costa Rica Localization',
    'description': """
Extended functionalities for l10n_cr.
This module inherits from l10n_cr to allow custom modifications for Costa Rica localization.
    """,
    'author': 'User',
    'depends': ['base', 'l10n_cr', 'account', 'l10n_latam_invoice_document', 'l10n_latam_base'],
    'data': [
        'views/account_move_views.xml',
        'views/report_invoice.xml',
        'data/l10n_latam_document_type_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
