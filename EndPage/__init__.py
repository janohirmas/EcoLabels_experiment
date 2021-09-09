from otree.api import *
from numpy import random
import numpy as np
import time



doc = """
This app creates the questionnaire and shows end page. 
"""


class Constants(BaseConstants):
    name_in_url = 'EndPage'
    players_per_group = None
    num_rounds = 1
    # Quality and Sustainability ranges
    Q1      = 30
    Q_step  = 10
    S1      = 0
    S2_2    = 15
    S2_3    = 5
    S3      = 10
    S_step  = 10
    # Prolific Link
    ProlificLink = "https://www.google.com"
    Slides = [
        dict(
            Title = 'Results',
            path='EndPage/slide0.html',
            ),
        dict(
            Title = 'Results',
            path='EndPage/slide1.html',
            ),        
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Selected Trial
    partID              = models.StringField()
    SelectedTrial       = models.IntegerField()
    Bonus               = models.FloatField()
    TreeAmount          = models.IntegerField()
    ProlificID          = models.StringField()
    validQ              = models.IntegerField()
    TotalTime           = models.FloatField()
    dTimeOutFocus       = models.FloatField()
    iOutFocus           = models.IntegerField()
    iFSChanges          = models.IntegerField()
    sTreesLocation      = models.StringField()


# PAGES


class EndPage(Page):

    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        ## Determining Value of Sustainability rating
        S = int(participant.S)
        T = int(participant.treatment)
        Q = int(participant.Q)
        print(type(T))
        print([S==1,T==2])
        if (T==1):
            Smin = Constants.S1 + S*Constants.S_step 
        elif (S==1 & T==2):
            Smin = Constants.S2_2 
        elif (S==1 & T==3):
            Smin = Constants.S2_3
        Smax = Smin + Constants.S_step +1
        Svalue = random.randint(Smin,Smax)/10
        ## Determining value of Quality rating
        Qmin = Constants.Q1 + Q*Constants.Q_step
        Qmax = Qmin + Constants.Q_step + 1
        Qvalue = np.floor(random.randint(Qmin,Qmax)/5)/2
        participant.Bonus = Qvalue - int(participant.Price)
        participant.TreeAmount = Svalue
        
        return {
            'Slides' :  Constants.Slides,
            'SelectedTrial' : participant.SelectedTrial,
            'Price' : participant.Price,
            'Q' : Qvalue,
            'S' : Svalue,
            'Bonus' : participant.Bonus,
            'TreeLocation' : str(participant.sTreesLocation),
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        # Define Participant and other Vars
        part    = player.participant
        start   = part.startTime
        end     = time.time()
        # Save relevant variables
        player.partID           = part.code
        player.ProlificID       = part.label
        player.TotalTime        = end - start
        player.SelectedTrial    = int(part.SelectedTrial)
        player.Bonus            = part.Bonus
        player.TreeAmount       = part.TreeAmount
        player.validQ           = part.validQuestionnaire
        player.iFSChanges       = part.iFullscreenChanges
        player.iOutFocus        = part.iOutFocus
        player.dTimeOutFocus    = part.dTimeOutFocus
        player.sTreesLocation   = part.sTreesLocation

class FinalPage(Page):
    pass



page_sequence = [ EndPage, FinalPage]



