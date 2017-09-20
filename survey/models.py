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
                 'prefer not to say',]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def set_payoff(self):
        """Calculate payoff, which is zero for the survey"""
        self.payoff = 0

    cognitive_reflection_one = models.CharField()
    cognitive_reflection_two = models.CharField()
    # cognitive_reflection_three = models.CharField()
    cognitive_reflection_four = models.CharField()
    cognitive_reflection_five = models.CharField()
    cognitive_reflection_six = models.CharField()

    demographic_one_scale = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '10'}))

    age = models.CharField(default="Prefer not to say", blank=True, null=True)

    height = models.CharField(default="Prefer not to say", blank=True, null=True)

    weight = models.CharField(default="Prefer not to say", blank=True, null=True)

    gender = models.CharField(choices=['Male', 'Female', "Prefer not to say"],
                              widget=widgets.RadioSelect())

    ethnicity = models.CharField(choices=Constants.ETHNICITY,
                                 widget=widgets.RadioSelectHorizontal())

    california_residency = models.CharField(
        choices=['No', 'Yes, for 5 years or more', 'Yes, for less than 5 years', 'Prefer not to say'],
        widget=widgets.RadioSelect())

    father_occupation = models.CharField(widget=widgets.RadioSelect(),
                                         choices=["Wage-employed", "Self-employed", "Unemployed", "Prefer not to say"]
                                         )

    mother_occupation = models.CharField(widget=widgets.RadioSelect(),
                                         choices=["Wage-employed", "Self-employed", "Unemployed", "Prefer not to say"]
                                         )

    income = models.CharField(widget=widgets.RadioSelect(),
                              choices=["Less than $24,000",
                                       "$24,000 - $45,000",
                                       "$45,000 - $75,000",
                                       "$75,000 - $121,000",
                                       "More than $121,000",
                                       "Don't know",
                                       "Prefer not to say"
                                       ])

    education_father = models.CharField(widget=widgets.RadioSelect(),
                                        choices=["Completed Primary",
                                                 "Completed Secondary",
                                                 "Completed technical college",
                                                 "Completed University",
                                                 "Other",
                                                 "Prefer not to say"
                                                 ])

    education_mother = models.CharField(widget=widgets.RadioSelect(),
                                        choices=["Completed Primary",
                                                 "Completed Secondary",
                                                 "Completed technical college",
                                                 "Completed University",
                                                 "Other",
                                                 "Prefer not to say"
                                                 ])

    crt_bat = models.PositiveIntegerField()
    crt_widget = models.PositiveIntegerField()
    crt_lake = models.PositiveIntegerField()
