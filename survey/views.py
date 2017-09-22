# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants


class CognitiveReflectionTest(Page):
    timeout_seconds = 180

    form_model = models.Player
    form_fields = ['c_r_1',
                   'c_r_2',
                   'c_r_4',
                   'c_r_5',
                   'c_r_6']

    def before_next_page(self):
        self.player.set_payoff()


class One(Page):
    form_model = models.Player
    form_fields = ['demo_1_scl']


class One2(Page):
    form_model = models.Player
    form_fields = ['affct1_scl', 'affct2_scl']


class Two(Page):
    form_model = models.Player
    form_fields = ['age', 'height', 'weight', 'gender']


class Three(Page):
    form_model = models.Player
    form_fields = ['ethnicity']

    def is_displayed(self):
        return False


class Four(Page):
    form_model = models.Player
    form_fields = ['cali_residnc']


class Demographics(Page):
    form_model = models.Player
    form_fields = ['father_occ', 'mother_occ', 'income', 'edu_father', 'edu_mother']


page_sequence = [
    CognitiveReflectionTest,
    One,
    One2,
    Two,
    Three,
    Four,
    Demographics,
]
