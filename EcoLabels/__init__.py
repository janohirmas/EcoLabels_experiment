from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'EcoLabels'
    players_per_group = None
    num_rounds = 1
    

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Q1 = models.IntegerField()
    Q2 = models.StringField()
    Q3 = models.StringField()
    Q4 = models.IntegerField()

# PAGES
class Introduction(Page):
    pass

class Instructions(Page):
    form_model = 'player'
    form_fields = ['Q1', 'Q2', 'Q3', 'Q4']

class Results(Page):
    pass


page_sequence = [Introduction, Instructions, Demographics, Questionnaire, Results]


