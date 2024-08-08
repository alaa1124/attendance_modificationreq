# -*- coding: utf-8 -*-
# from odoo import http


# class AttendanceModificationreq(http.Controller):
#     @http.route('/attendance_modificationreq/attendance_modificationreq', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/attendance_modificationreq/attendance_modificationreq/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('attendance_modificationreq.listing', {
#             'root': '/attendance_modificationreq/attendance_modificationreq',
#             'objects': http.request.env['attendance_modificationreq.attendance_modificationreq'].search([]),
#         })

#     @http.route('/attendance_modificationreq/attendance_modificationreq/objects/<model("attendance_modificationreq.attendance_modificationreq"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('attendance_modificationreq.object', {
#             'object': obj
#         })

