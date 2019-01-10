# Copyright 2017 FactorLibre - Ismael Calvo <ismael.calvo@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    sii_sale_description = fields.Char(string='SII Description for sales')
    sii_purchase_description = fields.Char(string='SII Description for '
                                                  'purchases')
