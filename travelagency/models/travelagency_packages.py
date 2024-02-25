from odoo import models,fields

class TravelagencyPackages(models.Model):
    _name = 'travelagency.packages'
    _description = 'Different packages for travel agency'

    name = fields.Char(string='Package Name',required=True)
    days = fields.Integer(string='Days')
    price = fields.Float(string='Price',required=True)
    description = fields.Text(string='Package description')

    package_type_id = fields.Many2one('travelagency.package.type',string='Package Type')
