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
    def after_all_players_arrive(self):
        self.group.decision_one_payoff()
        self.group.decision_two_payoff()


page_sequence = [
    ScreenOne,
    DecideOne,
    ScreenTwo,
    DecideTwo,
    ResultsWaitPage,
]
