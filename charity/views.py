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

    def donated_amount_max(self):
        return int(math.floor(self.player.participant.vars["carrying_payoff"]) * 0.4)

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
            'earnings': "{0:.2f}".format(self.player.participant.vars["carrying_payoff"]),
            'max_donation': "{0:.2f}".format((self.player.participant.vars["carrying_payoff"] * 0.4))
        }


class ResultsWaitPage(WaitPage):
    body_text = "Please wait."

    def after_all_players_arrive(self):
        self.group.set_payoff()


class Results(Page):
    def vars_for_template(self):
        return {
            'donated': self.player.donated_amount,
        }


class Wait(WaitPage):
    body_text = "Please wait."

    wait_for_all_groups = True

page_sequence = [
    Donate,
    ResultsWaitPage,
    Results,
    Wait,
]
