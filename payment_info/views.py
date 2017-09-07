# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants
import random


class PaymentInfo(Page):
    def is_displayed(self):
        game_obj = self.participant.vars["game_payoff"].keys()
        self.player.total_payoff = sum(payoffs(game_obj))
        return True

    def vars_for_template(self):
        participant = self.player.participant
        return {
            'redemption_code': participant.label or participant.code,
            'payoff': self.player.total_payoff,
            'vouchers': participant.vars["vouchers"]
        }


def payoffs(game_obj):
    games = game_obj.keys()
    games = random.sample(games, 3)
    for game in games:
        yield game_obj[game]


page_sequence = [PaymentInfo]
