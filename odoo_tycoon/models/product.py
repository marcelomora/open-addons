# -*- coding: utf-8 -*-
# Copyright 2020 Accioma (https://www.accioma.com).
# @author Marcelo Mora <marcelo.mora@accioma.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_tycoon = fields.Boolean("Is Tycoon")

