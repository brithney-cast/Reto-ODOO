from odoo import models, fields

class Order (models.Model):
    _name = "inventory.order"
    _description = "Orden de venta"

    name = fields.Char(string="Nombre de  orden de venta", required=True)
    date_order = fields.Datetime(string="Fecha de orden de venta", default=fields.Datetime.now)
    client_id = fields.Many2one("inventory.client", string="Cliente", required=True)
    order_line_ids = fields.One2many("inventory.order_line", "order_id", string="Línea de órdenes de venta", required=True)
