from odoo import api,fields,models
from builtins import sum

class taCustomer(models.Model):
    _name = 'ta.customer'
    _description = 'Customer of Travel Agency'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'partner_id'

    partner_id = fields.Many2one(
        'res.partner',
        string='Customer',
        tracking=True,
        required=True
    )
    gender = fields.Selection(string='Gender',selection=[('male','Male'), ('female','Female'), ('other','Other')])
    phone = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street2')
    city = fields.Char(string='City')
    country_id = fields.Many2one(comodel_name='res.country', string='Country')
    state_id = fields.Many2one(comodel_name='res.country.state', string='State')
    
    status= fields.Selection(string='Status',tracking=True,selection=[
    ('new', 'New'),('package_added', 'Package Added'),('confirmed', 'Confirmed'),('cancelled', 'Cancelled')],default='new')
    date_from = fields.Date('Date From')
    date_to = fields.Date('Date To')
    invoice_date = fields.Date(string='Invoice Date', default=fields.Date.today)
    package_ids = fields.Many2many('product.template',relation='package_rel',required=True,tracking=True)
    accommodation_ids = fields.Many2many('product.template',relation='acc_rel',required=True,tracking=True)
    transportation_ids = fields.Many2many('product.template',relation='transport_rel',required=True,tracking=True)

    total_amount = fields.Float(string='Total Amount',compute='_compute_total_cost',store=True)
    
    @api.depends('package_ids','accommodation_ids','transportation_ids')
    def _compute_total_cost(self):
        for record in self:
            record.total_amount = sum(record.package_ids.mapped('list_price') + record.accommodation_ids.mapped('list_price')+ record.transportation_ids.mapped('list_price'))
    
    @api.onchange('state_id')
    def _set_country_id(self):
        for record in self:
            if record.state_id:
                record.country_id = record.state_id.country_id


    @api.onchange('package_ids','accommodation_ids')
    def _onchange_status(self):
        for record in self:
            if record.package_ids or record.accommodation_ids or record.transportation_ids:
                record.status = 'package_added'
            else:
                record.status = 'new'

    def action_confirm(self):
        self.ensure_one()  
        self.status = 'confirmed'
        sequence = self.env['ir.sequence'].next_by_code('travel.customer')
        for record in self:
            invoice_line_ids = []
            for product in record.package_ids | record.accommodation_ids | record.transportation_ids:
                invoice_line_ids.append((0, 0, {
                    "product_id": product.id,
                    "name": product.name,
                    "quantity": 1,
                    "price_unit": product.list_price,
                }))
            self.env['account.move'].create({
                "name": sequence,
                "partner_id": record.partner_id.id,
                "invoice_date": record.invoice_date,
                "move_type": "out_invoice",
                "invoice_line_ids": invoice_line_ids,
            })

    def action_cancel(self):
        self.status = 'cancelled'
