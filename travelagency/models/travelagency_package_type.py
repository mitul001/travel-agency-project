from odoo import models,fields

class TravelagencyPackageType(models.Model):
    _name = 'travelagency.package.type'
    _description = 'Different package type for packages'

    name = fields.Char(string='Package Type',required=True)

    packages_ids = fields.One2many('travelagency.packages','package_type_id')
