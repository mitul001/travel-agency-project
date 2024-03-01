from odoo import api,fields,models

class TravelagencyCustomer(models.Model):
    _name = 'travelagency.customer'
    _description = 'Customer of Travel Agency'
    _inherit = ['mail.thread.main.attachment', 'mail.activity.mixin']

    name = fields.Char(string='Name',required=True,tracking=True)
    gender = fields.Selection(string='Gender',selection=[('male','Male'), ('female','Female'), ('other','Other')])
    phone = fields.Char(string='Phone Number',required=True)
    email = fields.Char(string='Email')
    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street2')
    city = fields.Char(string='City')
    state = fields.Char(string='State')
    country = fields.Char(string='Country')
    package_budget = fields.Float(string='Package Budget',required=True)
    accommodation_budget = fields.Float(string='Accommodation Budget',required=True)
    budget = fields.Float(string='Budget',compute="_compute_total_budget")
    status= fields.Selection(string='Status',tracking=True,selection=[
    ('new', 'New'),('package_added', 'Package Added'),('confirmed', 'Confirmed'),('cancelled', 'Cancelled')],default=str('new'))
    accommodation_type_id = fields.Many2one('travelagency.accommodation.type')
    packages_type_id = fields.Many2one('travelagency.package.type')
    package_ids = fields.Many2many('travelagency.packages',required=True,tracking=True)
    accommodation_ids = fields.Many2many('travelagency.accommodation',required=True,tracking=True)

    @api.depends('package_budget','accommodation_budget')
    def _compute_total_budget(self):
        for record in self:
            record.budget=record.accommodation_budget+record.package_budget

    @api.onchange('package_ids','accommodation_ids')
    def _onchange_status(self):
        if self.package_ids or self.accommodation_ids:
            self.status = 'package_added'
        else:
            self.status = 'new'

    def action_confirm(self):
        self.status = 'confirmed'

    def action_cancel(self):
        self.status = 'cancelled'