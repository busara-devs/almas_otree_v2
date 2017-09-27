# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from random import shuffle


class Introduction(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1


class QuestionOne(Page):
    form_model = models.Player
    l1 = ["menu_a"]
    form_fields = l1


class QuestionTwo(Page):
    form_model = models.Player
    l2 = ["menu_b"]
    form_fields = l2


class QuestionThree(Page):
    form_model = models.Player
    l3 = ["menu_c"]
    form_fields = l3


class QuestionFour(Page):
    form_model = models.Player
    l4 = ["menu_d"]
    form_fields = l4


class ResultsWaitPage(WaitPage):
    body_text = "Please wait."

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_preference()
            p.set_payoff()


class Wait(WaitPage):
    body_text = "Please wait."

    wait_for_all_groups = True

page_sequence = [
    Introduction,
    QuestionOne,
    QuestionTwo,
    QuestionThree,
    QuestionFour,
    ResultsWaitPage,
    Wait
]
