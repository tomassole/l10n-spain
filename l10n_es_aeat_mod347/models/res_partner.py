# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.multi
    def _compute_num_347_records(self):
        record_obj = self.env['l10n.es.aeat.mod347.partner_record']
        for partner in self:
            cond = [('partner_id', '=', partner.id)]
            partner.num_347_records = len(record_obj.search(cond))

    not_in_mod347 = fields.Boolean(
        "Not included in 347 report",
        help="If you mark this field, this partner will not be included in "
             "any AEAT 347 model report, independently from the total "
             "amount of its operations.", default=False,
    )
    num_347_records = fields.Integer(
        string='AEAT 347 partner records', compute='_compute_num_347_records')

    @api.model
    def _commercial_fields(self):
        res = super(ResPartner, self)._commercial_fields()
        res += ['not_in_mod347']
        return res

    @api.multi
    def show_partner_347_records(self):
        res = {
            'view_mode': 'tree,form',
            'res_model': 'l10n.es.aeat.mod347.partner_record',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'domain': [('partner_id', '=', self.id)],
            'context':
                {'tree_view_ref': 'l10n_es_aeat_mod347.l10n_es_aeat_'
                 'mod347_partner_record_tree_view'}}
        return res
