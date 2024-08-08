# -*- coding: utf-8 -*-

from odoo import models, fields, api


class attendance_modificationreq(models.Model):
    _name = 'attendance_modificationreq.attendance_modificationreq'
    _description = 'attendance_modificationreq.attendance_modificationreq'

    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, default='New')
    employeename = fields.Many2one('hr.employee', string='Employee', required=True)
    Date = fields.Date(string='Date')
    type = fields.Selection([
        ('check_in', 'Check In'),
        ('check_out', 'Check Out')
    ], string='Type', required=True)
    action = fields.Selection([
        ('new_record', 'New Record'),
        ('modifcation', 'Modifcation')
    ], string='Type', required=True)
    reason = fields.Text()
    attendance = fields.Many2one(
        'hr.attendance',
        string='Attendance',
        domain=lambda self: [('employee_id', '=', self.employeename.id)],
        states={'draft': [('readonly', False)]},
        attrs={'invisible': [('state', '!=', 'draft')]}
    )

    

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('attendance_modificationreq.seq') or 'New'
        return super(attendance_modificationreq, self).create(vals)
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

