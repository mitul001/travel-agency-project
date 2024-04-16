from odoo import models,fields,api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    purchase_ok = fields.Boolean('Can be Purchased',default=False)
    detailed_type = fields.Selection([
        ('consu', 'Consumable'),
        ('service', 'Service')], string='Product Type', default='service', required=True,
        help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
             'A consumable product is a product for which stock is not managed.\n'
             'A service is a non-material product you provide.')
    category = fields.Selection(string='Category', selection=[('package', 'Package'), ('transportation', 'Transportation'),('accommodation', 'Accommodation'),])

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'category' not in vals and 'default_category' in self._context:
                vals['category'] = self._context.get('default_category')
        return super(ProductTemplate, self).create(vals_list)
