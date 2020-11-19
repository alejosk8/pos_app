# -*- coding: utf-8 -*-
from odoo import http

# class ChochosApp(http.Controller):
#     @http.route('/chochos_app/chochos_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/chochos_app/chochos_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('chochos_app.listing', {
#             'root': '/chochos_app/chochos_app',
#             'objects': http.request.env['chochos_app.chochos_app'].search([]),
#         })

#     @http.route('/chochos_app/chochos_app/objects/<model("chochos_app.chochos_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('chochos_app.object', {
#             'object': obj
#         })