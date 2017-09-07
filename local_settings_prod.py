import os
from settings import BASE_DIR
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

USE_POINTS = False
SESSION_CONFIGS = [
    {
        "name": "full_exp",
        "display_name": "Almas Temparature Experiment",
        "num_demo_participants": 6,
        "app_sequence": ["production", "real_effort_dictator", "risk_game", "time_preference", "trust", "public_goods",
                         "ravens", "joy_of_destruction", "charity_donation", "survey", "payment_info"],
    },
]

DEBUG = False
