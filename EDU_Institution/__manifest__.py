# -*- coding: utf-8 -*-
{
    'name': 'EDU Institution',
    'version': '11.0.0.2',
    'category': 'Education',
    "sequence": 1,
    'summary': 'Core of Higher Education Management Apps',
    'website': 'https://www.antimattersoft.com/',
    'description': u"""

Written by Joe Shields for 10/11/2018

""",
    'author': 'JOSHIELDS',
    'depends': [
        'account',
        'base',
        'document',
        'product',
        'sale',
        'contacts',
    ],
    'data': [
        'views/building.xml',
        'views/room.xml',
        'menu/menu.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
    'license': 'OPL-1',
}