# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants
import math


class Wait(WaitPage):
    body_text = "Please wait."

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.payoff_points = p.participant.vars["carrying_payoff"]
            p.payoff_currency = c(p.participant.vars["carrying_payoff"]).to_real_world_currency(self.session)


class PaymentInfo(Page):

    def vars_for_template(self):
        participant = self.player.participant
        menu_a_b_today = participant.vars.get("menu_a_b_today", None)
        menu_a_b_3weeks = participant.vars.get("menu_a_b_3weeks", None)
        menu_c_d_3weeks = participant.vars.get("menu_c_d_3weeks", None)
        menu_c_d_7weeks = participant.vars.get("menu_c_d_7weeks", None),

        if menu_a_b_3weeks and menu_a_b_today:
            return {
                'redemption_code': participant.label or participant.code,
                'payoff': "{0:.2f}".format(participant.vars.get("carrying_payoff", None)),
                'payoff_usd': c(participant.vars.get("carrying_payoff", None)).to_real_world_currency(self.session),
                'vouchers': participant.vars.get("vouchers", None),
                'airtime_worth': 1 * participant.vars.get("vouchers", None),

                'menu_a_b_today': float("{0:.2f}".format(participant.vars.get("menu_a_b_today", None)["today"])),
                'menu_a_b_today_usd': c(participant.vars.get("menu_a_b_today", None)["today"]).to_real_world_currency(self.session),

                'menu_a_b_3weeks': float("{0:.2f}".format(participant.vars.get("menu_a_b_3weeks", None)["weeks3"])),
                'menu_a_b_3weeks_usd': c(participant.vars.get("menu_a_b_3weeks", None)["weeks3"]).to_real_world_currency(self.session)
            }

        elif menu_c_d_3weeks and menu_c_d_7weeks:
            return {
                'redemption_code': participant.label or participant.code,
                'payoff': "{0:.2f}".format(participant.vars.get("carrying_payoff", None)),
                'payoff_usd': c(participant.vars.get("carrying_payoff", None)).to_real_world_currency(self.session),
                'vouchers': participant.vars.get("vouchers", None),
                'airtime_worth': 1 * participant.vars.get("vouchers", None),

                'menu_c_d_3weeks': float("{0:.2f}".format(participant.vars.get("menu_c_d_3weeks", None)["weeks3"])),
                'menu_c_d_3weeks_usd': c(participant.vars.get("menu_c_d_3weeks", None)["weeks3"]).to_real_world_currency(self.session),

                'menu_c_d_7weeks': float("{0:.2f}".format(participant.vars.get("menu_c_d_7weeks", None)["weeks7"])),
                'menu_c_d_7weeks_usd': c(participant.vars.get("menu_c_d_7weeks", None)["weeks7"]).to_real_world_currency(self.session)
            }
        else:
            return {
                'redemption_code': participant.label or participant.code,
                'payoff': "{0:.2f}".format(participant.vars.get("carrying_payoff", None)),
                'payoff_usd': c(participant.vars.get("carrying_payoff", None)).to_real_world_currency(self.session),
                'vouchers': participant.vars.get("vouchers", None),
                'airtime_worth': 1 * participant.vars.get("vouchers", None),
            }


page_sequence = [Wait, PaymentInfo]
