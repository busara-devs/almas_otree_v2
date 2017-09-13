# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from builtins import zip
import random


class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True
    body_text = "Please wait."

    def pair_up(self, lst):
        pair = iter(lst)
        return zip(pair, pair)

    def after_all_players_arrive(self):
        # sort players by correct sliders from previous rounds
        sorted_players = sorted(
            self.subsession.get_players(),
            key=lambda player: player.participant.vars['total_correct']
        )
        print("sorted ::", [(p, p.participant.vars['total_correct']) for p in sorted_players])
        if len(sorted_players) > 3:

            pairs = list(self.pair_up(sorted_players))

            median_sort = int(len(pairs) / 2)

            for pair in pairs:
                if pairs.index(pair) > median_sort:
                    print("p1 p2::", pair)
                    for player in pair:
                        player.participant.vars["rank"] = "high"

                elif pairs.index(pair) == median_sort:
                    print("p3 p4::", pair)
                    for player in pair:
                        player.participant.vars["rank"] = random.choice(["high", "low"])

                else:
                    print("p5 p6::", pair)
                    for player in pair:
                        player.participant.vars["rank"] = "low"

        # chunk players into groups
        group_matrix = []
        players_per_group = Constants.players_per_group
        for i in range(0, len(sorted_players), players_per_group):
            group_matrix.append(sorted_players[i: i + players_per_group])
        self.subsession.set_group_matrix(group_matrix)


        # if len(sorted_players) == 3:
        #     pass
        # else:
        #     # assuming 6, 12, 0r 18 players
        #     median_sort = len(sorted_players) / 2
        #
        #     for i in sorted_players:
        #         if sorted_players.index(i) > median_sort:
        #             i.participant.vars["rank"] = "high"
        #         else:
        #             i.participant.vars["rank"] = "low"
        #
        # # chunk players into groups
        # group_matrix = []
        # ppg = Constants.players_per_group
        # for i in range(0, len(sorted_players), ppg):
        #     group_matrix.append(sorted_players[i:i+ppg])
        #
        # # set new groups
        # self.subsession.set_group_matrix(group_matrix)


class Intro(Page):

    def vars_for_template(self):
        participant = self.player.participant
        return {
            'rank': participant.vars["rank"]
        }


class Offer(Page):
    form_model = models.Player
    form_fields = ["keep"]

    def vars_for_template(self):
        participant = self.player.participant
        return {
            'rank': participant.vars["rank"]
        }

    def keep_error_message(self, value):
        if self.player.participant.vars["rank"] == "high":
            high_choices = list(range(0, 2401, 5))
            if value not in high_choices:
                return "Value must be {}".format(list(high_choices))
        elif self.player.participant.vars["rank"] == "low":
            low_choices = list(range(0, 1201, 5))
            if value not in low_choices:
                return "Value must be {}".format(list(low_choices))


class ResultsWaitPage(WaitPage):
    body_text = "Please wait."

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Wait(WaitPage):
    body_text = "Please wait."

    wait_for_all_groups = True

page_sequence = [
    ShuffleWaitPage,
    Intro,
    Offer,
    ResultsWaitPage,
    Wait,
]
