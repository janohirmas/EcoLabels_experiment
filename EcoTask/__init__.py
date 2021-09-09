from otree.api import *
import numpy as np
from numpy import random
from random import SystemRandom, sample
from random import choices
import pandas as pd
import csv

doc = """
Creates Table with Visual Tracing
"""


class Constants(BaseConstants):
    name_in_url         = 'Main-Task'
    # Sustainability Sets
    lS1, lS2 = [[0,1],[1,2],[0,2]], [[0,0],[1,1],[2,2]]
    ## Quality Sets 
    lQc,lQs, lQe= [[1,0],[2,0],[2,1]], [[0,1],[0,2],[1,2]], [[0,0],[1,1],[2,2]]
    ## Price Sets
    lPrices = [1,1.5,2,2.5,3,3]
    lPoe, lPse, lPeq = [],[],[]

    for x  in lPrices:
        for y in lPrices:
            lPair = [x,y]
            if x>y:
                lPoe.append(lPair)
            elif x<y: 
                lPse.append(lPair)
            else:
                lPeq.append(lPair)

    ## Number of trials
    num_reps            = 1 # number of repetitions per permutation
    num_repsEq          = 2 # Number of cases with equal sustainability
    num_prounds         = 3 # Number of Practice Rounds  
    num_rounds          = 2*(num_reps*len(lS1)*5+num_repsEq)+num_prounds # Number of rounds
    players_per_group   = None
    ## Attention Setup variables
    # Checks if you require FullScreen 
    ## if you want to record number of FS changes add integer form iFullscreenChange
    # Checks if focus changes to other pages
    ## if you want to record the number of times that focus is lost, add integer form iFocusLost
    ## if you want to record the total time that focus is lost, add float form dFocusLostT
    sImagePath          = 'EcoTask/figures/'
    sImagePath_static   = 'EcoTask/figures/'     # Image Path        
    txtSustainability   = 'EcoTask/text/sustainability.html'
    txtQuality          = 'EcoTask/text/quality.html'
    imgLeaf_symbol      = sImagePath_static+'one_leaf.png'
    imgStar_symbol      = sImagePath_static+'one_star.png'
    sPathQ_l            = sImagePath_static+'Infographic_graphs/qual_lin.png'
    sPathQ_cv            = sImagePath_static+'Infographic_graphs/qual_concave.png'
    sPathQ_cv            = sImagePath_static+'Infographic_graphs/qual_convex.png'
    sPathS_l            = sImagePath_static+'Infographic_graphs/sus_linear.png'
    sPathS_cv           = sImagePath_static+'Infographic_graphs/sus_concave.png'
    sPathS_cx           = sImagePath_static+'Infographic_graphs/sus_convex.png' 
    # Variables for Infographics
    Q1l,Q1h = 30, 40
    Q2l,Q2h = 40, 50
    Q3l,Q3h = 50, 60
    S1l, S1h = 0, 10
    S2l_l, S2h_l = 10, 20
    S2l_cv, S2h_cv = 15, 25
    S2l_cx, S2h_cx = 5, 15
    S3l, S3h  = 20, 30 
    Currency = 'Pounds'
  
    ## Slides Infographics
    SlidePath = 'Infographics/slide'
    Slides = [
        dict(Title = 'Additional Information', path=SlidePath+'0.html'),
        dict(Title = 'Additional Information', path=SlidePath+'1.html'),    
        dict(Title = 'Additional Information', path=SlidePath+'2.html'),
        dict(Title = 'Everything Clear? Please answer these questions correctly to proceed:', path=SlidePath+'3.html'),
    ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    ## Decision Variables
    iDec                = models.IntegerField(blank=True)
    dRT                 = models.FloatField(blank=True)
    ## Attention Variables
    sButtonClick        = models.StringField(blank=True)
    sTimeClick          = models.StringField(blank=True)
    ## Trial Variables
    iBlock              = models.IntegerField(blank=True)
    iBlockTrial         = models.IntegerField(blank=True)
    iTreatment          = models.IntegerField(blank=True)
    PresOrder           = models.StringField(blank=True)
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
    ## SETUP FOR PARTICIPANT
    if subsession.round_number == 1:
        for player in subsession.get_players():
            p, session = player.participant, subsession.session
            lTreat, lRownames   = createTreatment()
            p.vRownames         = lRownames
            p.mTreat            = lTreat
            iTreatment = session.config['iTreatment']
            if iTreatment == 4:
                p.treatment     = random.randint(1,4)
            else:
                p.treatment     = iTreatment
                
            p.PresOrder         = random.choice(['Qual', 'Sus'])
            p.SelectedTrial     = random.choice(range(Constants.num_prounds+1,Constants.num_rounds))
            print('Trial selected for participant {}: {}'.format(p.code,p.SelectedTrial))
    ## SETUP FOR PLAYER ROUNDS
    for player in subsession.get_players():
        ## Load participant and save participant variables in player
        p = player.participant
        player.iTreatment = int(p.treatment)
        player.PresOrder =  str(p.PresOrder)
        player.sAttrOrder = p.vRownames[1]
        ## Round Variables
        total_rounds = (Constants.num_rounds-Constants.num_prounds)/2
        round = player.round_number-Constants.num_prounds
        if round<1: ## These are practice rounds, random trial selected
            player.iBlock = 0
            player.iBlockTrial = random.randint(total_rounds)
            x = int( player.iBlockTrial-1)
            lAttr = p.mTreat[x].split(',')
        elif (round<=total_rounds): ## These are the observations of the first block
            player.iBlock = 1
            player.iBlockTrial = int(round)
            x = int(round-1)
            lAttr = p.mTreat[x].split(',')
        else: ## These are the observations of the first block
            player.iBlock = 2
            player.iBlockTrial = int(round-total_rounds)
            x = int(round-total_rounds-1)
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

#* Functions
def join2String(list, delimiter= ','):
        return delimiter.join(map(str,list))

def createTreatment():
    n = Constants.num_reps
    n_eq = Constants.num_repsEq

    #* Sets
    iSize = int((Constants.num_rounds-Constants.num_prounds)/2)
    ## Sustainability
    lS1 = Constants.lS1
    lS2 = Constants.lS2
    ## Quality
    lQc = Constants.lQc
    lQs = Constants.lQs
    lQe = Constants.lQe

    ## Prices
    lPoe = Constants.lPoe
    lPse = Constants.lPse
    lPeq = Constants.lPeq


    lTreatments = ["" for x in range(iSize)]
    lPrices     = []
    lQual       = []

    ## Competing Quality and Alternative more expensive
    lPrices.extend(sample(lPoe,n))
    lQual.extend(sample(lQc,n))
    ## Competing Quality and Eco more expensive
    lPrices.extend(sample(lPse,n))
    lQual.extend(sample(lQc,n))
    ## Supporting Quality and Eco more expensive
    lPrices.extend(sample(lPse,n))
    lQual.extend(sample(lQs,n))
    ## Equal Quality and Eco more expensive
    lPrices.extend(sample(lPse,n))
    lQual.extend(sample(lQe,n))
    ## Competing Quality and Equal price
    lPrices.extend(sample(lPeq,n))
    lQual.extend(sample(lQc,n))  

    # Establish order of qualities
    order = sample(['Quality','Sustainability'],2)
    counter = 0
    for i in range(len(lPrices)):
        for sus in range(len(lS1)): 

            # Invert order if in this trial outcomes are flipped
            if random.choice([True,False]):
                #print('flip')
                q       = lQual[i].copy()[::-1]
                s       = lS1[sus].copy()[::-1]
                lAttr   = lPrices[i].copy()[::-1]
            else:
                #print('stick')
                q       = lQual[i].copy()
                s       = lS1[sus].copy()  
                lAttr   = lPrices[i].copy()
            # Add attributes depending order
            if order[0]=='Quality':
                lAttr.extend(q)
                lAttr.extend(s)
            else: 
                lAttr.extend(s)
                lAttr.extend(q)

            lTreatments[counter]=  join2String(lAttr)
            counter +=1

    # Add the observations with equal Sustainability 
    ## Select which trial do we use:
    lCombs = random.randint(0,len(lPrices),size=n_eq)

    for sus in range(n_eq):       
        # Randomize order
        if random.choice([True,False]):
            q       = lQual[lCombs[sus]].copy()[::-1]
            s       = lS2[sus].copy()[::-1]
            lAttr   = lPrices[lCombs[sus]].copy()[::-1]
        else:
            q       = lQual[lCombs[sus]].copy()
            s       = lS2[sus].copy()
            lAttr   = lPrices[lCombs[sus]].copy()

        if order[0]=='Quality':
                lAttr.extend(q)
                lAttr.extend(s)
        else: 
                lAttr.extend(s)
                lAttr.extend(q)
        lTreatments[counter]=  join2String(lAttr)
        counter +=1
    lAttList = ['Price', order[0], order[1]]
    random.shuffle(lTreatments)
    # pd.DataFrame(lTreatments).to_csv('treatment.csv')
    return lTreatments,lAttList

# PAGES
class PracticeInfo1(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class PracticeInfo2(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_prounds

class Task(Page):
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

    staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        # Add Focus variables to total if it's not practice trial
        if (player.round_number < Constants.num_prounds):
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

class Infographics(Page):
    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        
        # Pick images based on treatment for sustainability info
        if participant.treatment == 1:
            S2low, S2high, Sgraph = Constants.S2l_l, Constants.S2h_l, Constants.sPathS_l
        elif participant.treatment == 2:
            S2low, S2high, Sgraph = Constants.S2l_cv, Constants.S2h_cv, Constants.sPathS_cv
        else:
            S2low, S2high, Sgraph = Constants.S2l_cx, Constants.S2h_cx, Constants.sPathS_cx
        # Create Dictionary with all necessary info
        dicSustainabilityInfo = {
            'Item' : 'Leaf-rating & trees planted',
            'Graph' : Sgraph,
            'Title' : 'Sustainability',
            'p1' : 'leaf',
            'p2' : 'sustainability',
            'p3' : 'One tree planted',
            'p4' : 'trees',
            'Symbol' : Constants.imgLeaf_symbol,
            'low1' : Constants.S1l,
            'low2' : S2low,
            'low3' : Constants.S3l,
            'hi1' : Constants.S1h,
            'hi2' : S2high,
            'hi3' : Constants.S3h,
            'disclaimer' : "We will sum the points of all participants to calculate how many trees we need to plant and round it up. Let's say you get 0.8 trees and I get 0.5, that means 1.3 trees in total. Then, we will plant 2 trees! Every point counts! ",
        }
        dicQualityInfo = {
            'Item' : 'Star-rating & Bonus Payment',
            'Graph' : Constants.sPathQ_l,
            'Title' : 'Quality',
            'p1' : 'star',
            'p2' : 'quality',
            'p3' : 'One pound (£)',
            'p4' : Constants.Currency,
            'Symbol' : Constants.imgStar_symbol,
            'low1' : Constants.Q1l,
            'low2' : Constants.Q2l,
            'low3' : Constants.Q3l,
            'hi1' : Constants.Q1h,
            'hi2' : Constants.Q2h,
            'hi3' : Constants.Q3h,
            'disclaimer' : 'You will only get values with no decimals or 50p (4.0 or 4.5 for example)',
        }
        # Pick images based on treatment for sustainability info
        if participant.PresOrder == 'Qual':
            dicFirst, dicSecond    = dicQualityInfo, dicSustainabilityInfo
        else:
            dicFirst, dicSecond  = dicSustainabilityInfo, dicQualityInfo

        return dict(
            First = dicFirst,
            Second = dicSecond,
            Slides = Constants.Slides,
        ) 

    ## Show only in the middle of the experiment
    @staticmethod
    def is_displayed(player):
        return ((player.iBlock==2) & (player.iBlockTrial==1))

    def js_vars(player: Player):
        session = player.subsession.session
        p = player.participant
        # Pick images based on treatment for sustainability info
        if p.PresOrder == 'Qual':
            first, second    = Constants.Q3l, Constants.S1h
        else:
            first, second  = Constants.S3l, Constants.Q1h
        return {
            'StartLeft'         : player.bStartLeft,
            'bRequireFS'        : session.config['bRequireFS'],
            'bCheckFocus'       : session.config['bCheckFocus'],
            'dPixelRatio'       : p.dPixelRatio,
            'firstAnswer'       : str(first),
            'secondAnswer'       : str(second),
        }


class Ready(Page):
    @staticmethod
    def is_displayed(player):
        return ((player.iBlock==2) & (player.iBlockTrial==1))
        

page_sequence = [PracticeInfo1, Between, Task, Infographics, Ready, PracticeInfo2]
