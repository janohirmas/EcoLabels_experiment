from email.policy import default
from otree.api import *
import numpy as np
from numpy import random
from random import SystemRandom, sample
from random import choices
import pandas as pd
import csv

from sqlalchemy import true

doc = """
Creates Table with Visual Tracing
"""


class Constants(BaseConstants):
    name_in_url         = 'Main-Task2'
    ## Number of trials
    num_reps            = 1 # number of repetitions per permutation
    num_repsEq          = 2 # Number of cases with equal sustainability
    num_prounds         = 0 # Number of Practice Rounds  
    num_rounds          = (num_reps*3*5+num_repsEq)+num_prounds # Number of rounds
    players_per_group   = None
    sImagePath          = 'global/figures/'

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    ## Decision Variables
    iDec                = models.IntegerField(blank=True)
    dRT                 = models.FloatField(blank=True)
    ## Attention Variables
    sButtonClick        = models.LongStringField(blank=True)
    sTimeClick          = models.LongStringField(blank=True)
    ## Trial Variables
    iPracticeRound      = models.BooleanField(initial=0)
    iBlock              = models.IntegerField(initial=2)
    iBlockTrial         = models.IntegerField(blank=True)
    sAttrOrder          = models.StringField(blank=True)
    bStartLeft          = models.BooleanField(blank=True)
    dRTbetween          = models.FloatField(blank=True)
    dTime2First         = models.FloatField(blank=True)
    ## Focus Variables
    iFocusLost          = models.IntegerField(blank=True)
    dFocusLostT         = models.FloatField(blank=True)
    iFullscreenChange   = models.IntegerField(blank=True)
    ## Attributes
    P0                  = models.StringField(blank=True)
    P1                  = models.StringField(blank=True)
    Q0                  = models.StringField(blank=True)
    Q1                  = models.StringField(blank=True)
    S0                  = models.StringField(blank=True)
    S1                  = models.StringField(blank=True)



# FUNCTIONS

def creating_session(subsession):
    ## SETUP FOR PLAYER ROUNDS
    for player in subsession.get_players():
        ## Load participant and save participant variables in player
        p = player.participant
        player.sAttrOrder = p.sAttrOrder = p.vRownames[1] # Order of presentation of attributes. 1st attribute always price, then Q or S
        ## Round Variables
        total_rounds = Constants.num_rounds-Constants.num_prounds
        round = player.round_number-Constants.num_prounds

        if round<1: ## These are practice rounds, random trial selected
            player.iPracticeRound   = 1
            player.iBlockTrial      = random.randint(total_rounds)
            x = int( player.iBlockTrial-1)
            lAttr = p.mTreat[x].split(',')
        elif (round<=total_rounds): ## These are the trials of the block
            player.iBlockTrial = int(round)
            x = int(round-1)
            lAttr = p.mTreat[x].split(',')

        ## Randomize if mouse starts on left or right
        player.bStartLeft = random.choice([True,False])
        # Check order of Attributes and save them as player variables
        player.P0   = lAttr[0]
        player.P1   = lAttr[1]
        if p.vRownames[1]=='Quality':
            player.Q0 = lAttr[2]
            player.Q1 = lAttr[3]
            player.S0 = lAttr[4]
            player.S1 = lAttr[5]
        else:
            player.Q0 = lAttr[4]
            player.Q1 = lAttr[5]
            player.S0 = lAttr[2]
            player.S1 = lAttr[3]


# PAGES
class Task(Page):
    template_name = 'ecotask/Task.html'

    form_model = 'player'
    form_fields = [
        'iDec', 
        'sButtonClick', 
        'sTimeClick',
        'dRT',
        'sAttrOrder',
        'iFocusLost',
        'dFocusLostT',
        'iFullscreenChange',
        'dTime2First',
    ]


    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        print('Part: {}, trial: {}'.format(participant.label, player.round_number))
        vRownames = participant.vRownames   ## Variable order
        Q0,Q1 = str(int(player.Q0)+1),str(int(player.Q1)+1)
        S0,S1 = str(int(player.S0)+1),str(int(player.S1)+1)
        if vRownames[1]=='Quality':
            A10 = Constants.sImagePath+'star_'+Q0+'.png'
            A11 = Constants.sImagePath+'star_'+Q1+'.png'
            A20 = Constants.sImagePath+'leaf_'+S0+'.png'
            A21 = Constants.sImagePath+'leaf_'+S1+'.png'
        else:
            A10 = Constants.sImagePath+'leaf_'+S0+'.png'
            A11 = Constants.sImagePath+'leaf_'+S1+'.png'
            A20 = Constants.sImagePath+'star_'+Q0+'.png'
            A21 = Constants.sImagePath+'star_'+Q1+'.png'

        return dict(
            Attr1 = vRownames[1],
            Attr2 = vRownames[2],
            P0 = player.P0,
            P1 = player.P1,
            A10 = A10,
            A11 = A11,
            A20 = A20,
            A21 = A21,
        ) 

    @staticmethod
    def js_vars(player: Player):
        session = player.session
        p = player.participant
        return {
            'bRequireFS'        : session.config['bRequireFS'],
            'bCheckFocus'       : session.config['bCheckFocus'],
            'iTimeOut'          : session.config['iTimeOut'],
            'dPixelRatio'       : p.dPixelRatio,
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        # Add Focus variables to total if it's not practice trial
        if (player.round_number > Constants.num_prounds):
            participant.iOutFocus = int(participant.iOutFocus) + player.iFocusLost
            participant.iFullscreenChanges = int(participant.iFullscreenChanges) + player.iFullscreenChange
            participant.dTimeOutFocus = float(participant.dTimeOutFocus) + player.dFocusLostT
        # If this is selected trial, save relevant variables
        if (participant.SelectedTrial==player.round_number):
            if (player.iDec==0):
                participant.Price = player.P0
                participant.Q = player.Q0
                participant.S = player.S0
            else:
                participant.Price = player.P1
                participant.Q = player.Q1
                participant.S = player.S1
       


        
class Between(Page):
    template_name = 'ecotask/Between.html'

    form_model = 'player'
    form_fields = [
        'dRTbetween',
    ]
    
    @staticmethod
    def js_vars(player: Player):
        session = player.subsession.session
        p = player.participant
        return {
            'StartLeft'         : player.bStartLeft,
            'bRequireFS'        : session.config['bRequireFS'],
            'bCheckFocus'       : session.config['bCheckFocus'],
            'dPixelRatio'       : p.dPixelRatio,
        }

class Ready(Page):
    template_name = 'ecotask/Ready.html'

    @staticmethod
    def vars_for_template(player: Player):
        # Return selected text
        return dict(
            text = 'Now, we will continue with the experiment.'
        )

    @staticmethod
    def is_displayed(player):
        # Displayed on: First round of each block or first round after the trials
        return (player.round_number==1)
        

page_sequence = [Ready, Between, Task]
