# -*- coding: utf-8 -*-

from odoo import models, fields, api

class attendance_modificationreq(models.Model):
    _name = 'attendance_modificationreq.attendance_modificationreq'
    _description = 'Attendance Modification Request'

    name = fields.Char(string='Name', required=True, copy=False, readonly=True, default='New')
    employeename = fields.Many2one('hr.employee', string='Employee', required=True)
    date = fields.Date(string='date')
    type = fields.Selection([
        ('check_in', 'Check In'),
        ('check_out', 'Check Out')
    ], string='Type', required=True)
    action = fields.Selection([
        ('new_record', 'New Record'),
        ('modifcation', 'Modification')
    ], string='Action Type', required=True, default='new_record')
    reason = fields.Text()
    attendance = fields.Many2one(
        'hr.attendance',
        string='Attendance',
        domain="[('employee_id', '=', employeename)]"
    )
    updated_check_in = fields.Datetime(string='Updated Check-In')
    updated_check_out = fields.Datetime(string='Updated Check-Out')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
    ], string='Status', default='draft')

    def action_confirm(self):
        """Change the state of the request to 'confirmed'."""
        self.state = 'confirmed'

    show_confirm_button = fields.Boolean(compute='_compute_show_confirm_button')

    @api.depends('state')
    def _compute_show_confirm_button(self):
        for rec in self:
            rec.show_confirm_button = (rec.state == 'draft')


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('attendance_modificationreq.seq') or 'New'
        return super(attendance_modificationreq, self).create(vals)
