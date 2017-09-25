# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree import widgets
from otree.common import Currency as c, currency_range
import random
# </standard imports>


doc = """
In the trust game, the participants are matched in pairs where
one of them, participant A, is given a fixed amount of money, say X KSH and the other,
participant B, is not given any money. Participant A can decide to keep the money, in
which case player A will receive the actual payment of X KSH and player B will receive
nothing. Participant A can also decide to send part or all of the money, Y <= X to
player B in which case player B will receive 3Y KSH. In this case player B is given the
option to send money back to player A (any amount he or she likes). If participant A
trusts that some money will be sent back, he or she will benefit from sending the money
to participant B. If, on the other hand, the trust is lower, participant A may decide
to keep the money. Hence, the amount sent from A measures the level of trust of the
participants. The amount sent back from B, reveals the trustworthiness which is also an
interesting measure to study in itself.
"""


class Constants(BaseConstants):
    name_in_url = 'trust'
    players_per_group = 2
    num_rounds = 1

    # Initial amount allocated to each player
    amount_allocated = 600
    multiplication_factor = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_payoffs(self):
        for p in self.get_players():
            points = int(Constants.amount_allocated) - int(p.sent_amount) + \
                     int(p.get_others_in_group()[0].sent_back_amount) + \
                     int(p.remaining_amount)
            #p.participant.vars["carrying_payoff"] += points
            #p.participant.vars["game_payoff"]["trust"] = points
            p.payoff = points
            p.trust_points = points


class Player(BasePlayer):
    sent_amount = models.IntegerField(min=0, max=600)
    sent_back_amount = models.IntegerField()
    tripled_amount = models.IntegerField()
    remaining_amount = models.IntegerField()
    trust_points = models.IntegerField(initial=0)
