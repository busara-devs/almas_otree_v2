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
    name_in_url = 'joy_O_D'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def pc_destroyed_points(self):
        choice = random.choice([0, 1])
        if choice == 0:
            # heads nothing
            other = self.get_others_in_group()[0]
            other.coin_toss = "Heads"
        else:
            # tails all
            other = self.get_others_in_group()[0]
            if other.vouchers > 1:
                other.pc_destroyed = random.randrange(1, other.vouchers)
                other.coin_toss = "Tails"
            else:
                other.coin_toss = "Tails"

    def set_vouchers(self):
        other = self.get_others_in_group()[0]
        other.vouchers = other.vouchers - other.pc_destroyed

    p_destroy = models.IntegerField(min=0)

    o_destroyed = models.IntegerField(min=0)

    pc_destroyed = models.IntegerField(default=0)

    vouchers = models.IntegerField(default=0)

    coin_toss = models.CharField()
