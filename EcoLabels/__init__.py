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
    pass


# PAGES
class Introduction(Page):
    pass

class Instructions(Page):
    pass

class Results(Page):
    pass


page_sequence = [Introduction, Instructions, Results]

