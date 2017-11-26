from odoo import models, fields, api


class USHrContract(models.Model):
    FUTA_TYPE_EXEMPT = 'exempt'
    FUTA_TYPE_BASIC = 'basic'
    FUTA_TYPE_NORMAL = 'normal'

    _inherit = 'hr.contract'

    w4_allowances = fields.Integer(string='Federal W4 Allowances', default=0)
    w4_filing_status = fields.Selection([
        ('', 'Exempt'),
        ('single', 'Single'),
        ('married', 'Married'),
        ('married_as_single', 'Married but at Single Rate'),
    ], string='Federal W4 Filing Status', default='single')
    w4_is_nonresident_alien = fields.Boolean(string="Federal W4 Is Nonresident Alien", default=False)
    w4_additional_withholding = fields.Float(string="Federal W4 Additional Withholding", default=0.0)

    external_wages = fields.Float(string='External Existing Wages', default=0.0)

    futa_type = fields.Selection([
        (FUTA_TYPE_EXEMPT, 'Exempt (0%)'),
        (FUTA_TYPE_NORMAL, 'Normal Net Rate (0.6%)'),
        (FUTA_TYPE_BASIC, 'Basic Rate (6%)'),
    ], string="Federal Unemployment Tax Type (FUTA)", default='normal')

    futa_rate_2016 = fields.Float(string="Federal Unemployment Rate 2016", compute="compute_futa_rate_2016")
    futa_rate_2017 = fields.Float(string="Federal Unemployment Rate 2017", compute="compute_futa_rate_2017")

    @api.multi
    def compute_futa_rate_2016(self):
        for contract in self:
            if contract.futa_type == self.FUTA_TYPE_EXEMPT:
                contract.futa_rate_2016 = 0.0
            elif contract.futa_type == self.FUTA_TYPE_NORMAL:
                contract.futa_rate_2016 = 0.6
            else:
                contract.futa_rate_2016 = 6.0

    @api.multi
    def compute_futa_rate_2017(self):
        for contract in self:
            if contract.futa_type == self.FUTA_TYPE_EXEMPT:
                contract.futa_rate_2017 = 0.0
            elif contract.futa_type == self.FUTA_TYPE_NORMAL:
                contract.futa_rate_2017 = 0.6
            else:
                contract.futa_rate_2017 = 6.0
