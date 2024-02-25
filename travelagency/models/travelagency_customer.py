from odoo import fields,models

class TravelagencyCustomer(models.Model):
    _name = 'travelagency.customer'
    _description = 'Customer of Travel Agency'

    name = fields.Char(string='Name',required=True)
    gender = fields.Selection(string='Gender',selection=[('male','Male'), ('female','Female'), ('other','Other')])
    phone = fields.Char(string='Phone Number',required=True)
    email = fields.Char(string='Email')
    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street2')
    city = fields.Char(string='City')
    state = fields.Char(string='State')
    country = fields.Char(string='Country')
    budget = fields.Integer(string='Budget',required=True)

    accommodation_type_id = fields.Many2one('travelagency.accommodation.type')
    packages_type_id = fields.Many2one('travelagency.package.type')
    package_ids = fields.Many2many('travelagency.packages',required=True)
    accommodation_ids = fields.Many2many('travelagency.accommodation',required=True)
