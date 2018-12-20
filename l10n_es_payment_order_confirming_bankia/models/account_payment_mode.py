# (c) 2016 Soluntec Proyectos y Soluciones TIC. - Rubén Francés , Nacho Torró
# (c) 2015 Serv. Tecnol. Avanzados - Pedro M. Baeza
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api


class AccountPaymentMode(models.Model):
    _inherit = "account.payment.mode"

    conf_bankia_type = fields.Selection(
        string='Tipo de pago', default='T',
        selection=[('T', 'Tranferencia'),
                   ('P', 'Pago domiciliado'),
                   ('C', 'Cheque bancario')])
    bankia_customer_reference = fields.Char(size=10)

    is_conf_bankia = fields.Boolean(compute="_compute_is_conf_bankia")

    @api.multi
    @api.depends('payment_method_id.code')
    def _compute_is_conf_bankia(self):
        for record in self:
            record.is_conf_bankia = record.payment_method_id.code == \
                'conf_bankia'
