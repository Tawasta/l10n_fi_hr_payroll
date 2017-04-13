# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class HrContract(models.Model):
    
    # 1. Private attributes
    _inherit = 'hr.contract'

    # 2. Fields declaration
    tax_card_type = fields.Selection((('A', 'A'), ('B', 'B')), 'Tax card type', required=False)
    base_tax_percentage = fields.Float('Base tax percentage (%)', required=False, default=0.0)
    extra_tax_percentage = fields.Float('Extra tax percentage (%)', required=False, default=0.0)
    yearly_income_limit = fields.Float('Yearly income limit', required=False, default=0.0)
    monthly_income_limit = fields.Float('Monthly income limit', required=False, default=0.0)

    benefit_car = fields.Float('Car benefit', required=False, default=0.0)
    benefit_apartment = fields.Float('Apartment benefit', required=False, default=0.0)
    benefit_lunch = fields.Float('Lunch benefit', required=False, default=0.0)
    benefit_other = fields.Float('Other benefit', required=False, default=0.0)
    membership_fee = fields.Float('Membership fee (%)')
    union = fields.Char('Union')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
