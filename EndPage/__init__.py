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

    # Selected Trial
    TreesLocation = models.StringField(blank=True)
    Bonus = models.FloatField(blank=True)

# PAGES


class EndPage(Page):
    form_model = 'player'
    form_fields = ['TreesLocation']
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
        player.Bonus = Qvalue - int(participant.Price)

        return {
            'SelectedTrial' : participant.SelectedTrial,
            'Price' : participant.Price,
            'Q' : Qvalue,
            'S' : Svalue,
            'Bonus' : player.Bonus,
        }

page_sequence = [EndPage]


