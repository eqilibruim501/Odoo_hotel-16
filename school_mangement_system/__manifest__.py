# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'School System',
    'version': '1.2',
    'summary': 'School management system',
    'description': """
    School information
            """,
    'depends': ['base_setup'],
    'data': [
        'security/ir.model.access.csv',
        'views/School_views.xml',
    ],

}
