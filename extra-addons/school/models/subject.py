# -*- coding: utf-8 -*-

from odoo import models, fields


class subject(models.Model):
    _name = 'school.subject'
    _description = 'school.subject'

    name = fields.Char(string="Nombre", required=True)
    credits = fields.Integer(string="Créditos", required=True)
    max_students = fields.Integer(string="Máximo de Estudiantes", required=True)
    active = fields.Boolean(string="Activo", default=True)
    student_ids = fields.Many2many("school.student", string="Estudiantes")
    

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
