from otree.api import *
from numpy import empty, random
from random import SystemRandom, sample
from random import choices


doc = """
This app creates the questionnaire and shows end page. 
"""


class Constants(BaseConstants):
    name_in_url = 'EndPage'
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
    trial_pay   = models.StringField()
    Bonus       = models.FloatField()
    TreeAmount  = models.IntegerField(blank=True)

# PAGES


class EndPage(Page):
    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        ## Determining Value of Sustainability rating
        S = int(participant.S)
        T = int(participant.treatment)
        Q = int(participant.Q)
        print(type(S))
        if (S!=1):
            Svalue = Constants.S1 + S*Constants.S_step + random.randint(0,Constants.S_step)
        elif (S==1 & T==1):
            Svalue = Constants.S1 + S*Constants.S_step + random.randint(0,Constants.S_step)
        elif (S==1 & T==2):
            Svalue = Constants.S2_2 + random.randint(0,Constants.S_step)
        elif (S==1 & T==3):
            Svalue = Constants.S2_3+ random.randint(0,Constants.S_step) 
        else:
            print('Error determining treatment and Sustainability level')  
        print(Svalue)
        ## Determining value of Quality rating
        Qvalue = Constants.Q1 + Q*Constants.Q_step + random.randint(0,Constants.Q_step)
        participant.Bonus = Qvalue - int(participant.Price)
        participant.TreeAmount = Svalue
        
        return {
            'SelectedTrial' : participant.SelectedTrial,
            'Price' : participant.Price,
            'Q' : Qvalue,
            'S' : Svalue,
            'Bonus' : participant.Bonus,
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        part = player.participant
        player.trial_pay = str(part.SelectedTrial)
        player.Bonus = part.Bonus
        player.TreeAmount = part.TreeAmount


class FinalPage(Page):
    pass



page_sequence = [ EndPage, FinalPage]



