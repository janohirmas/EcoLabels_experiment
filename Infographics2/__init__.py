from otree.api import *
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
    PresentationOrder           = models.StringField(blank=True)


# FUNCTIONS
def creating_session(subsession):
    ## SETUP FOR PARTICIPANT
    if subsession.round_number == 1:
        for player in subsession.get_players():
            # Call global variables
            p = player.participant
            iT = player.session.config['iTreatment']
            #! Delete this once finished and joined
            p.dPixelRatio = 1.75
            # Determine Presentation Order
            player.PresentationOrder = random.choice(['Qual', 'Sus'])
            # Determine Treatment condition
            if (iT==Constants.iRandomTreatment):
                p.treatment = random.randint(1,Constants.iRandomTreatment) 
            else:
                p.treatment = iT

# PAGES
class Instructions(Page):
    pass


class Belief(WaitPage):
    pass


class Info(Page):

    # If the treatment is no-info (4), then the Infographics page should not be shown
    @staticmethod
    def is_displayed(player):
        return (player.participant.treatment != 4 )

    # Pass variables for FS checks and Presentation Order (quality,sustainability)
    @staticmethod
    def js_vars(player: Player):
        session = player.subsession.session
        p = player.participant
        # Pick images based on treatment for sustainability info
        if player.PresentationOrder == 'Qual':
            first, second    = Constants.Q3l, Constants.S1h
        else:
            first, second  = Constants.S3l, Constants.Q1h
        return {
            'bRequireFS'        : session.config['bRequireFS'],
            'bCheckFocus'       : session.config['bCheckFocus'],
            'dPixelRatio'       : p.dPixelRatio,
            'firstAnswer'       : str(first),
            'secondAnswer'       : str(second),
        }


    # Pass all relevant paths for figures for the template
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
            'disclaimer' : 'values will be rounded up to the next 50p',
        }
        # Pick images based on treatment for sustainability info
        if player.PresentationOrder == 'Qual':
            dicFirst, dicSecond    = dicQualityInfo, dicSustainabilityInfo
        else:
            dicFirst, dicSecond  = dicSustainabilityInfo, dicQualityInfo

        return dict(
            First = dicFirst,
            Second = dicSecond,
            Slides = Constants.Slides,
        ) 



page_sequence = [Instructions, Belief, Info]
