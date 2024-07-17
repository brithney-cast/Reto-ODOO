from odoo import models, fields

class Client (models.Model):
    _name = "inventory.client"
    _description = "Información del cliente"

    name = fields.Char(string="Nombre completo", required=True)
    email = fields.Char(string="Correo electrónico")
    telephone = fields.Integer(string="Teléfono", required=True)
    order_ids = fields.One2many("inventory.order", "client_id", string="Ordenes de venta")