# -*- coding: utf-8 -*-

from odoo import models, fields


class product(models.Model):
    _name = 'inventory.product'
    _description = 'dv_inventory.product'

    name = fields.Char()
    description = fields.Text()
    #client_id = fields.Many2one("inventory.client", string="Cliente")
    order_line_ids = fields.One2many("inventory.order_line", "product_id", string="Líneas de Ordenes")
