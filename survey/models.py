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

from django_countries.fields import CountryField

doc = """
Survey questions to collect general background information about the subjects.
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1
    ETHNICITY = ['Bukusu',
                 'Chonyi',
                 'Digo',
                 'Duruma',
                 'Elgeyo',
                 'Embu',
                 'Giriama',
                 'Isukha',
                 'Jibana',
                 'Kalenjin',
                 'Kamba',
                 'Kauma',
                 'Kikuyu',
                 'Kipsigis',
                 'Kisii',
                 'Kuria',
                 'Luhya',
                 'Luo',
                 'Maasai',
                 'Maragoli',
                 'Marakwet',
                 'Marama',
                 'Meru',
                 'MijiKenda',
                 'Nandi',
                 'Okiek',
                 'Orma',
                 'Oromo',
                 'Pokomo',
                 'Pokot',
                 'Rabai',
                 'Rendile',
                 'Ribe',
                 'Sabaot',
                 'Samburu',
                 'Sengwer',
                 'Somali',
                 'Swahili',
                 'Tachoni',
                 'Taita',
                 'Taveta',
                 'Terik',
                 'Tugen',
                 'Turkana',
                 'Prefer not to say',]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def set_payoff(self):
        """Calculate payoff, which is zero for the survey"""
        self.payoff = 0

    c_r_1 = models.CharField()
    c_r_2 = models.IntegerField()
    c_r_4 = models.IntegerField()
    c_r_5 = models.IntegerField()
    c_r_6 = models.IntegerField()

    demo_1_scl = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '10'}))

    age = models.IntegerField(blank=True, null=True)

    height = models.IntegerField(blank=True, null=True)

    weight = models.IntegerField(blank=True, null=True)

    gender = models.CharField(choices=['Male', 'Female', "Prefer not to say"],
                              widget=widgets.RadioSelect())

    affct1_scl = models.IntegerField(widget=widgets.SliderInput(attrs={'step': '1', 'min': '1', 'max': '7'}))
    
    affct2_scl = models.IntegerField(widget=widgets.SliderInput(attrs={'step': '1', 'min': '1', 'max': '7'}))

    ethnicity = models.CharField(choices=Constants.ETHNICITY,
                                 widget=widgets.RadioSelectHorizontal())

    cali_residnc = models.CharField(
        choices=['No', 'Yes, for 5 years or more', 'Yes, for less than 5 years', 'Prefer not to say'],
        widget=widgets.RadioSelect())

    father_occ = models.CharField(widget=widgets.RadioSelect(),
                                         choices=["Wage-employed", "Self-employed", "Unemployed", "Prefer not to say"]
                                         )

    mother_occ = models.CharField(widget=widgets.RadioSelect(),
                                         choices=["Wage-employed", "Self-employed", "Unemployed", "Prefer not to say"]
                                         )

    income = models.CharField(widget=widgets.RadioSelect(),
                              choices=["Less than Ksh.10,000",
                                       "Ksh.10,000 - Ksh. 30,000",
                                       "Ksh. 30,000 - Ksh. 60,000",
                                       "Ksh. 60,000 - Ksh.100,000",
                                       "More than Ksh.100,000",
                                       "Don't know",
                                       "Prefer not to say"
                                       ])

    edu_father = models.CharField(widget=widgets.RadioSelect(),
                                        choices=["Completed Primary",
                                                 "Completed Secondary",
                                                 "Completed technical college",
                                                 "Completed University",
                                                 "Other",
                                                 "Prefer not to say"
                                                 ])

    edu_mother = models.CharField(widget=widgets.RadioSelect(),
                                        choices=["Completed Primary",
                                                 "Completed Secondary",
                                                 "Completed technical college",
                                                 "Completed University",
                                                 "Other",
                                                 "Prefer not to say"
                                                 ])
