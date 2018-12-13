# (c) 2016 Soluntec Proyectos y Soluciones TIC. - Rubén Francés , Nacho Torró
# (c) 2015 Serv. Tecnol. Avanzados - Pedro M. Baeza
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Exportación de fichero bancario Confirming para Bankia',
    'version': '8.0.1.0.0',
    'author': 'Soluntec, '
              'Odoo Community Association (OCA)',
    'contributors': [
        'Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>',
    ],
    'category': 'Localisation/Accounting',
    'website': 'https://github.com/OCA/l10n-spain',
    'license': 'AGPL-3',
    'depends': [
        'l10n_es_base_confirming',
    ],
    'data': [
        'data/account_payment_method.xml',
        'views/account_payment_mode.xml',
    ],
    'installable': True,
}
