# -*- coding: utf-8 -*-
# Copyright 2020 Accioma (https://www.accioma.com).
# @author Marcelo Mora <marcelo.mora@accioma.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api
from odoo.exceptions import Warning

class GameMove(models.Model):
    _name = 'game.move'
    _description = 'Game Move'

    @api.multi
    def name_get(self):
        """
        Custom name for game and player
        """
        res = []
        for r in self:
            res.append(
            (r.id,
             "{}:  {}".format(r.game_id.name, r.player_id.name)))
            return res

    game_id = fields.Many2one(
        'tycoon.game',
        'Game')

    player_id = fields.Many2one(
        'res.users',
        'Player')

    cash_total = fields.Float("Cash Total")
    cash_remaining = fields.Float("Cash Remaining")
    amount_total = fields.Float("Amount Total")
    game_line_ids = fields.One2many(
        'game.move.line',
        'game_id',
        'Game Line')

    @api.multi
    def submit_move(self):
        raise Warning("Method not implemented")

class GameMoveLine(models.Model):
    _name = 'game.move.line'
    _description = 'Game Move Line'

    game_id = fields.Many2one(
        'game.move',
        'Game')

    product_id = fields.Many2one(
        'product.product',
        'Product')

    price_unit = fields.Float("Price Unit")
    qty = fields.Float("Qty")
    price_total = fields.Float("Price Total", compute="_compute_totals", store=True )

    @api.onchange('product_id')
    def on_change_product(self):
        self.price_unit = self.product_id.lst_price

    @api.depends('price_unit', 'qty')
    def _compute_totals(self):
        for r in self:
            r.price_total = r.price_unit * r.qty
