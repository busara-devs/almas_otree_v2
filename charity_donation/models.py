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
In this game we want to measure how a person's willingness to donate part of their
earnings to charity varies with geographic location of the charity, which in turn is strongly
correlated with linguistic and ethnic group of the likely beneficiaries.
"""


class Constants(BaseConstants):
    name_in_url = 'charity_donation'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    donated_amount = models.CurrencyField(choices=range(0,250+1,50))
