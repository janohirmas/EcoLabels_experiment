from otree.api import *
from sqlalchemy import true

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Infographics'
    players_per_group = None
    num_rounds = 1
    iRandomTreatment = 5 # Number for the treatment variable such that it randomizes between all conditions (which go from 1 to iRandomTreatment-1)
    sAttrOrder = 'Quality'
    # Image path
    sImagePath          = 'EcoTask/figures/'
    txtSustainability   = 'EcoTask/text/sustainability.html'
    txtQuality          = 'EcoTask/text/quality.html'
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
    )


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Information(Page):

    @staticmethod
    def vars_for_template(player: Player):
        if Constants.sAttrOrder == 'Quality':
            lAttr  = [Constants.lAttrQ, Constants.lAttrS]
        else:
            lAttr  = [Constants.lAttrS, Constants.lAttrQ]
        return dict(
            lAttr = lAttr,
            Info  = dict(
                path = 'InfoMid/Info.html',
                other = 'InfoMid/InfoValues.html',
            ),
            AddInfo = dict(
                exists  = true,
                content = 'InfoMid/InfoValues.html',
            )
        )


class Belief(WaitPage):
    pass    

class Infographics(Page):
    @staticmethod
    def is_displayed(player: Player):
        return (player.participant.treatment != Constants.iRandomTreatment)


page_sequence = [Information]
