# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class /odoo12/odoo-dev/addons/open-addons/odoo-tycoon(models.Model):
#     _name = '/odoo12/odoo-dev/addons/open-addons/odoo-tycoon./odoo12/odoo-dev/addons/open-addons/odoo-tycoon'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100