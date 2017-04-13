# -*- coding: utf-8 -*-

# 1. Standard library imports:
from datetime import datetime

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models
import openerp.addons.decimal_precision as dp

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class HrPayslip(models.Model):
    
    # 1. Private attributes
    _inherit = 'hr.payslip'

    # 2. Fields declaration
    nb_of_days = fields.Integer('Total no. of days in the payslip period', compute='compute_nb_of_days')
    pay_days = fields.Date('Pay day')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    @api.multi
    def compute_nb_of_days(self):
        for record in self:
            day_from = datetime.strptime(record.date_from,"%Y-%m-%d")
            day_to = datetime.strptime(record.date_to,"%Y-%m-%d")
            record.nb_of_days = (day_to - day_from).days + 1
