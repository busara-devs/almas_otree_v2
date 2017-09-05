# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):

    def before_next_page(self):
        self.player.vouchers = self.participant.vars["ravens_points"]


class Destroy(Page):
    form_model = models.Player
    form_fields = ["other_player_destroyed"]

    def player_destroyed_max(self):
        # 0 - 2/2 = 1
        other_players_points = self.player.get_others_in_group()[0].participant.vars["ravens_points"]
        if other_players_points >= 2:
            return other_players_points/2
        else:
            return 0

    def vars_for_template(self):
        py = self.player.get_others_in_group()[0]
        return {
            "raven_points": py.participant.vars["ravens_points"],
        }
    def before_next_page(self):
        player_y = self.player.get_others_in_group()[0]
        player_y.vouchers = player_y.vouchers - player_y.player_destroyed

        self.player.computer_destroyed_points()


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for player in self.group.get_players():
            player.participant.vars["vouchers"] = player.vouchers



page_sequence = [
    Introduction,
    Destroy,
    ResultsWaitPage,
]
