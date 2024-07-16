from odoo import models, fields

class Client (models.Model):
    _name = "inventory.client"
    _description = "Información del cliente"

    name = fields.Char(string="Nombre completo")
    email = fields.Char(string="Correo electrónico")
    telephone = fields.Integer(string="Teléfono")
    product_ids = fields.One2many("inventory.product", "client_id", string="Productos")