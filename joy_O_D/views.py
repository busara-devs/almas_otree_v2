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
    form_fields = ["p_destroy"]

    def p_destroy_max(self):
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
        player_y.vouchers = player_y.vouchers - self.player.p_destroy
        self.player.pc_destroyed_points()
        self.player.set_vouchers()


class Destroyed(Page):
    def vars_for_template(self):
        py = self.player.get_others_in_group()[0]
        total_destroyed = py.p_destroy + self.player.pc_destroyed
        return {
            "destroyed": total_destroyed
        }


class ResultsWaitPage(WaitPage):
    body_text = "Please wait."

    def after_all_players_arrive(self):
        for player in self.group.get_players():
            player.participant.vars["vouchers"] = player.vouchers
            # save what the other player destroyed.
            player.o_destroy = player.get_others_in_group()[0].p_destroy


class Wait(WaitPage):
    body_text = "Please wait."

    wait_for_all_groups = True


page_sequence = [
    Introduction,
    Wait,
    Destroy,
    ResultsWaitPage,
    Wait,
]
