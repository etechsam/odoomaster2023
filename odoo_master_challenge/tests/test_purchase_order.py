# Copyright 2023 Etech
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from .common import PurchaseOrderCommon
from odoo.exceptions import ValidationError


class TestPurchaseOrder(PurchaseOrderCommon):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.order_1 = cls.env['purchase.order'].create({
            'partner_id': cls.no_need_approval_supplier.id,
            'order_line': [
                (0, 0, {
                    'product_id': cls.product_1.id,
                    'product_qty': 10,
                    'price_unit': 300
                })
            ]
        })

        cls.order_2 = cls.env['purchase.order'].create({
            'partner_id': cls.need_approval_supplier.id,
            'order_line': [
                (0, 0, {
                    'product_id': cls.product_1.id,
                    'product_qty': 10,
                    'price_unit': 300
                })
            ]
        })

    def test_purchase_order_buyer(self):
        self.assertFalse(self.order_1.user_id.id)
        self.assertFalse(self.order_2.user_id.id)

    def test_duplication_purchase_order(self):
        self.order_1.user_id = self.purchase_user
        new_order = self.order_1.copy()
        self.assertFalse(new_order.user_id.id)

    def test_purchase_order_need_approval_no_user_id(self):
        with self.assertRaises(ValidationError):
            self.order_2.with_user(self.purchase_user).button_confirm()

    def test_no_need_approval_supplier_purchase_user(self):
        self.order_1.with_user(self.purchase_user).button_confirm()
        self.assertEqual(self.order_1.state, 'purchase')
        self.assertEqual(self.order_1.user_id, self.purchase_user)

    def test_need_approval_supplier_purchase_user(self):
        self.order_2.user_id = self.purchase_manager
        self.order_2.with_user(self.purchase_user).button_confirm()
        self.assertEqual(self.order_2.state, 'to approve')

    def test_no_need_approval_supplier_purchase_manager(self):
        self.order_1.with_user(self.purchase_manager).button_confirm()
        self.assertEqual(self.order_1.state, 'purchase')
        self.assertEqual(self.order_1.user_id, self.purchase_manager)

    def test_need_approval_supplier_purchase_manager(self):
        self.order_2.with_user(self.purchase_manager).button_confirm()
        self.assertEqual(self.order_2.state, 'purchase')
        self.assertEqual(self.order_2.user_id, self.purchase_manager)

