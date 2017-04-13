# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models
import openerp.addons.decimal_precision as dp

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class HrPayslipInput(models.Model):
    
    # 1. Private attributes
    _inherit = 'hr.payslip.input'

    # 2. Fields declaration
    qty = fields.Float('Quantity')
    price = fields.Float('Price')
    amount = fields.Float(
        string='Amount',
        digits_compute=dp.get_precision('Payroll'),
        help="It is used in computation. For e.g. A rule for sales having 1% commission of basic salary for \
         per product can defined in expression like result = inputs.SALEURO.amount * contract.wage*0.01.")

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges
    @api.onchange('qty', 'price')
    def onchange_qty_update_price(self):
        for record in self:
            amount = 0.00

            if record.qty and record.price:
                amount = record.qty * record.price

            record.amount = amount

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
