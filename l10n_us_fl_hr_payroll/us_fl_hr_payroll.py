from odoo import models, fields, api


class USFLHrContract(models.Model):
    _inherit = 'hr.contract'

    fl_unemp_rate_2016 = fields.Float(string="Florida Unemployment Rate 2016", compute="fetch_fl_unemp_rate_2016")
    fl_unemp_rate_2017 = fields.Float(string="Florida Unemployment Rate 2017", compute="fetch_fl_unemp_rate_2017")

    @api.multi
    def fetch_fl_unemp_rate_2016(self):
        for contract in self:
            contract.fl_unemp_rate_2016 = 0.0 if (contract.futa_type == self.FUTA_TYPE_BASIC) \
                else contract.employee_id.company_id.fl_unemp_rate_2016

    @api.multi
    def fetch_fl_unemp_rate_2017(self):
        for contract in self:
            contract.fl_unemp_rate_2017 = 0.0 if (contract.futa_type == self.FUTA_TYPE_BASIC) \
                else contract.employee_id.company_id.fl_unemp_rate_2017


class FLCompany(models.Model):
    _inherit = 'res.company'

    # Defaults from :: http://floridarevenue.com/dor/taxes/reemployment.html
    fl_unemp_rate_2016 = fields.Float(string="Florida Unemployment Rate 2016", default=2.7)
    fl_unemp_rate_2017 = fields.Float(string="Florida Unemployment Rate 2017", default=2.7)
