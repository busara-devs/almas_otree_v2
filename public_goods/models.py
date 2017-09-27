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
    endowment = 1200
    efficiency_factor = 2

    # tokens for guessing correctly
    guess_value = 175

    GUESS_CHOICE = {
        "1": [0],
        "2": list(range(1, 241)),
        "3": list(range(241, 481)),
        "4": list(range(481, 721)),
        "5": list(range(721, 961)),
        "6": list(range(961, 1200)),
        "7": [1200],
    }

    GUESS_CHOICES = [
        ("1", "0 tokens"),
        ("2", "1 - 240 tokens"),
        ("3", "241 - 480 tokens"),
        ("4", "481 - 720 tokens"),
        ("5", "721 - 960 tokens"),
        ("6", "961 - 1199 tokens"),
        ("7", "1200 tokens"),
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
                p.guess_points = Constants.guess_value
                points = (Constants.endowment - p.contribution) + self.individual_share + Constants.guess_value
                p.participant.vars["game_payoff"]["p_g_points"] = points
                p.participant.vars["carrying_payoff"] += points
                p.payoff = points
                p.p_g_points = points
            else:
                points = (Constants.endowment - p.contribution) + self.individual_share
                p.participant.vars["game_payoff"]["p_g_points"] = points
                p.participant.vars["carrying_payoff"] += points
                p.payoff = points
                p.p_g_points = points


class Player(BasePlayer):
    contribution = models.IntegerField(
        min=0, max=Constants.endowment,
        doc="""The amount contributed by the player""",
    )
    question = models.IntegerField()

    guess = models.CharField(widget=widgets.RadioSelect(), choices=Constants.GUESS_CHOICES)
    guess_points = models.IntegerField(initial=0)
    # guess_two = models.CharField(widget=widgets.RadioSelect(), choices=Constants.GUESS_CHOICES)
    p_g_points = models.IntegerField(initial=0)

    def guess_correct(self):
        guess_choices = Constants.GUESS_CHOICE
        px, py = self.get_others_in_group()
        player = random.choice([px, py])
        if self.guess:
            return player.contribution in guess_choices[str(self.guess)]
