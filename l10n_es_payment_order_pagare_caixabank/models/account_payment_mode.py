# -*- coding: utf-8 -*-
# (c) 2018 Comunitea Servicios Tecnológicos - Javier Colmenero
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api


class AccountPaymentMode(models.Model):
    _inherit = "account.payment.mode"

    is_pagare_caixabank = fields.Boolean(
        string="Is Pagaré Caixabank",
        compute="_compute_is_pagare_caixabank")

    @api.multi
    @api.depends('payment_method_id.code')
    def _compute_is_pagare_caixabank(self):
        for record in self:
            record.is_pagare_caixabank = record.payment_method_id.code == \
                'pagare_caixabank'
