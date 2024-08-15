from odoo import http
from odoo.http import request

class Test(http.Controller):
    @http.route('/odoo_test/odoo_test/', auth='public', website=True)
    def index(self, **kw):
        material = request.env['material.material'].sudo().search([])
        return request.render('odoo_test.materials_page',{
            'material' : material,
        })