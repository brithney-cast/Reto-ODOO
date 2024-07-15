# -*- coding: utf-8 -*-

from odoo import models, fields


class Subject(models.Model):
    _name = 'school.subject'
    _description = 'school.subject'

    name = fields.Char(string="Nombre", required=True)
    credits = fields.Integer(string="Créditos", required=True)
    max_students = fields.Integer(string="Máximo de Estudiantes", required=True)
    active = fields.Boolean(string="Activo", default=True)
    student_ids = fields.Many2many("school.student", string="Estudiantes")
    teacher_id = fields.Many2one("school.teacher", string="Profesor")