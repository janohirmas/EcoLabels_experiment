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

    # variables for instructions
    Q1 = models.IntegerField()
    Q2 = models.StringField()
    Q3 = models.StringField()
    Q4 = models.IntegerField()

    # Variables for Demographics
    D1 = models.StringField()
    D2 = models.StringField()
    D3 = models.StringField()
    D4 = models.StringField()
    D5 = models.StringField()
    D6 = models.StringField()
    D7 = models.StringField()

    # variables for Questionnaire
    QT1 = models.StringField()
    QT2 = models.StringField()
    QT3 = models.StringField()
    QT4 = models.StringField()
    QT5 = models.StringField()
    QT6 = models.StringField()
    QT7 = models.StringField()
    QT8 = models.StringField()
    QT9 = models.StringField()
    QT10 = models.StringField()
    QT11= models.StringField()
    QT12= models.StringField()
    QT13 = models.StringField()
    QT14 = models.StringField()
    QT15 = models.StringField()
    QT16= models.StringField()
    QT17= models.StringField()
    QT18= models.StringField()
    QT19= models.StringField()
    QT20= models.StringField()
    QT21= models.StringField()
    QT22 = models.StringField()
    QT23 = models.StringField()
    QT24= models.StringField()
    QT25 = models.StringField()
    QT26 = models.StringField()
    QT27 = models.StringField()

# PAGES
class Introduction(Page):
    pass

class Instructions(Page):
    form_model = 'player'
    form_fields = ['Q1', 'Q2', 'Q3', 'Q4']

class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'QT1', 'QT2', 'QT3','QT4', 'QT5', 'QT6', 'QT7','QT8', 'QT9', 'QT10', 'QT11', 'QT12', 'QT13', 'QT14', 'QT15','QT16', 'QT17', 'QT18','QT19', 'QT20', 'QT21', 'QT22','QT23', 'QT24', 'QT25','QT26', 'QT27']

    def is_displayed(self):
        return True

class old_Questionnaire(Page):
    pass

class Results(Page):
    pass


page_sequence = [Questionnaire, Instructions, old_Questionnaire,  Introduction, Results]


