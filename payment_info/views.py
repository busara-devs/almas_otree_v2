# -*- coding: utf-8 -*-
from __future__ import division
from ._builtin import Page, WaitPage
import math


class WaitForAll(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.payoff = p.participant.vars["carrying_payoff"]
            p.total_payoff = p.participant.vars["carrying_payoff"]


class PaymentInfo(Page):
    def vars_for_template(self):
        participant = self.player.participant
        return {
            'redemption_code': participant.label or participant.code,
            'payoff': math.ceil(participant.vars["carrying_payoff"]),
            'vouchers': participant.vars["vouchers"]
        }


page_sequence = [WaitForAll, PaymentInfo]
