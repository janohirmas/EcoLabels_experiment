from genericpath import exists
from re import template
from xml.etree.ElementInclude import include
from otree.api import *
from sqlalchemy import false

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'EndBelief'
    players_per_group = None
    num_rounds = 1
    # Vars for Belief ranges
    Q1l,Q1h = 60, 70
    Q2l,Q2h = 70, 80
    Q3l,Q3h = 80, 90
    S1l, S1h = 0, 10
    S2l_l, S2h_l = 10, 20
    S2l_cv, S2h_cv = 15, 25
    S2l_cx, S2h_cx = 5, 15
    S3l, S3h  = 20, 30 
    # Paths for images
    sImagePath          = 'global/figures/'

    sPathQ_l            = sImagePath+'Infographic_graphs/qual_lin.png'
    sPathQ_cv           = sImagePath+'Infographic_graphs/qual_concave.png'
    sPathQ_cx           = sImagePath+'Infographic_graphs/qual_convex.png'
    sPathS_l            = sImagePath+'Infographic_graphs/sus_linear.png'
    sPathS_cv           = sImagePath+'Infographic_graphs/sus_concave.png'
    sPathS_cx           = sImagePath+'Infographic_graphs/sus_convex.png' 
    lS = dict(
        attr = 'Sustainability',
        graph1 = sPathS_cv,
        graph2 = sPathS_l,
        graph3 = sPathS_cx,
    )
    lQ = dict(
        attr = 'Quality',
        graph1 = sPathQ_cv,
        graph2 = sPathQ_l,
        graph3 = sPathQ_cx,
    )



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Reaction Times
    dRTbelief_end = models.FloatField()
    dRTgraph_end = models.FloatField()
    # Beliefs
    B01 = models.IntegerField()
    B02 = models.IntegerField()
    B03 = models.IntegerField()
    B11 = models.IntegerField()
    B12 = models.IntegerField()
    B13 = models.IntegerField()
    # Graph choices
    graphQuality = models.IntegerField()
    graphSustainability = models.IntegerField()



# PAGES
class Belief(Page):
    template_name = 'InfoMid/Belief.html'
    form_model = 'player'
    form_fields = [
        'dRTbelief_end', 'B01','B02','B03','B11','B12','B13'
    ]


    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            lAttr = player.participant.lAttr,
            AddInfo = dict(
                exists  = True,
                content = 'InfoMid/InfoValues.html',
            ),
            IntroBelief = 'You are almost finished. Before we continue, we would like to ask you again about the ratings',
            BonusText = '',
        )    

    @staticmethod
    def js_vars(player: Player):
        if (player.participant.sAttrOrder=="Quality"):
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
            lInputs = ['dRTbelief_end','B01','B02','B03','B11','B12','B13'],
            RTvar = 'dRTbelief_end',
        )




class Shapes(Page):
    form_model = 'player'
    form_fields = ['dRTgraph_end','graphQuality','graphSustainability']

    @staticmethod
    def vars_for_template(player: Player):
        if (player.participant.sAttrOrder == 'Quality'):
            lAttr = [Constants.lQ,Constants.lS]
        else:
            lAttr = [Constants.lQ,Constants.lS]

        return dict(
            lAttr = lAttr,
            AddInfo = dict(content='Instructions/slide3.html'),
        )

    @staticmethod
    def js_vars(player: Player):
        if (player.participant.sAttrOrder=="Quality"):
            sA1 = '3'
            sA2 = '1'
        else:
            sA1 = '1'
            sA2 = '3'

        return dict(
            sA1= sA1, 
            sA2 = sA2,
            lInputs = ['dRTgraph_end','graphQuality','graphSustainability'],
        )
    
    @staticmethod
    def is_displayed(player: Player):
        return (player.participant.iTreatment  != 4)

class First(Page):
    pass

page_sequence = [First,Belief, Shapes]
