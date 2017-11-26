from openerp import models, fields, api


class USOHHrContract(models.Model):
    _inherit = 'hr.contract'

    oh_income_allowances = fields.Integer(string='Ohio Income Allowances', default=0)
    oh_unemp_rate_2016 = fields.Float(string="Ohio Unemployment Rate 2016", compute="fetch_oh_unemp_rate_2016")
    oh_unemp_rate_2017 = fields.Float(string="Ohio Unemployment Rate 2017", compute="fetch_oh_unemp_rate_2017")

    @api.multi
    def fetch_oh_unemp_rate_2016(self):
        for contract in self:
            contract.oh_unemp_rate_2016 = 0.0 if (contract.futa_type == self.FUTA_TYPE_BASIC) \
                else contract.employee_id.company_id.oh_unemp_rate_2016

    @api.multi
    def fetch_oh_unemp_rate_2017(self):
        for contract in self:
            contract.oh_unemp_rate_2017 = 0.0 if (contract.futa_type == self.FUTA_TYPE_BASIC) \
                else contract.employee_id.company_id.oh_unemp_rate_2017


class OHCompany(models.Model):
    _inherit = 'res.company'

    # Defaults from :: https://jfs.ohio.gov/ouc/uctax/rates.stm
    oh_unemp_rate_2016 = fields.Float(string="Ohio Unemployment Rate 2016", default=2.7)
    oh_unemp_rate_2017 = fields.Float(string="Ohio Unemployment Rate 2017", default=2.7)
