from odoo import models,fields

class TravelagencyAccommodation(models.Model):
    _name = 'travelagency.accommodation'
    _description = 'Accomodation details for travel agency'

    name = fields.Char(string='Accommodation Name',required=True)
    price = fields.Float(string='Price Per Day',required=True)
    description = fields.Text(string='Accommodation description')

    accommodation_type_id = fields.Many2one('travelagency.accommodation.type',string='Accommodation Type')
