# -*- coding: utf-8 -*-
from odoo import http




class OdooInfo(http.Controller):
    @http.route('/odoo_info/odoo_info', auth='public')
    def index(self, **kw):
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        return "Hello, world"

    @http.route('/odoo_info/odoo_info/objects', auth='public')
    def list(self, **kw):
        return http.request.render('odoo_info.listing', {
            'root': '/odoo_info/odoo_info',
            'objects': http.request.env['odoo_info.odoo_info'].search([]),
        })

    @http.route('/odoo_info/odoo_info/objects/<model("odoo_info.odoo_info"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('odoo_info.object', {
            'object': obj
        })

    @http.route('/odoo_info/version', auth='public')
    def version(self, **kw):
        #env = http.request.env
        #print(env)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        return "Versionx 1.0"
