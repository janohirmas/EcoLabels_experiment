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
    name_in_url         = 'EcoTask'
    players_per_group   = None
    # Number of rounds
    num_rounds          = 66 
    # Number of Practice Rounds                                    
    num_prounds         = 3
    # mouseover or click 
    sActivation         = 'mouseover'                             
    # List that can include val,col,row
    vTrigger            = "val"                                   
    # random or constant
    Attr_order          = "constant"  
    # Timeout time (in seconds)
    ## if no time-out required, leave as 0
    iTimeOut            = 0
    # Checks if you require FullScreen
    ## if you want to record number of FS changes add integer form iFullscreenChange
    bRequireFS          = True                                   
    # Checks if focus changes to other pages
    ## if you want to record the number of times that focus is lost, add integer form iFocusLost
    ## if you want to record the total time that focus is lost, add float form dFocusLostT
    bCheckFocus         = True                               
    # set up padding between rows (top and bottom)
    TablePaddingV       = "1vh"                                   
    # set up padding between columns (left and right)
    TablePaddingH       = "0vh"                                   
    # Column Names
    vColnames           = ["Product A", "Product B"]              
    # Row Names
    vRownames           = ["Price","Quality","Sustainability"] 
    # Image Path
    sImagePath          = '/static/EcoTask/figures/'        
    # Image files for infographics (instructions, quality, sustainability: linear/concave/convex)
    test_graph          = 'EcoTask/figures/Infographic_graphs/Q_double_1-3.png'
    imgFile_Inst        = 'EcoTask/figures/instruction.png'
    imgFile_Quality     = 'EcoTask/figures/quality.png'
    imgFile_Linear      = 'EcoTask/figures/sus_linear.png'
    imgFile_Concave     = 'EcoTask/figures/sus_nonlin_high.png'
    imgFile_Convex      = 'EcoTask/figures/sus_nonlin_low.png'  
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
    sTableVals          = models.StringField(blank=True)
    iTreatment          = models.IntegerField(blank=True)
    PresOrder           = models.StringField(blank=True)
    sAttrOrder          = models.StringField(blank=True)
    bStartLeft          = models.BooleanField(blank=True)
    ## Trial Variables
    iFocusLost          = models.IntegerField(blank=True)
    dFocusLostT         = models.FloatField(blank=True)
    iFullscreenChange   = models.IntegerField(blank=True)
    P1                  = models.StringField(blank=True)
    P2                  = models.StringField(blank=True)
    Q1                  = models.StringField(blank=True)
    Q2                  = models.StringField(blank=True)
    S1                  = models.StringField(blank=True)
    S2                  = models.StringField(blank=True)



# FUNCTIONS

def creating_session(subsession):
    if subsession.round_number == 1:
        for player in subsession.get_players():
            participant = player.participant
            lTreat, lRownames = createTreatment()
            participant.vRownames = lRownames
            participant.mTreat = lTreat
            participant.treatment = random.choice([1, 2, 3])
            participant.PresOrder = random.choice(['Qual', 'Sus'])
            participant.SelectedTrial = random.choice(range(1,Constants.num_rounds))
            print(participant.SelectedTrial)

    for player in subsession.get_players():
        ## Load participant and save participant variables in player
        participant = player.participant
        player.iTreatment = int(participant.treatment)
        player.PresOrder  = str(participant.PresOrder)
        player.sAttrOrder = participant.vRownames[1]
        ## Round Variables
        round = player.round_number
        total_rounds = Constants.num_rounds/2
        ## Define same attributes for first and second block
        if round<total_rounds:
            x = int(round-1)
            lAttr = participant.mTreat[x].split(',')
        else:
            x = int(round-total_rounds-1)
            lAttr = participant.mTreat[x].split(',')
        ## Randomize if mouse starts on left or right
        player.bStartLeft = random.choice([True,False])
        # // print(lAttr)

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
    #* Sets
    iSize = 2*5*3+3

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
    lPrices.extend(sample(lPoe,2))
    lQual.extend(sample(lQc,2))
    ## Competing Quality and Eco more expensive
    lPrices.extend(sample(lPse,2))
    lQual.extend(sample(lQc,2))
    ## Supporting Quality and Eco more expensive
    lPrices.extend(sample(lPse,2))
    lQual.extend(sample(lQs,2))
    ## Equal Quality and Eco more expensive
    lPrices.extend(sample(lPse,2))
    lQual.extend(sample(lQe,2))
    ## Competing Quality and Equal price
    lPrices.extend(sample(lPeq,2))
    lQual.extend(sample(lQc,2))  

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

    # Add the observations with equal prices 
    ## Select which trial do we use:
    lCombs = random.randint(0,len(lPrices),size=len(lS2))

    for sus in range(len(lS2)):       
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
    pd.DataFrame(lTreatments).to_csv('treatment.csv')
    return lTreatments,lAttList

# PAGES
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
        print(lOutcomes)


        return {
            'vOutcomes'         : lOutcomes,
            'sActivation'       : Constants.sActivation,
            'vTrigger'          : Constants.vTrigger,
            'Attr_order'        : Constants.Attr_order,
            'TablePaddingV'     : Constants.TablePaddingV,
            'TablePaddingH'     : Constants.TablePaddingH,
            'vColnames'         : Constants.vColnames,
            'vRownames'         : vRownames,
            'bRequireFS'        : Constants.bRequireFS,
            'bCheckFocus'       : Constants.bCheckFocus,
            'iTimeOut'          : Constants.iTimeOut,
            'sImagePath'        : Constants.sImagePath,
        }
    staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
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
        return {
            'StartLeft' : player.bStartLeft,
            'bRequireFS'        : Constants.bRequireFS,
            'bCheckFocus'       : Constants.bCheckFocus,
        }

class Infographics_New(Page):
    @staticmethod
    def vars_for_template(player):
        return dict(
            test_graph = Constants.test_graph
        ) 

class Ready(Page):
    pass

class Infographics(Page):

    @staticmethod
    def vars_for_template(player):
        # Define images as variables
        img1 = Constants.imgFile_Inst
        Qual = Constants.imgFile_Quality
        participant = player.participant
        
        # Pick images based on treatment for sustainability info
        if participant.treatment == 1:
            Sus = Constants.imgFile_Linear
        elif participant.treatment == 2:
            Sus = Constants.imgFile_Concave
        else:
            Sus = Constants.imgFile_Convex

        # assign presentation order of quality and sustainability      
        if participant.PresOrder == 'Qual':
            img2 = Qual
            img3 = Sus
        else:
            img2 = Sus
            img3 = Qual

        # These images will be shown in this order on Infographic(Page) slides 
        return dict(
            slide_1_img = img1,
            slide_2_img = img2,
            slide_3_img = img3,
        )
    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds/2+1

page_sequence = [Infographics_New, Ready, Decision, Between, Infographics]
