from django.forms import forms, widgets as dj_widgets
from django import forms
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django.db import models as dj_models

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'debrief'
    players_per_group = None
    num_rounds = 1
    CHOICES_Q9 = [('Not very confident', ''),
                  ('Somewhat confident', ''),
                  ('Moderately confident', ''),
                  ('Very confident', ''),
                  ('Prefer not to answer', ''),
                  ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.CharField(choices=['Comfortable', 'Uncomfortable'], widget=widgets.RadioSelect())
    q1_comment = models.CharField(widget=forms.Textarea(
        attrs={"placeholder": "Please share any other comments on chair comfort:",
               "style": "height: 100px; width: 70%; padding: 8px;"}
    ), blank=True)

    q2 = models.CharField(choices=['Comfortable', 'Too bright', 'Too dim'], widget=widgets.RadioSelect())
    q2_comment = models.CharField(widget=forms.Textarea(
        attrs={"placeholder": "Please share any other comments on screen brightness:",
               "style": "height: 100px; width: 70%; padding: 8px;"}
    ), blank=True)

    q3 = models.CharField(choices=['Comfortable', 'Too dry', 'Too humid'], widget=widgets.RadioSelect())
    q3_comment = models.CharField(widget=forms.Textarea(
        attrs={"placeholder": "Please share any other comments on air quality:",
               "style": "height: 100px; width: 70%; padding: 8px;"}
    ), blank=True)

    q4 = models.CharField(choices=['Comfortable', 'Too cold', 'Too hot'], widget=widgets.RadioSelect())
    q4_comment = models.CharField(widget=forms.Textarea(
        attrs={"placeholder": "Please share any other comments on room temperature:",
               "style": "height: 100px; width: 70%; padding: 8px;"}
    ), blank=True)

    q5 = models.CharField(choices=['Comfortable', 'Too bright', 'Too dim'], widget=widgets.RadioSelect())
    q5_comment = models.CharField(widget=forms.Textarea(
        attrs={"placeholder": "Please share any other comments on room lighting:",
               "style": "height: 100px; width: 70%; padding: 8px;"}
    ), blank=True)

    q6 = models.CharField(choices=['Comfortable', 'Too empty', 'Too crowded'], widget=widgets.RadioSelect())
    q6_comment = models.CharField(widget=forms.Textarea(
        attrs={"placeholder": "Please share any other comments on room spacing:",
               "style": "height: 100px; width: 70%; padding: 8px;"}
    ), blank=True)

    q7 = models.CharField(choices=['Comfortable', 'Too silent', 'Too noisy'], widget=widgets.RadioSelect())
    q7_comment = models.CharField(widget=forms.Textarea(
        attrs={"placeholder": "Please share any other comments on noise level:",
               "style": "height: 100px; width: 70%; padding: 8px;"}
    ), blank=True)

    q8_g = models.CharField(choices=[('Generosity', 'Generosity')],widget=widgets.RadioSelect(), blank=True)
    q8_sb = models.CharField(choices=[('Screen brightness', 'Screen brightness')], widget=widgets.RadioSelect(), blank=True)
    q8_rl = models.CharField(choices=[('Room lighting', 'Room lighting')], widget=widgets.RadioSelect(), blank=True)
    q8_gd = models.CharField(choices=[('Gender Discrimination', 'Gender Discrimination')], widget=widgets.RadioSelect(), blank=True)
    q8_rt = models.CharField(choices=[('Room temperature', 'Room temperature')], widget=widgets.RadioSelect(), blank=True)
    q8_rs = models.CharField(choices=[('Room space', 'Room space')], widget=widgets.RadioSelect(), blank=True)
    q8_an = models.CharField(choices=[('Ambient noise', 'Ambient noise')], widget=widgets.RadioSelect(), blank=True)
    q8_none = models.CharField(choices=[('None of the above', 'None of the above')], widget=widgets.RadioSelect(), blank=True)
    q8_other_c = models.CharField(choices=[('other', 'other')], widget=widgets.RadioSelect(), blank=True)

    q8_other = models.CharField(widget=forms.Textarea(
        attrs={"style": "height: 100px; width: 70%; padding: 8px;", "id": "q8_other", "placeholder": "Other:"}
    ), blank=True)

    q9_g = models.CharField(choices=Constants.CHOICES_Q9, widget=widgets.RadioSelect(), blank=True)
    q9_sb = models.CharField(choices=Constants.CHOICES_Q9, widget=widgets.RadioSelect(), blank=True)
    q9_rl = models.CharField(choices=Constants.CHOICES_Q9, widget=widgets.RadioSelect(), blank=True)
    q9_gd = models.CharField(choices=Constants.CHOICES_Q9, widget=widgets.RadioSelect(), blank=True)
    q9_rt = models.CharField(choices=Constants.CHOICES_Q9, widget=widgets.RadioSelect(), blank=True)
    q9_rs = models.CharField(choices=Constants.CHOICES_Q9, widget=widgets.RadioSelect(), blank=True)
    q9_an = models.CharField(choices=Constants.CHOICES_Q9, widget=widgets.RadioSelect(), blank=True)
    q9_other = models.CharField(choices=Constants.CHOICES_Q9, widget=widgets.RadioSelect(), blank=True)

    q10 = models.CharField(choices=['Upon entering the room',
                                    'While waiting for the experiment to begin',
                                    'Sometime during the experiment',
                                    'During the computer survey',
                                    'During this paper survey',
                                    'Prefer not to answer'
                                    ], widget=widgets.RadioSelect())
