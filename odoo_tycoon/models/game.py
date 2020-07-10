# -*- coding: utf-8 -*-
# Copyright 2020 Accioma (https://www.accioma.com).
# @author Marcelo Mora <marcelo.mora@accioma.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api
#TODO: Import and implement translations
from odoo.exceptions import Warning

class TycoonGame(models.Model):
    """Tycoon Game List"""
    _name = "tycoon.game"

    name = fields.Char("Name", required=True)
    winner_id = fields.Many2one(
        'res.users',
        'Winner')
    date_start = fields.Datetime('Date Start', help='Start date of game')
    date_end = fields.Datetime('Date End', help='End date of game')
    manager_id = fields.Many2one(
        'res.users',
        'Manager')
    player_ids = fields.Many2many(
        comodel_name='res.users',
        string='Players')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('playing', 'Playing'),
        ('done', 'Done'),
        ],
        default='draft'
    )

    @api.multi
    def lets_play(self):
        """Lets play the game"""
        raise Warning("Not implemented method")

    @api.multi
    def end_game(self):
        """End the game"""
        raise Warning("Not implemented method")

