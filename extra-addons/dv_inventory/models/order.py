from odoo import models, fields, api, exceptions

class Order (models.Model):
    _name = "inventory.order"
    _description = "Orden de venta"

    name = fields.Char(string="Nombre de  orden de venta")
    date_order = fields.Datetime(string="Fecha de orden de venta", default=fields.Datetime.now)
    amount_total = fields.Float(string="Monto total")

    client_id = fields.Many2one("inventory.client", string="Cliente", required=True)
    order_line_ids = fields.One2many("inventory.order_line", "order_id", string="Línea de órdenes de venta")

    @api.model
    def create(self, values_list):
        if not values_list.get("name"):
            raise exceptions.ValidationError("El campo de nombre de venta es obligatorio")
        if not values_list.get("date_order"):
            raise exceptions.ValidationError("El campo de fecha de orden de venta es obligatorio")
        if not values_list.get("amount_total"):
            raise exceptions.ValidationError("El campo de monto total es obligatorio")
        if not values_list.get("order_line_ids"):
            raise exceptions.ValidationError("La orden de venta debe tener al menos una línea de orden de venta")
        
        return super(Order, self).create(values_list)
        
