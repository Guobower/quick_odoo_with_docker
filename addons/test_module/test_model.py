# -*- coding: utf-8 -*-

from openerp import models, fields


class TestModel(models.Model):
    _name = 'test.model'
    _description = u'测试模块'
    _order = 'write_date desc'

    key = fields.Char(u'Key', index=True, required=True)
    value = fields.Char(u'Value', index=True, required=True)
    description = fields.Text(u'Description')
