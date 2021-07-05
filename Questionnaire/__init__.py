from otree.api import *
from numpy import random
from random import SystemRandom, sample
from random import choices


doc = """
This app creates the questionnaire and shows end page. 
"""


class Constants(BaseConstants):
    name_in_url = 'Questionnaire'
    players_per_group = None
    num_rounds = 1
        # Quality and Sustainability ranges
    Q1      = 5
    Q_step  = 2
    S1      = 0
    S2_2    = 3
    S2_3    = 1
    S3      = 4
    S_step  = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

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
def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'Prolific_id', 'Bonus', 'TreeLocation', 'TreeAmount']
    for p in players:
        participant = p.participant
        session = p.session
        yield [session.code, participant.code, participant.prolific_id , participant.Bonus, participant.TreeLocation, participant.TreeAmount]

class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'QT1', 'QT2', 'QT3','QT4', 'QT5', 'QT6', 'QT7','QT8', 'QT9', 'QT10', 'QT11', 'QT12', 'QT13', 'QT14', 'QT15','QT16', 'QT17', 'QT18','QT19', 'QT20', 'QT21', 'QT22','QT23', 'QT24', 'QT25','QT26', 'QT27']

class EndPage(Page):
    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        ## Determining Value of Sustainability rating
        S = int(participant.S)
        T = int(participant.treatment)
        Q = int(participant.Q)
        if (S!=1):
            Svalue = Constants.S1 + S*Constants.S_step + random.randint(0,Constants.S_step)
        elif (S==2 & T==1):
            Svalue = Constants.S1 + S*Constants.S_step + random.randint(0,Constants.S_step)
        elif (S==2 & T==2):
            Svalue = Constants.S2_2 + random.randint(0,Constants.S_step)
        elif (S==2 & T==3):
            Svalue = Constants.S2_3+ random.randint(0,Constants.S_step) 
        else:
            print('Error determining treatment and Sustainability level')  
        print(Svalue)
        ## Determining value of Quality rating
        Qvalue = Constants.Q1 + Q*Constants.Q_step + random.randint(0,Constants.Q_step)
        participant.Bonus = Qvalue - int(participant.Price)
        
        return {
            'SelectedTrial' : participant.SelectedTrial,
            'Price' : participant.Price,
            'Q' : Qvalue,
            'S' : Svalue,
            'Bonus' : participant.Bonus,
        }


class FinalPage(Page):
    pass



page_sequence = [Questionnaire, EndPage, FinalPage]


