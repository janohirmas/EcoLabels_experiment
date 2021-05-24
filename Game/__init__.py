from otree.api import *
import random

doc = """
This app is for the experiment itself. 
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


# PAGES
class Introduction(Page):
    pass


page_sequence = [Introduction]


