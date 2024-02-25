from odoo import models,fields

class TravelagencyAccommodationType(models.Model):
    _name = 'travelagency.accommodation.type'
    _description = 'Different accommodation type for packages'

    name = fields.Char(string='Accommodation Type',required=True)

    accommodation_ids = fields.One2many('travelagency.accommodation','accommodation_type_id')
