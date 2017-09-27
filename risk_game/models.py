# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

# </standard imports>

author = 'Benson'

doc = """
In this Game, six different coins with different amounts for heads and tails.
Subjects can choose which coin they want to ip and then get the money that's associated with either heads or tails.
"""


class Constants(BaseConstants):
    name_in_url = 'risk_game'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def make_random_toss_one(self):
        for p in self.get_players():
            p.rand_toss_1 = random.choice(["Heads", "Tails"])

    def make_random_toss_two(self):
        for p in self.get_players():
            p.rand_toss_2 = random.choice(["Heads", "Tails"])

    def menu_a_points(self):
        for p in self.get_players():
            if p.decision_1 == "Coin 1":
                if p.rand_toss_1 == "Heads":
                    p.coin_1 = 0
                else:
                    p.coin_1 = 2880

            elif p.decision_1 == "Coin 2":
                if p.rand_toss_1 == "Heads":
                    p.coin_1 = 240
                else:
                    p.coin_1 = 2400

            elif p.decision_1 == "Coin 3":
                if p.rand_toss_1 == "Heads":
                    p.coin_1 = 480
                else:
                    p.coin_1 = 1920

            elif p.decision_1 == "Coin 4":
                if p.rand_toss_1 == "Heads":
                    p.coin_1 = 720
                else:
                    p.coin_1 = 1440

            elif p.decision_1 == "Coin 5":
                if p.rand_toss_1 == "Heads":
                    p.coin_1 = 840
                else:
                    p.coin_1 = 1200

            elif p.decision_1 == "Coin 6":
                p.coin_1 = 960

            elif p.decision_1 == "Coin 7":
                if p.rand_toss_1 == "Heads":
                    p.coin_1 = 1080

                else:
                    p.coin_1 = 720

    def menu_b_points(self):
        for p in self.get_players():
            if p.decision_2 == "Coin 1":
                if p.rand_toss_2 == "Heads":
                    p.coin_2 = 0
                else:
                    p.coin_2 = 2160

            elif p.decision_2 == "Coin 2":
                if p.rand_toss_2 == "Heads":
                    p.coin_2 = 240
                else:
                    p.coin_2 = 1920

            elif p.decision_2 == "Coin 3":
                if p.rand_toss_2 == "Heads":
                    p.coin_2 = 480
                else:
                    p.coin_2 = 1680

            elif p.decision_2 == "Coin 4":
                if p.rand_toss_2 == "Heads":
                    p.coin_2 = 720
                else:
                    p.coin_2 = 1440

            elif p.decision_2 == "Coin 5":
                if p.rand_toss_2 == "Heads":
                    p.coin_2 = 960
                else:
                    p.coin_2 = 1200

            elif p.decision_2 == "Coin 6":
                p.coin_2 = 1080

            elif p.decision_2 == "Coin 7":
                if p.rand_toss_2 == "Heads":
                    p.coin_2 = 1200
                else:
                    p.coin_2 = 960

    def set_payoff(self):
        self.menu_a_points()
        self.menu_b_points()

        for p in self.get_players():
            if p.coin_1 and p.coin_2:
                p.participant.vars["game_payoff"]["risk_game"] = p.coin_1 + p.coin_2
                p.participant.vars["carrying_payoff"] += p.coin_1 + p.coin_2
                p.risk_points = p.coin_1 + p.coin_2
                p.payoff = p.coin_1 + p.coin_2


class Player(BasePlayer):
    CHOICE_ONE = (
        ("Coin 1", "Coin 1: 0 tokens if heads and 2880 tokens if tails"),
        ("Coin 2", "Coin 2: 240 tokens if heads and 2400 tokens if tails"),
        ("Coin 3", "Coin 3: 480 tokens if heads and 1920 tokens if tails"),
        ("Coin 4", "Coin 4: 720 tokens if heads and 1440 tokens if tails"),
        ("Coin 5", "Coin 5: 840 tokens if heads and 1200 tokens if tails"),
        ("Coin 6", "Coin 6: 960 tokens if heads and 960 tokens if tails"),
        ("Coin 7", "Coin 7: 1080 tokens if heads and 720 tokens if tails"),
    )

    CHOICE_TWO = (
        ("Coin 1", "Coin 1: 0 tokens if heads and 2160 tokens if tails"),
        ("Coin 2", "Coin 2: 240 tokens if heads and 1920 tokens if tails"),
        ("Coin 3", "Coin 3: 480 tokens if heads and 1680 tokens if tails"),
        ("Coin 4", "Coin 4: 720 tokens if heads and 1440 tokens if tails"),
        ("Coin 5", "Coin 5: 960 tokens if heads and 1200 tokens if tails"),
        ("Coin 6", "Coin 6: 1080 tokens if heads and 1080 tokens if tails"),
        ("Coin 7", "Coin 7: 1200 tokens if heads and 960 tokens if tails"),
    )

    decision_1 = models.CharField(choices=CHOICE_ONE, widget=widgets.RadioSelect())
    rand_toss_1 = models.CharField()
    coin_1 = models.IntegerField()
    coin_2 = models.IntegerField()
    decision_2 = models.CharField(choices=CHOICE_TWO, widget=widgets.RadioSelect())
    rand_toss_2 = models.CharField()
    risk_points = models.IntegerField()
