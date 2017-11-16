from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Debrief(Page):
    form_fields = ["q1", "q1_comment",
                   "q2", "q2_comment",
                   "q3", "q3_comment",
                   "q4", "q4_comment",
                   "q5", "q5_comment",
                   "q6", "q6_comment",
                   "q7", "q7_comment",
                   "q8_g", "q8_sb",
                   "q8_rl", "q8_gd",
                   "q8_rt", "q8_rs",
                   "q8_an", "q8_none",
                   "q8_other", "q8_other_c",
                   "q9_g", "q9_sb",
                   "q9_rl", "q9_gd",
                   "q9_rt", "q9_rs",
                   "q9_an", "q9_other",
                   "q10"]
    form_model = models.Player


page_sequence = [
    Debrief
]
