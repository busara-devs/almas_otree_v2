# -*- coding: utf-8 -*-
from __future__ import division

import json
import random

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants



class Introduction(Page):

    def before_next_page(self):
        self.player.vouchers = self.participant.vars["ravens_points"]


class Destroy(Page):
    form_model = models.Player
    form_fields = ["player_destroyed"]

    def player_destroyed_max(self):
        # 0 - 2/2 = 1
        other_players_points = self.player.get_others_in_group()[0].participant.vars["ravens_points"]
        if other_players_points > 0:
            return other_players_points
        else:
            return 0

    def vars_for_template(self):
        py = self.player.get_others_in_group()[0]
        return {
            "raven_points": py.participant.vars["ravens_points"],
        }

    def before_next_page(self):
        player_y = self.player.get_others_in_group()[0]
        player_y.vouchers = player_y.vouchers - self.player.player_destroyed
        self.player.computer_destroyed_points()
        self.player.set_vouchers()


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for player in self.group.get_players():
            player.participant.vars["vouchers"] = player.vouchers

            # get three random game payoffs
            print(player.participant.vars["game_payoff"])
            game_obj = player.participant.vars["game_payoff"]
            player.participant.vars["carrying_payoff"] = sum(payoffs(player, game_obj))


def payoffs(p, game_obj):
    games = game_obj.keys()
    games = random.sample(games, 3)
    p.random_games = json.dumps(games)
    for game in games:
        yield game_obj[game]


page_sequence = [
    Introduction,
    Destroy,
    ResultsWaitPage,
]
