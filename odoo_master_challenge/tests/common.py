# Copyright 2023 Etech
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class PurchaseOrderCommon(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        context = dict(cls.env.context, no_reset_password=True)
        cls.env = cls.env(context=context)
        cls.purchase_manager = cls.env["res.users"].create({
            "name": "Purchase Manager",
            "login": "purchase_manager",
            "email": "purchase_manager@example.com",
            "groups_id": [(4, cls.env.ref('purchase.group_purchase_manager').id)]
        })
        cls.purchase_user = cls.env["res.users"].create({
            "name": "Purchase User",
            "login": "purchase_user",
            "email": "purchase_user@example.com",
            "groups_id": [(3, cls.env.ref('purchase.group_purchase_manager').id),
                          (4, cls.env.ref('purchase.group_purchase_user').id)]
        })
        cls.no_need_approval_supplier = cls.env['res.partner'].create({
            "name": "Super Supplier",
            "no_need_approval": True
        })
        cls.need_approval_supplier = cls.env['res.partner'].create({
            "name": "Super Supplier",
            "no_need_approval": False
        })
        cls.product_1 = cls.env['product.product'].create({
            'name': 'Product 1',
        })
