from odoo import models, fields, api


class grade(models.Model):

    _name = 'school.grade'
    _description = 'school.grade'

    grade = fields.Float(string="Nota", required=True)
    grade_type = fields.Selection([('practice1', 'Práctica 1'),
                                   ('practice2', 'Práctica 2'),
                                   ('final_examen', 'Examen Final')],
                                   string="Tipo de Nota", required=True)
    date = fields.Date(string="Fecha", required=True)
    student_id = fields.Many2one("school.student", string="Estudiante", required=True)
    subject_id = fields.Many2one("school.subject", string="Asignatura", required=True)

    @api.onchange('student_id')
    def _onchange_student_id(self):
        if self.student_id:
            return {
                'domain': {
                    'subject_id': [('id', 'in', self.student_id.subject_ids.ids)]
                }
            }