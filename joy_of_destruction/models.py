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

author = 'Your name here'

doc = """
Two participants are paired and both completed the Raven's matrices
and earned some airtime vouchers. They are given opportunity to destroy some of
your partner's vouchers. This will happen anonymously, so that your choices will never be
revealed to any other participant.
"""


class Constants(BaseConstants):
    name_in_url = 'joy_of_destruction'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):

    def computer_destroyed_points(self):
        choice = random.choice([0,1])
        if choice == 1:
            # heads nothing
            self.coin_toss = "Heads"
        else:
            # tails all

            other = self.get_others_in_group()[0]
            if self.other_player_destroyed <= other.vouchers:
                other.vouchers -= random.randrange(1, other.vouchers - self.player_destroyed)
                self.coin_toss = "Tails"

    player_destroyed = models.IntegerField(min=0)

    computer_destroyed = models.IntegerField(default=0)

    vouchers = models.IntegerField(default=0)

    coin_toss = models.CharField()

