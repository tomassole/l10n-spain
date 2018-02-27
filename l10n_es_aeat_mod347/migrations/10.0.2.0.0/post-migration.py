from odoo import SUPERUSER_ID, fields
from odoo.api import Environment
import json
from datetime import datetime


def migrate(cr, version):
    env = Environment(cr, SUPERUSER_ID, {})
    invoice_obj = env['account.invoice']
    invoices = invoice_obj.search([('company_id', 'not in', [1,])])
    invoices._compute_amount_total_wo_irpf()
