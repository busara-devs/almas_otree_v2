# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants


class CognitiveReflectionTest(Page):
    timeout_seconds = 180

    form_model = models.Player
    form_fields = ['cognitive_reflection_one',
                   'cognitive_reflection_two',
                   'cognitive_reflection_four',
                   'cognitive_reflection_five',
                   'cognitive_reflection_six']

    def before_next_page(self):
        self.player.set_payoff()


class One(Page):
    form_model = models.Player
    form_fields = ['demographic_one_scale']


class One2(Page):
    form_model = models.Player
    form_fields = ['affect1_scale', 'affect2_scale']


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
    form_fields = ['california_residency']


class Demographics(Page):
    form_model = models.Player
    form_fields = ['father_occupation', 'mother_occupation', 'income', 'education_father', 'education_mother']


page_sequence = [
    CognitiveReflectionTest,
    One,
    One2,
    Two,
    Three,
    Four,
    Demographics,
]
