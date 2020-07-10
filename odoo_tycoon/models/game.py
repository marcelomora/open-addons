# -*- coding: utf-8 -*-
# Copyright 2020 Accioma (https://www.accioma.com).
# @author Marcelo Mora <marcelo.mora@accioma.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api

class TycoonGame(models.Model):
    """Tycoon Game List"""
    _name = "tycoon.game"

    name = fields.Char("Name")
    date_start = fields.Datetime('Date Start', help='Start date of game')
