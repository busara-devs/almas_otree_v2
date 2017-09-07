# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random
import math


class Donate(Page):
    form_model = models.Player
    form_fields = ['donated_amount']

    def donated_amount_error_message(self, value):
        if math.floor(self.player.participant.vars["carrying_payoff"]) * 0.4 <= value:
            return 'Amount to donate should be less than or equal to what you have!'

    def vars_for_template(self):
        charities = ["Kiambu Orphans Initiative",
                     "Kanyawegi childrens home",
                     "Destined Childrens Home Kikuyu",
                     "Kakamega Orphans Care Centre",
                     "Upendo Childrens Centre Nyeri",
                     "Huruma Childrens Home Ngong",
                     "Baraka Childrens Home Mombasa"]

        charity = random.choice(charities)
        self.player.charity_allocated = charity
        return {
            'charity': charity,
            'max_donation': math.floor(self.player.participant.vars["carrying_payoff"] * 0.4)
        }


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()


class Results(Page):
    def vars_for_template(self):
        return {
            'donated': self.player.donated_amount,
        }


page_sequence = [
    Donate,
    ResultsWaitPage,
    Results
]
