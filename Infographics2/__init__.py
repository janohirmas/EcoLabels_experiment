
from otree.api import *
from numpy import random

from Infographics import Information, First, Belief

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Infographics2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    sImagePath          = 'global/figures/'
    imgLeaf_symbol      = sImagePath+'one_leaf.png'
    imgStar_symbol      = sImagePath+'one_star.png'
    sPathQ_l            = sImagePath+'Infographic_graphs/qual_lin2.png'
    sPathQ_cv           = sImagePath+'Infographic_graphs/qual_concave2.png'
    sPathQ_cx           = sImagePath+'Infographic_graphs/qual_convex2.png'
    sPathS_l            = sImagePath+'Infographic_graphs/sus_linear2.png'
    sPathS_cv           = sImagePath+'Infographic_graphs/sus_concave2.png'
    sPathS_cx           = sImagePath+'Infographic_graphs/sus_convex2.png' 
    iRandomTreatment    = 4

    lAttrQ = dict(
        attr = 'Quality',
        attr_lower = 'quality',
        conversion = '10 points = 0.5 pound',
        min = '60',
        max = '90',
        explain = 'is worth 3 pounds and the best one is worth 4.5',
        symbolName = 'stars',
        symbolPath = imgStar_symbol,
        extra = '',
        symbol1Path = sImagePath+'star_1.png',
        symbol2Path = sImagePath+'star_2.png',
        symbol3Path = sImagePath+'star_3.png',
        graphPath   = sPathQ_l,
    )
    lAttrS = dict(
        attr = 'Sustainability',
        attr_lower = 'sustainability',
        conversion = '10 points = 1 tree planted',
        min = '0',
        max = '30',
        explain = 'will plant 0 trees and the best will plant 3 trees',
        symbolName = 'leaves',
        symbolPath = imgLeaf_symbol,
        extra = '<li> The total amount of points donated to the area you selected will be rounded up, so no point will be lost. For example, 102 points will mean 11 trees planted (instead of 10). </li>',
        symbol1Path = sImagePath+'leaf_1.png',
        symbol2Path = sImagePath+'leaf_2.png',
        symbol3Path = sImagePath+'leaf_3.png',
        graphPath   = sPathS_l,
   )

# FUNCTIONS 
def creating_session(subsession):
    ## SETUP FOR PARTICIPANT
    for player in subsession.get_players():
        p, session = player.participant, subsession.session
        iTreatment = session.config['iTreatment']
        if (iTreatment!=C.iRandomTreatment):
            player.iTreatment = p.iTreatment = iTreatment 
        else:
            # player.iTreatment =  p.iTreatment = iTreatment = random.randint(1,Constants.iRandomTreatment) 
            # For the follow up we omitted the non information treatment
            player.iTreatment =  p.iTreatment = iTreatment = random.randint(1,C.iRandomTreatment)
        print('Treatment for participant: {}'.format(p.iTreatment))
        # Add path to graph to treatment dictionary
        lAttrS = C.lAttrS.copy()
        lAttrQ = C.lAttrQ.copy()
        if (player.iTreatment==2):
            lAttrS.update({'graphPath': C.sPathS_cx})
        elif (player.iTreatment==3):
            lAttrQ.update({'graphPath': C.sPathQ_cx})
        sAttrOrder = p.sAttrOrder # (Change when ready!!)
        #sAttrOrder = random.choice(['Quality','Sustainability']) # Delete when ready
        player.sAttrOrder = p.sAttrOrder  #= sAttrOrder # remove last equal when ready
        if sAttrOrder == 'Quality':
            p.lAttr  = [lAttrQ, lAttrS]
        else:
            p.lAttr  = [lAttrS, lAttrQ]
        

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sAttrOrder          = models.StringField()
    dRTbelief           = models.FloatField(blank=True)
    dRTinfographics     = models.FloatField(blank=True)
    iTreatment          = models.IntegerField()
    # Beliefs
    B01 = models.FloatField()
    B02 = models.FloatField()
    B03 = models.FloatField()
    B11 = models.FloatField()
    B12 = models.FloatField()
    B13 = models.FloatField()


# PAGES
class Infographics(Page):

    @staticmethod
    def js_vars(player: Player):
        lSolutions = ['3','1']
        if player.iTreatment ==1:
            lSolutions.extend(['15','15'])
        elif player.iTreatment ==2:
            lSolutions.extend(['15','2.5'])
        elif player.iTreatment ==3:
            lSolutions.extend(['27.5','15'])


        return dict(
            lSolutions = lSolutions
        )
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            lAttr = player.participant.lAttr
        )

page_sequence = [First, Information, Belief, Infographics ]
