from odoo import models,fields

class TravelagencyPreferenceTag(models.Model):
    _name = 'travelagency.preference.tag'
    _description = 'different tags for preference'

    name = fields.Char(string='Tags',required=True)
    color =  fields.Integer(string='Color')

    _sql_constraints = [('Uniq_name','UNIQUE(name)','A preference tag name must be unique')]
