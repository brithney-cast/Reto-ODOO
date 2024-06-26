# -*- coding: utf-8 -*-

from odoo import models, fields


class student(models.Model):
    _name = 'school.student'
    _description = 'school.student'

    name = fields.Char(string="Nombre", required=True)
    birth_date = fields.Date(string="Fecha de Nacimiento", required=True)
    age = fields.Integer(string="Edad")
    final_exam_grade = fields.Float(string="Nota Examen Final")
    subject_ids = fields.Many2many("school.subject", string="Asignaturas")
    