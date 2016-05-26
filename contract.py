from openerp.osv import osv, fields
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp

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

class hr_payslip_input(osv.osv):
    _inherit='hr.payslip.input'
    _columns={
              'qty':fields.float('Quantity'),
              'price':fields.float('Price'),
              'amount': fields.float('Amount',digits_compute=dp.get_precision('Payroll'), help="It is used in computation. For e.g. A rule for \
              sales having 1% commission of basic salary for per product can defined in expression like \
              result = inputs.SALEURO.amount * contract.wage*0.01."),
              }
    
    def onchange_qty_price(self, cr, uid, ids, qty, price,context=None):
        if context is None:
            context = {}
        if qty and price:
            amount = qty * price
        else:
            amount = 0.0
        res = {'value':{
                      'amount':amount
                      }
            }
        return res
    


def _get_nb_of_days(self, cr, uid, ids, field_names, arg=None, context=None):
    result = {}
    for slip in self.browse(cr,uid,ids, context):
        day_from = datetime.strptime(slip.date_from,"%Y-%m-%d")
        day_to = datetime.strptime(slip.date_to,"%Y-%m-%d")
        result[slip.id] = (day_to - day_from).days + 1
    return result

class hr_payslip(osv.osv):
    '''
    Employee Pay Slip
    '''
    _inherit = 'hr.payslip'
    _description = 'Pay Slips'
    _columns = {
        'nb_of_days': fields.function(_get_nb_of_days, method=True, type='integer',string='Total no. of days in month'),
    }
