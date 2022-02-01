from otree.api import *
from sqlalchemy import true
from numpy import random

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Infographics'
    players_per_group = None
    num_rounds = 1
    iRandomTreatment = 5 # Number for the treatment variable such that it randomizes between all conditions (which go from 1 to iRandomTreatment-1)
    Bonus = '5p (0.05 pounds)'
    # Image path
    sImagePath          = 'global/figures/'
    imgLeaf_symbol      = sImagePath+'one_leaf.png'
    imgStar_symbol      = sImagePath+'one_star.png'
    sPathQ_l            = sImagePath+'Infographic_graphs/qual_lin.png'
    sPathQ_cv           = sImagePath+'Infographic_graphs/qual_concave.png'
    sPathQ_cv           = sImagePath+'Infographic_graphs/qual_convex.png'
    sPathS_l            = sImagePath+'Infographic_graphs/sus_linear.png'
    sPathS_cv           = sImagePath+'Infographic_graphs/sus_concave.png'
    sPathS_cx           = sImagePath+'Infographic_graphs/sus_convex.png' 
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
    lAttrQ = dict(
        attr = 'Quality',
        attr_lower = 'quality',
        conversion = '10 points = 1 pound',
        min = '30',
        max = '60',
        explain = 'is worth 3 pounds and the best one is worth 6',
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
        graphPath   = '',
   )


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sAttrOrder          = models.StringField()
    dRTbelief           = models.FloatField(blank=true)
    dRTinfographics     = models.FloatField(blank=true)
    iTreatment          = models.IntegerField()


# FUNCTIONS 
def creating_session(subsession):
    ## SETUP FOR PARTICIPANT
    for player in subsession.get_players():
        p, session = player.participant, subsession.session
        iTreatment = session.config['iTreatment']
        if (iTreatment!=Constants.iRandomTreatment):
            player.iTreatment = iTreatment
        else:
            player.iTreatment = iTreatment = random.randint(1,Constants.iRandomTreatment-1)
        # Add path to graph to treatment dictionary
        lAttrS = Constants.lAttrS
        if (iTreatment==1):
            lAttrS['graphPath'] = Constants.sPathS_l
        elif (iTreatment==2):
            lAttrS['graphPath'] = Constants.sPathS_cv
        elif (iTreatment==3):
            lAttrS['graphPath'] = Constants.sPathS_cx
        print(lAttrS['graphPath'])
        sAttrOrder = p.sAttrOrder # (Change when ready!!)
        # sAttrOrder = random.choice(['Quality','Sustainability']) # Delete when ready
        player.sAttrOrder = p.sAttrOrder # = sAttrOrder # remove last equal when ready
        if sAttrOrder == 'Quality':
            p.lAttr  = [Constants.lAttrQ, lAttrS]
        else:
            p.lAttr  = [lAttrS, Constants.lAttrQ]



# PAGES
class Information(Page):

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            lAttr = player.participant.lAttr,
            AddInfo = dict(
                exists  = False,
                content = 'InfoMid/InfoValues.html',
            )
        )


class Belief(Page):
    form_model = 'player'
    form_fields = [
        'dRTbelief', 
    ]


    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            lAttr = player.participant.lAttr,
            AddInfo = dict(
                exists  = True,
                content = 'InfoMid/InfoValues.html',
            )
        )    

    @staticmethod
    def js_vars(player: Player):
        if (player.sAttrOrder=="Quality"):
            iMin1 = Constants.Q1l
            iMin2 = Constants.S1l
            iMax1 = Constants.Q3h
            iMax2 = Constants.S3h
        else:
            iMin2 = Constants.Q1l
            iMin1 = Constants.S1l
            iMax2 = Constants.Q3h
            iMax1 = Constants.S3h

        return dict(
            iMin1 = iMin1,
            iMin2 = iMin2,
            iMax1 = iMax1,
            iMax2 = iMax2,
            lInputs = ['dRTbelief'],
        )


class Infographics(Page):

    form_model = 'player'
    form_fields = [
        'dRTinfographics', 
    ]
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            lAttr = player.participant.lAttr,
            AddInfo = dict(
                exists  = True,
                content = 'InfoMid/InfoValues.html',
            )
        )    

    @staticmethod
    def js_vars(player: Player):
        if (player.sAttrOrder=="Quality"):
            sA1 = '3'
            sA2 = '1'
        else:
            sA1 = '1'
            sA2 = '3'

        return dict(
            sA1= sA1, 
            sA2 = sA2,
            lInputs = ['dRTinfographics'],
        )

    @staticmethod
    def is_displayed(player: Player):
        return (player.iTreatment != int(Constants.iRandomTreatment-1))


page_sequence = [Information, Belief, Infographics]
