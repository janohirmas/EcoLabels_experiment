from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    D2 = models.StringField()
    D3 = models.StringField()
    QT1 = models.StringField()
    D7 = models.StringField()
    D1 = models.StringField()


# PAGES
class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['D1', 'D2', 'D3', 'D7', 'QT1']


page_sequence = [Questionnaire]
