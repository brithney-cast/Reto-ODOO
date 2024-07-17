from odoo import models, fields

class OrderLine (models.Model):
    _name = "inventory.order_line"
    _description = "Línea de Orden de venta"

    quantity = fields.Integer(string="Cantidad", required=True)
    price_unit = fields.Float(string="Precio Unitario", required=True)
    subtotal = fields.Float(string="Subtotal", required=True)
    client_id = fields.Many2one("inventory.client", string="Cliente", required=True)
    order_id = fields.Many2one("inventory.order", string="Órden de venta")