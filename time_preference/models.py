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
This game will serve two purposes. First, it enables us to identify patience, and the effect
of temperature on patience. Second, it enables us to identify time inconsistency. We
will use the traditional protocol for eliciting so-called beta-delta preferences, namely
a price list with ditterent choices about timing of payments.
"""


class Constants(BaseConstants):
    name_in_url = 'time_preference'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for p in self.get_players():
            p.participant.vars["chosen_future"] = list()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def set_choices(self):
        choices = []
        menu_a = ["menu_a_q1", "menu_a_q2", "menu_a_q3", "menu_a_q4", "menu_a_q5", "menu_a_q6"]
        menu_b = ["menu_b_q1", "menu_b_q2", "menu_b_q3", "menu_b_q4", "menu_b_q5", "menu_b_q6"]
        menu_c = ["menu_c_q1", "menu_c_q2", "menu_c_q3", "menu_c_q4", "menu_c_q5", "menu_c_q6"]
        menu_d = ["menu_d_q1", "menu_d_q2", "menu_d_q3", "menu_d_q4", "menu_d_q5", "menu_d_q6"]

        choice_a = random.choice(menu_a)
        choice_b = random.choice(menu_b)
        choice_c = random.choice(menu_c)
        choice_d = random.choice(menu_d)

        choices.append(choice_a)
        choices.append(choice_b)
        choices.append(choice_c)
        choices.append(choice_d)

        return choices

    def select_payoff(self):
        points = 0
        for choice in self.set_choices():
            menu_option = getattr(self, str(choice))
            if "now" in menu_option:
                now_option = int(str(menu_option).split("_")[0])
                points += now_option
                # self.participant.vars["game_payoff"]["time_preference"] = now_option
            else:
                points = 0
                self.participant.vars["chosen_future"].append(menu_option)
        self.payoff = points
        self.participant.vars["carrying_payoff"] = points
        self.participant.vars["game_payoff"]["time_preference"] = points
        self.time_preference_points = points

    q1_a = (('240_now', 'A: KSH 240'), ('0_future', 'B: KSH 0'),)
    q2_a = (('192_now', 'A: ksh 192 '), ('70_future', 'B: KSH 70'),)
    q3_a = (('144_now', 'A: KSH 144 '), ('140_future', 'B: KSH 140'),)
    q4_a = (('96_now', 'A: KSH 96 '), ('210_future', 'B: KSH 210'),)
    q5_a = (('48_now', 'A: KSH 48 '), ('275_future', 'B: KSH 275'),)
    q6_a = (('0_now', 'A: ksh 0'), ('340_future', 'B: KSH 340'),)

    q1_b = (('290_now', 'A: KSH 290'), ('0_future', 'B: KSH 0'),)
    q2_b = (('250_now', 'A: KSH 250'), ('53_future', 'B: KSH 53'),)
    q3_b = (('180_now', 'A: KSH 180'), ('110_future', 'B: KSH 110'),)
    q4_b = (('120_now', 'A: KSH 120'), ('170_future', 'B: KSH 170'),)
    q5_b = (('64_now', 'A: KSH 64'), ('230_future', 'B: KSH 230'),)
    q6_b = (('0_now', 'A: KSH 0'), ('290_future', 'B: KSH 290'),)

    q1_c = (('240_now', 'A: KSH 240'), ('0_future', 'B: KSH 0'),)
    q2_c = (('192_now', 'A: KSH 192'), ('70_future', 'B: KSH 70'),)
    q3_c = (('144_now', 'A: KSH 144 '), ('140_future', 'B: KSH 140'),)
    q4_c = (('96_now', 'A: KSH 96'), ('210_future', 'B: KSH 210'),)
    q5_c = (('48_now', 'A: KSH 48 '), ('960_future', 'B: KSH 275'),)
    q6_c = (('0_now', 'A: KSH 0'), ('1200_future', 'B: KSH 340'),)

    q1_d = (('290_now', 'A: KSH 290'), ('0_future', 'B: KSH 0'),)
    q2_d = (('240_now', 'A: KSH 240'), ('50_future', 'B: KSH 50'),)
    q3_d = (('180_now', 'A: KSH 180'), ('110_future', 'B: KSH 110'),)
    q4_d = (('120_now', 'A: kSH 120'), ('170_future', 'B: KSH 170'),)
    q5_d = (('64_now', 'A: KSH 64 '), ('230_future', 'B: KSH 230'),)
    q6_d = (('0_now', 'A: KSH 0'), ('290_future', 'B: KSH 290'),)

    menu_a_q1 = models.CharField(choices=q1_a, verbose_name="", widget=widgets.RadioSelect())
    menu_a_q2 = models.CharField(choices=q2_a, verbose_name="", widget=widgets.RadioSelect())
    menu_a_q3 = models.CharField(choices=q3_a, verbose_name="", widget=widgets.RadioSelect())
    menu_a_q4 = models.CharField(choices=q4_a, verbose_name="", widget=widgets.RadioSelect())
    menu_a_q5 = models.CharField(choices=q5_a, verbose_name="", widget=widgets.RadioSelect())
    menu_a_q6 = models.CharField(choices=q6_a, verbose_name="", widget=widgets.RadioSelect())

    menu_b_q1 = models.CharField(choices=q1_b, verbose_name="", widget=widgets.RadioSelect())
    menu_b_q2 = models.CharField(choices=q2_b, verbose_name="", widget=widgets.RadioSelect())
    menu_b_q3 = models.CharField(choices=q3_b, verbose_name="", widget=widgets.RadioSelect())
    menu_b_q4 = models.CharField(choices=q4_b, verbose_name="", widget=widgets.RadioSelect())
    menu_b_q5 = models.CharField(choices=q5_b, verbose_name="", widget=widgets.RadioSelect())
    menu_b_q6 = models.CharField(choices=q6_b, verbose_name="", widget=widgets.RadioSelect())

    menu_c_q1 = models.CharField(choices=q1_c, verbose_name="", widget=widgets.RadioSelect())
    menu_c_q2 = models.CharField(choices=q2_c, verbose_name="", widget=widgets.RadioSelect())
    menu_c_q3 = models.CharField(choices=q3_c, verbose_name="", widget=widgets.RadioSelect())
    menu_c_q4 = models.CharField(choices=q4_c, verbose_name="", widget=widgets.RadioSelect())
    menu_c_q5 = models.CharField(choices=q5_c, verbose_name="", widget=widgets.RadioSelect())
    menu_c_q6 = models.CharField(choices=q6_c, verbose_name="", widget=widgets.RadioSelect())

    menu_d_q1 = models.CharField(choices=q1_d, verbose_name="", widget=widgets.RadioSelect())
    menu_d_q2 = models.CharField(choices=q2_d, verbose_name="", widget=widgets.RadioSelect())
    menu_d_q3 = models.CharField(choices=q3_d, verbose_name="", widget=widgets.RadioSelect())
    menu_d_q4 = models.CharField(choices=q4_d, verbose_name="", widget=widgets.RadioSelect())
    menu_d_q5 = models.CharField(choices=q5_d, verbose_name="", widget=widgets.RadioSelect())
    menu_d_q6 = models.CharField(choices=q6_d, verbose_name="", widget=widgets.RadioSelect())

    time_preference_points = models.IntegerField(initial=0)
