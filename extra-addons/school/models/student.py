# -*- coding: utf-8 -*-

from odoo import models, fields, api


class student(models.Model):
    _name = 'school.student'
    _description = 'school.student'

    name = fields.Char(string="Nombre", required=True)
    birth_date = fields.Date(string="Fecha de Nacimiento", required=True)
    age = fields.Integer(compute="_get_age", store=True, string="Edad")
    final_exam_grade = fields.Float(string="Nota Examen Final")
    subject_ids = fields.Many2many("school.subject", string="Asignaturas")
    grade_ids = fields.One2many("school.grade", "student_id", string="Notas")


    @api.depends('birth_date')
    def _get_age(self):
        try:
            for student in self:
                if student.birth_date:
                    age = fields.Date.today() - student.birth_date
                    student.age = age.days // 365
                else:
                    student.age  = 0
        except Exception as e:
            student.age = 0
            print(f"Se encontró un error al calcular la edad para el registro {student.id}: {e}")

    