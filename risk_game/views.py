# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class ScreenOne(Page):
    pass


class DecideOne(Page):
    form_model = models.Player
    form_fields = ['decision_one']

    def before_next_page(self):
        self.group.make_random_toss_one()


class ScreenTwo(Page):
    pass


class DecideTwo(Page):
    form_model = models.Player
    form_fields = ['decision_two']

    def before_next_page(self):
        self.group.make_random_toss_two()


class ResultsWaitPage(WaitPage):
    body_text = "Please wait."

    def after_all_players_arrive(self):
        self.group.set_payoff()


class Wait(WaitPage):
    body_text = "Please wait."

    wait_for_all_groups = True


page_sequence = [
    ScreenOne,
    DecideOne,
    ScreenTwo,
    DecideTwo,
    ResultsWaitPage,
    Wait,
]
