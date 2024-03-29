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
    # Treatment Variables
    lS1 = [[0,1],[1,2],[0,2]]
    lS2 = [[0,0],[1,1],[2,2]]

    ## Quality
    lQc = [[1,0],[2,0],[2,1]]
    lQs = [[0,1],[0,2],[1,2]]
    lQe = [[0,0],[1,1],[2,2]]

    ## Prices
    iP1,iP2,iP3,iP4 = [1,2,3,4]

    lPoe = [[iP2,iP1],[iP3,iP1],[iP3,iP2],[iP4,iP1],[iP4,iP2],[iP4,iP3]]
    lPse = [[iP1,iP2],[iP1,iP3],[iP2,iP3],[iP1,iP4],[iP2,iP4],[iP3,iP4]]
    lPeq = [[iP1,iP1],[iP2,iP2],[iP3,iP3],[iP4,iP4]]

    ## Number of trials
    num_reps            = 1 # number of repetitions per permutation
    num_repsEq          = 2 # Number of cases with equal sustainability
    num_prounds         = 3 # Number of Practice Rounds  
    num_rounds          = 2*(num_reps*len(lS1)*5+num_repsEq)+num_prounds # Number of rounds
    # # ## Modifiable variables
    # Modifiable variables
    # lVars = ['iTreatment', 'sActivation', 'iTimeOut','bRequireFS','bCheckFocus','vTrigger','Attr_order']
    # lDefaults = [1,"'mouseover'",0,True,True,"'val'","'constant'"]
    # for i in range(len(lVars)):
    #     try:
    #         eval(lVars[i])
    #     except NameError:
    #         print('{} is not defined. Set to default.'.format(lVars[i]))
    #         exec("{} = {}".format(lVars[i],lDefaults[i]))
    #     else:
    #         print('{} is defined'.format(lVars[i]))



    players_per_group   = None
    ## Attention Setup variables
    # Checks if you require FullScreen 
    ## if you want to record number of FS changes add integer form iFullscreenChange
    # Checks if focus changes to other pages
    ## if you want to record the number of times that focus is lost, add integer form iFocusLost
    ## if you want to record the total time that focus is lost, add float form dFocusLostT
    Attr_order          = 'constant'
    TablePaddingV       = "1vh" # set up padding between rows (top and bottom)                                  
    TablePaddingH       = "0vh" # set up padding between columns (left and right)                                  
    vColnames           = ["Product A", "Product B"]   # Column Names           
    vRownames           = ["Price","Quality","Sustainability"] # Row Names
    sImagePath          = '/static/EcoTask/figures/'     # Image Path        
    # Image files for infographics (instructions, quality, sustainability: linear/concave/convex)
    txtSustainability   = 'EcoTask/text/sustainability.html'
    txtQuality          = 'EcoTask/text/quality.html'
    imgLeaf_symbol      = 'EcoTask/figures/one_leaf.png'
    imgStar_symbol      = 'EcoTask/figures/one_star.png'
    imgFile_Quality     = 'EcoTask/figures/Infographic_graphs/quality.png'
    imgFile_Linear      = 'EcoTask/figures/Infographic_graphs/sus_linear.png'
    imgFile_Concave     = 'EcoTask/figures/Infographic_graphs/sus_concave.png'
    imgFile_Convex      = 'EcoTask/figures/Infographic_graphs/sus_convex.png' 
    # Variables for Infographics
    Q1l = 4
    Q1h = 5 
    Q2l = 5
    Q2h = 6 
    Q3l = 6
    Q3h = 7 
    S1l = 0
    S1h = 2 
    S2l_l = 2
    S2h_l = 4 
    S2l_cv = 3
    S2h_cv = 5 
    S2l_cx = 1
    S2h_cx = 3 
    S3l = 4
    S3h = 6 
    Currency = 'Pounds'

  
    ## Slides Infographics
    SlidePath = 'Infographics/slide'
    Slides = [
    dict(
        Title = 'Additional Information',
        path=SlidePath+'0.html',
        ),
    dict(
        Title = 'Additional Information',
        path=SlidePath+'1.html',
        ),    
    dict(
        Title = 'Additional Information',
        path=SlidePath+'2.html',
        ),
    dict(
        Title = 'Everything Clear? Please answer these questions correctly to proceed:',
        path=SlidePath+'3.html',
        ),

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
    sTableVals          = models.StringField(blank=True)
    iTreatment          = models.IntegerField(blank=True)
    PresOrder           = models.StringField(blank=True)
    sAttrOrder          = models.StringField(blank=True)
    bStartLeft          = models.BooleanField(blank=True)
    ## Focus Variables
    iFocusLost          = models.IntegerField(blank=True)
    dFocusLostT         = models.FloatField(blank=True)
    iFullscreenChange   = models.IntegerField(blank=True)
    ## Attributes
    P1                  = models.StringField(blank=True)
    P2                  = models.StringField(blank=True)
    Q1                  = models.StringField(blank=True)
    Q2                  = models.StringField(blank=True)
    S1                  = models.StringField(blank=True)
    S2                  = models.StringField(blank=True)



# FUNCTIONS

def creating_session(subsession):
    ## SETUP FOR PARTICIPANT
    if subsession.round_number == 1:
        for player in subsession.get_players():
            participant = player.participant
            session = subsession.session
            lTreat, lRownames = createTreatment()
            participant.vRownames = lRownames
            participant.mTreat = lTreat
            participant.treatment = session.config['iTreatment']
            participant.PresOrder = random.choice(['Qual', 'Sus'])
            participant.SelectedTrial = random.choice(range(Constants.num_prounds+1,Constants.num_rounds))
            print('Trial selected for participant {}: {}'.format(participant.label,participant.SelectedTrial))
    ## SETUP FOR PLAYER ROUNDS
    for player in subsession.get_players():
        ## Load participant and save participant variables in player
        participant = player.participant
        player.iTreatment = int(participant.treatment)
        player.PresOrder  = str(participant.PresOrder)
        player.sAttrOrder = participant.vRownames[1]
        ## Round Variables
        total_rounds = (Constants.num_rounds-Constants.num_prounds)/2
        round = player.round_number-Constants.num_prounds
        if round<1: ## These are practice rounds, random trial selected
            player.iBlock = 0
            player.iBlockTrial = random.randint(total_rounds)
            x = int( player.iBlockTrial-1)
            lAttr = participant.mTreat[x].split(',')
        elif (round<=total_rounds): ## These are the observations of the first block
            player.iBlock = 1
            player.iBlockTrial = int(round)
            x = int(round-1)
            lAttr = participant.mTreat[x].split(',')
        else: ## These are the observations of the first block
            player.iBlock = 2
            player.iBlockTrial = int(round-total_rounds)
            x = int(round-total_rounds-1)
            lAttr = participant.mTreat[x].split(',')
        ## Randomize if mouse starts on left or right
        player.bStartLeft = random.choice([True,False])

        # Check order of Attributes and save them as player variables
        
        player.P1   = lAttr[0]
        player.P2   = lAttr[1]
        
        if participant.vRownames[1]=='Quality':
            player.Q1 = lAttr[2]
            player.Q2 = lAttr[3]
            player.S1 = lAttr[4]
            player.S2 = lAttr[5]
        else:
            player.Q1 = lAttr[4]
            player.Q2 = lAttr[5]
            player.S1 = lAttr[2]
            player.S2 = lAttr[3]

def createTreatment():
    n = Constants.num_reps
    n_eq = Constants.num_repsEq

    #* Sets
    iSize = n*5*3+n_eq
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

    #* Functions
    def join2String(list, delimiter= ','):
        return delimiter.join(map(str,list))

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

class Decision(Page):
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
    ]


    @staticmethod
    def js_vars(player: Player):
        participant = player.participant
        session = player.subsession.session
        lE                  = ['img:leaf_1.png','img:leaf_2.png','img:leaf_3.png']
        lQ                  = ['img:star_1.png','img:star_2.png','img:star_3.png']
        lSus    = [lE[int(player.S1)],lE[int(player.S2)]]
        lQual   = [lQ[int(player.Q1)],lQ[int(player.Q2)]]
        vRownames = participant.vRownames
        vOutcomes = [player.P1,player.P2]
        if vRownames[1]=='Quality':
            vOutcomes.extend(lQual)
            vOutcomes.extend(lSus)
        else:
            vOutcomes.extend(lSus)
            vOutcomes.extend(lQual)
        lOutcomes = ','.join(vOutcomes)
        print('Part: {}, trial: {}'.format(participant.label, player.round_number))


        return {
            'vOutcomes'         : lOutcomes,
            'sActivation'       : session.config['sActivation'],
            'vTrigger'          : session.config['vTrigger'],
            'Attr_order'        : Constants.Attr_order,
            'TablePaddingV'     : Constants.TablePaddingV,
            'TablePaddingH'     : Constants.TablePaddingH,
            'vColnames'         : Constants.vColnames,
            'vRownames'         : vRownames,
            'bRequireFS'        : session.config['bRequireFS'],
            'bCheckFocus'       : session.config['bCheckFocus'],
            'iTimeOut'          : session.config['iTimeOut'],
            'sImagePath'        : Constants.sImagePath,
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
                participant.Price = player.P1
                participant.Q = player.Q1
                participant.S = player.S1
            else:
                participant.Price = player.P1
                participant.Q = player.Q1
                participant.S = player.S1
        
class Between(Page):
    @staticmethod
    def js_vars(player: Player):
        session = player.subsession.session
        return {
            'StartLeft' : player.bStartLeft,
            'bRequireFS'        : session.config['bRequireFS'],
            'bCheckFocus'       : session.config['bCheckFocus'],
        }

class Infographics(Page):
    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        
        # Pick images based on treatment for sustainability info
        if participant.treatment == 1:
            S2low = Constants.S2l_l
            S2high = Constants.S2h_l
            Sgraph = Constants.imgFile_Linear
        elif participant.treatment == 2:
            S2low = Constants.S2l_cv
            S2high = Constants.S2h_cv
            Sgraph = Constants.imgFile_Concave
        else:
            S2low = Constants.S2l_cx
            S2high = Constants.S2h_cx
            Sgraph = Constants.imgFile_Convex
        # Create Dictionary with all necessary info
        dicSustainabilityInfo = {
            'Item' : 'Leaf-rating & trees planted',
            'Graph' : Sgraph,
            'Title' : 'Sustainability',
            'p1' : 'leaf',
            'p2' : 'sustainability',
            'p3' : 'amount of planted trees',
            'p4' : 'trees',
            'Symbol' : Constants.imgLeaf_symbol,
            'low1' : Constants.S1l,
            'low2' : S2low,
            'low3' : Constants.S3l,
            'hi1' : Constants.S1h,
            'hi2' : S2high,
            'hi3' : Constants.S3h,

        }
        dicQualityInfo = {
            'Item' : 'Star-rating & Bonus Payment',
            'Graph' : Constants.imgFile_Quality,
            'Title' : 'Quality',
            'p1' : 'star',
            'p2' : 'quality',
            'p3' : 'bonus payment',
            'p4' : Constants.Currency,
            'Symbol' : Constants.imgStar_symbol,
            'low1' : Constants.Q1l,
            'low2' : Constants.Q2l,
            'low3' : Constants.Q3l,
            'hi1' : Constants.Q1h,
            'hi2' : Constants.Q2h,
            'hi3' : Constants.Q3h,

        }
        # Pick images based on treatment for sustainability info
        if participant.PresOrder == 'Qual':
            dicFirst    = dicQualityInfo
            dicSecond   = dicSustainabilityInfo
        else:
            dicFirst   = dicSustainabilityInfo
            dicSecond    = dicQualityInfo

        return dict(
            First = dicFirst,
            Second = dicSecond,
            Slides = Constants.Slides,
        ) 
    ## Show only in the middle of the experiment
    @staticmethod
    def is_displayed(player):
        return ((player.iBlock==2) & (player.iBlockTrial==1))

class Ready(Page):
    @staticmethod
    def is_displayed(player):
        return ((player.iBlock==2) & (player.iBlockTrial==1))
        

page_sequence = [PracticeInfo1, Between, Decision, Infographics, Ready, PracticeInfo2]
