# Copyright 2023 Etech
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Odoo Master Challenge',
    'description': """
        Double purchase validation""",
    'version': '16',
    'license': 'AGPL-3',
    'author': 'Etech',
    'website': 'https://www.etechconsulting-mg.com',
    'depends': [
        "purchase"
    ],
    'data': [
        'views/res_partner_views.xml',
        'views/purchase_order_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'odoo_master_challenge/static/src/js/purchase_order_list_view.js',
            'odoo_master_challenge/static/src/xml/purchase_approve_all.xml',
        ],
    }
}
