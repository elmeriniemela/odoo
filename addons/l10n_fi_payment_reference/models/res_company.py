
from odoo import models, _

class ResCompany(models.Model):
    _inherit = "res.company"

    def _get_invoice_reference_types(self):
        types = super()._get_invoice_reference_types()
        types.extend([
            ('fi_bank_reference', _('Finnish Bank Reference')),
            ('rf_bank_reference', _('International Bank Reference')),
        ])
        return types
