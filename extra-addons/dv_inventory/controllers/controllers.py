# -*- coding: utf-8 -*-
# from odoo import http


# class DvInventory(http.Controller):
#     @http.route('/dv_inventory/dv_inventory', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dv_inventory/dv_inventory/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dv_inventory.listing', {
#             'root': '/dv_inventory/dv_inventory',
#             'objects': http.request.env['dv_inventory.dv_inventory'].search([]),
#         })

#     @http.route('/dv_inventory/dv_inventory/objects/<model("dv_inventory.dv_inventory"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dv_inventory.object', {
#             'object': obj
#         })
