from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ModulOdoo(models.Model):
    _name = 'material.material'
    _description = 'matrial.material'
    _rec_name = 'code'

    code = fields.Char(string="Material Code", required=True)
    name = fields.Char(string="Material Name", required=True)
    tipe = fields.Selection([
        ('fabric', 'Fabric'),
        ('jenas', 'Jeans'),
        ('cotton', 'Cotton')], string="Material Type", required=True)
    buy_price = fields.Integer(string="Material Buy Price", required=True)
    supplier_id = fields.Many2one('res.partner', string="Supplier", required=True)

    @api.model
    def create(self, vals):
        if vals['buy_price'] < 100:
            raise ValidationError('Buy Price cannot be less than 100')
        result = super(ModulOdoo, self).create(vals)

        return result


    def write(self, vals):
        if vals['buy_price'] < 100:
            raise ValidationError('Buy Price cannot be less than 100')
        result = super(ModulOdoo, self).write(vals)
        
        return result