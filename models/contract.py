from openerp.osv import osv, fields
from openerp.tools.translate import _

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
         'pay_days': fields.date('Pay day'),
    }
