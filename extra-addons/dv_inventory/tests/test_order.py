from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestOrder(TransactionCase):

    def setUp(self):
        super(TestOrder, self).setUp()
        # Crea datos de prueba aquí
        self.client = self.env['inventory.client'].create({
            'name': 'Cliente Prueba',
            'telephone': 75698465
        })
        self.product = self.env['inventory.product'].create({
            'name': 'Mesa'
        })
        self.order_line = self.env['inventory.order_line'].create({
            'product_id': self.product.id,
            'quantity': 1,
            'price_unit': 10.0,
            'subtotal': 12,
            'client_id': self.client.id
        })

    def test_create_order(self):
        order = self.env['inventory.order'].create({
            'name': 'Orden de Abastacemiento',
            'date_order': '2024-07-26 10:00:00',
            'amount_total': 60,
            'client_id': self.client.id,
            'order_line_ids': [(6, 0, [self.order_line.id])]
        })
        self.assertEqual(order.name, 'Orden de Abastacemiento')
        self.assertEqual(order.amount_total, 60.0)

    def test_create_order_error(self):
        with self.assertRaises(ValidationError):
            self.env['inventory.order'].create({
                'date_order': '2024-07-26 12:00:00',
                'amount_total': 100.0,
                'client_id': self.client.id,
                'order_line_ids': [(6, 0, [self.order_line.id])]
            })
