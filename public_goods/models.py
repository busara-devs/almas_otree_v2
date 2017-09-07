# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree import widgets
from otree.common import Currency as c, currency_range
import random

# </standard imports>

doc = """
This is a one-period public goods game with 3 players. Assignment to groups is random.

"""


class Constants(BaseConstants):
    name_in_url = 'public_goods'
    players_per_group = 3
    num_rounds = 1

    """Amount allocated to each player"""
    endowment = 340
    efficiency_factor = 2

    #  for guessing correctly
    guess_correct = 50

    GUESS_CHOICE = {
        1: [0],
        2: [list(range(1, 71))],
        3: [list(range(71, 141))],
        4: [list(range(141, 211))],
        5: [list(range(211, 276))],
        6: [list(range(276, 344))],
        7: [345],
    }

    GUESS_CHOICES = [
        ("1", "KSH 0"),
        ("2", "KSH 1 - KSH 70"),
        ("3", "KSH 71 - KSH 140"),
        ("4", "KSH 141 - KSH 210"),
        ("5", "KSH 211 - KSH 275"),
        ("6", "KSH 276 - KSH 344"),
        ("7", "KSH 345"),
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.IntegerField()

    individual_share = models.IntegerField()

    def set_payoffs(self):

        self.total_contribution = sum([p.contribution for p in self.get_players()])
        self.individual_share = self.total_contribution * Constants.efficiency_factor / Constants.players_per_group
        for p in self.get_players():
            if p.guess_correct():
                points = (Constants.endowment - p.contribution) + self.individual_share + Constants.guess_correct
                p.participant.vars["game_payoff"]["public_goods_game"] = points
                p.participant.vars["carrying_payoff"] += points
                p.payoff = points
                p.public_goods_game = points
            else:
                points = (Constants.endowment - p.contribution) + self.individual_share
                p.participant.vars["game_payoff"]["public_goods_game"] = points
                p.participant.vars["carrying_payoff"] += points
                p.payoff = points
                p.public_goods_game = points


class Player(BasePlayer):
    contribution = models.IntegerField(
        min=0, max=Constants.endowment,
        doc="""The amount contributed by the player""",
    )
    question = models.IntegerField()

    guess_one = models.CharField(widget=widgets.RadioSelect(), choices=Constants.GUESS_CHOICES)
    guess_two = models.CharField(widget=widgets.RadioSelect(), choices=Constants.GUESS_CHOICES)
    public_goods_game = models.IntegerField(initial=0)

    def guess_correct(self):
        guess_choices = Constants.GUESS_CHOICE
        px, py = self.get_others_in_group()
        return px.contribution in guess_choices[int(self.guess_one)] and py.contribution in guess_choices[
            int(self.guess_two)]
