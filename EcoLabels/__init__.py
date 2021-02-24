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
    Q1 = models.StringField(label="Question 1:")
    Q2 = models.StringField(label="Question 2:")


# PAGES
class Introduction(Page):
    pass

class Instructions(Page):
    form_model = 'player'
    form_fields = ['Q1', 'Q2']

class Results(Page):
    pass


page_sequence = [Introduction, Instructions, Results]

