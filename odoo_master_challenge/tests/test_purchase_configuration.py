# Copyright 2023 Etech
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests.common import SingleTransactionCase


class PurchaseConfiguration(SingleTransactionCase):

    def test_po_double_validation_company_configuration(self):
        self.assertEqual(self.env.ref('base.main_company').po_double_validation, 'two_step')

    def test_po_double_validation_amount_company_configuration(self):
        self.assertEqual(self.env.ref('base.main_company').po_double_validation_amount, 2500)
