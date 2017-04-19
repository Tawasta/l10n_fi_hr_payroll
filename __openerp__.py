# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright Plan First Oy (http://www.plan1st.fi/)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################

{
    'name': 'Finnish Salary',
    'summary': 'Adds fields to HR contracts for calculating Finnish salaries',
    'version': '8.0.1.2.33',
    'category': 'Human Resources',
    'website': 'http://www.plan1st.fi',
    'author': 'Oy Tawasta Technologies Ltd.',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
    'depends': [
        'hr',
        'hr_contract',
        'hr_payroll',
    ],
    'data': [
        'data/hr_contribution_register.xml',
        'data/hr_salary_rule_category.xml',
        'data/hr_salary_rule.xml',  # Salary rules refer to contribution register and rule category
        'data/hr_rule_input.xml',  # Inputs refer to salary rules

        'views/contract_view.xml',
    ],
    'demo': [
    ],
}