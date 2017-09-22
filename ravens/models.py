# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.db import models
from otree import widgets
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Benson'

doc = """
Raven's matrices to measure cognitive ability.
"""


class Constants(BaseConstants):
    name_in_url = 'ravens'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for p in self.get_players():
            p.participant.vars["ravens_points"] = 0


class Group(BaseGroup):

    def set_payoffs(self):
        for p in self.get_players():
            if p.raven_1 == "four":
                p.points += 1
            if p.raven_2 == "six":
                p.points += 1
            if p.raven_3 == "one":
                p.points += 1
            if p.raven_4 == "three":
                p.points += 1
            if p.raven_5 == "four":
                p.points += 1
            if p.raven_6 == "six":
                p.points += 1
            p.correct_ravens = p.points
            p.participant.vars["ravens_points"] = p.points


class Player(BasePlayer):
    points = models.IntegerField(default=0)

    CHOICES = [("one", ""), ("two", ""), ("three", ""), ("four", ""), ("five", ""), ("six", "")]
    CHOICES_8 = [("one", ""), ("two", ""), ("three", ""), ("four", ""),
                 ("five", ""), ("six", ""), ("seven", ""), ("eight", "")]

    p_1 = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=CHOICES_8)
    p_2 = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=CHOICES)
    raven_1 = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=CHOICES)
    raven_2 = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=CHOICES_8)
    raven_3 = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=CHOICES)
    raven_4 = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=CHOICES)
    raven_5 = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=CHOICES_8)
    raven_6 = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=CHOICES_8)

    correct_ravens = models.IntegerField(initial=0)
