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
            p.random_coin_toss_one = random.choice(["Heads", "Tails"])

    def make_random_toss_two(self):
        for p in self.get_players():
            p.random_coin_toss_two = random.choice(["Heads", "Tails"])

    def decision_one_payoff(self):
        points = 0
        for p in self.get_players():
            if p.decision_one == "Coin 1":
                if p.random_coin_toss_one == "Heads":
                    p.payoff = 0
                    points = 0
                else:
                    p.payoff = 820
                    points = 820

            elif p.decision_one == "Coin 2":
                if p.random_coin_toss_one == "Heads":
                    p.payoff = 70
                    points = 70
                else:
                    p.payoff = 350
                    points = 350

            elif p.decision_one == "Coin 3":
                if p.random_coin_toss_one == "Heads":
                    p.payoff = 140
                    points = 140
                else:
                    p.payoff = 550
                    points = 550

            elif p.decision_one == "Coin 4":
                if p.random_coin_toss_one == "Heads":
                    p.payoff = 210
                    points = 210
                else:
                    p.payoff = 410
                    points = 410

            elif p.decision_one == "Coin 5":
                if p.random_coin_toss_one == "Heads":
                    p.payoff = 240
                    points = 240
                else:
                    p.payoff = 340
                    points = 340

            elif p.decision_one == "Coin 6":
                p.payoff = 275
                points = 275

            elif p.decision_one == "Coin 7":
                if p.random_coin_toss_one == "Heads":
                    p.payoff = 310
                    points = 310
                else:
                    p.payoff = 210
                    points = 210

            p.participant.vars["game_payoff"]["risk_game"] = points
            p.participant.vars["carrying_payoff"] += points
            p.risk_games_points = points

    def decision_two_payoff(self):
        points = 0
        for p in self.get_players():
            if p.decision_two == "Coin 1":
                if p.random_coin_toss_two == "Heads":
                    p.payoff = 0
                    points = 0
                else:
                    p.payoff = 620
                    points = 620

            elif p.decision_two == "Coin 2":
                if p.random_coin_toss_two == "Heads":
                    p.payoff = 70
                    points = 70
                else:
                    p.payoff = 550
                    points = 550

            elif p.decision_two == "Coin 3":
                if p.random_coin_toss_two == "Heads":
                    p.payoff = 140
                    points = 140
                else:
                    p.payoff = 480
                    points = 480

            elif p.decision_two == "Coin 4":
                if p.random_coin_toss_two == "Heads":
                    p.payoff = 210
                    points = 210
                else:
                    p.payoff = 410
                    points = 410

            elif p.decision_two == "Coin 5":
                if p.random_coin_toss_two == "Heads":
                    p.payoff = 275
                    points = 275
                else:
                    p.payoff = 340
                    points = 340

            elif p.decision_two == "Coin 6":
                p.payoff = 310
                points = 310

            elif p.decision_two == "Coin 7":
                if p.random_coin_toss_two == "Heads":
                    p.payoff = 340
                    points = 340
                else:
                    p.payoff = 275
                    points = 275

            p.participant.vars["game_payoff"]["risk_game"] += points
            p.participant.vars["carrying_payoff"] += points
            p.risk_games_points = points


class Player(BasePlayer):
    CHOICE_ONE = (
        ("Coin 1", "Coin 1: KSH 0 if heads and KSH 820 if tails"),
        ("Coin 2", "Coin 2: KSH 70  if heads and KSH 350 if tails"),
        ("Coin 3", "Coin 3: KSH 140 if heads and KSH 550 if tails"),
        ("Coin 4", "Coin 4: KSH 210 if heads and KSH 410 if tails"),
        ("Coin 5", "Coin 5: KSH 240 if heads and KSH 340 if tails"),
        ("Coin 6", "Coin 6: KSH 275 if heads and KSH 275 if tails"),
        ("Coin 7", "Coin 6: KSH 310 if heads and KSH 210 if tails"),
    )

    CHOICE_TWO = (
        ("Coin 1", "Coin 1: KSH 0 if heads and KSH 620 if tails"),
        ("Coin 2", "Coin 2: KSH 70 if heads and KSH 550 if tails"),
        ("Coin 3", "Coin 3: KSH 140  if heads and KSH 480 if tails"),
        ("Coin 4", "Coin 4: KSH 210 if heads and KSH 410 if tails"),
        ("Coin 5", "Coin 5: KSH 275 if heads and KSH 340 if tails"),
        ("Coin 6", "Coin 6: KSH 310 if heads and KSH 310 if tails"),
        ("Coin 7", "Coin 7: KSH 340 if heads and KSH 275 if tails"),
    )

    decision_one = models.CharField(choices=CHOICE_ONE, widget=widgets.RadioSelect())
    random_coin_toss_one = models.CharField()

    decision_two = models.CharField(choices=CHOICE_TWO, widget=widgets.RadioSelect())
    random_coin_toss_two = models.CharField()
    risk_games_points = models.IntegerField()
