# -*- coding: utf-8 -*-
from odoo import http

# class Citassls(http.Controller):
#     @http.route('/citassls/citassls/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/citassls/citassls/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('citassls.listing', {
#             'root': '/citassls/citassls',
#             'objects': http.request.env['citassls.citassls'].search([]),
#         })

#     @http.route('/citassls/citassls/objects/<model("citassls.citassls"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('citassls.object', {
#             'object': obj
#         })