from openerp.osv import osv, fields
from openerp.tools.translate import _

class hr_contract_finnish(osv.osv):
    _name="hr.contract"
    _inherit="hr.contract"
    
    _columns = {
        'tax_card_type': fields.selection((('A', 'A'), ('B', 'B')), _('Tax card type'), required=False),
        'base_tax_percentage': fields.float('Base tax percentage (%)', required=False),
        'extra_tax_percentage': fields.float('Extra tax percentage (%)', required=False),
        'yearly_income_limit': fields.float('Yearly income limit', required=False),
        'monthly_income_limit': fields.float('Monthly income limit', required=False),
        
        'benefit_car': fields.float('Car benefit', required=False),
        'benefit_apartment': fields.float('Apartment benefit', required=False),
        'benefit_lunch': fields.float('Lunch benefit', required=False),
        'benefit_other': fields.float('Other benefit', required=False),
        'membership_fee':fields.float('Membership fee (%)'),
    }
    
    _defaults = {
        
        'base_tax_percentage': 0.0,
        'extra_tax_percentage': 0.0,
        'yearly_income_limit': 0.0,
        'monthly_income_limit': 0.0,
        
        'benefit_car': 0.0,
        'benefit_apartment': 0.0,
        'benefit_lunch': 0.0,
        'benefit_other': 0.0,
    }

hr_contract_finnish()