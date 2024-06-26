# -*- coding: utf-8 -*-

from odoo import models, fields


class teacher(models.Model):
    _name = 'school.teacher'
    _description = 'school.teacher'

    name = fields.Char(string="Nombre", required=True)
    profile = fields.Text(string="Perfil", required=True)
    subject_ids = fields.One2many("school.subject", "teacher_id", string="Asignaturas")