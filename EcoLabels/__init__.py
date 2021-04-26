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

    # Variables for Demographics
    D0 = models.StringField()
    D1 = models.StringField()
    D2 = models.StringField()
    D3 = models.StringField()
    D4 = models.StringField()
    D5 = models.StringField()
    D6 = models.StringField()

    # variables for Questionnaire
    QT1 = models.StringField()
    QT2 = models.StringField()
    QT3 = models.StringField()
    QT4 = models.StringField()
    QT5 = models.StringField()
    QT6 = models.StringField()
    QT7 = models.StringField()

# PAGES
class Introduction(Page):
    pass

class Instructions(Page):
    form_model = 'player'
    form_fields = ['Q1', 'Q2', 'Q3', 'Q4']

class Demographics(Page):
    form_model = 'player'
    form_fields = ['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6']

class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['QT1', 'QT2', 'QT3','QT4', 'QT5', 'QT6', 'QT7']

    def is_displayed(self):
        return True

class Results(Page):
    pass


page_sequence = [Questionnaire, Demographics, Introduction, Instructions, Results]


