# -*- coding: utf-8 -*-
# from odoo import http


# class VrHideCost(http.Controller):
#     @http.route('/vr_hide_cost/vr_hide_cost/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vr_hide_cost/vr_hide_cost/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vr_hide_cost.listing', {
#             'root': '/vr_hide_cost/vr_hide_cost',
#             'objects': http.request.env['vr_hide_cost.vr_hide_cost'].search([]),
#         })

#     @http.route('/vr_hide_cost/vr_hide_cost/objects/<model("vr_hide_cost.vr_hide_cost"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vr_hide_cost.object', {
#             'object': obj
#         })
