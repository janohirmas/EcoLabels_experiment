from otree.api import *
import time

doc = """
This app includes the introduction page, consent form and instructions of the experiment itself. 
"""

class Constants(BaseConstants):
    name_in_url = 'Instructions'
    players_per_group = None
    num_rounds = 1
    ## Symbols directory
    UvA_logo = 'global/figures/UvA_logo.png'
    OTP_logo = 'global/figures/Logo_OneTreePlanted.png'
    revealed_task = 'global/figures/revealed_task_img.png'
    circled_task = 'global/figures/circled_task_img.png'
    leaf_symbol = 'global/figures/one_leaf.png'
    star_symbol = 'global/figures/one_star.png'
    ## Variables that are not fully defined yet
    MaxBonus = int(3)
    NumTrials = int(37) 
    AvgDur = "15-20"
    TreesOrg = "One Tree Planted"

    ## Slides for introduction
    SlidePath = 'Instructions/slide'
    SlidesIntro = [
        dict(
            Title = 'Introduction',
            path='Introduction/slide0.html',
            ),
        dict(
            Title = 'Informed Consent',
            path='Introduction/slide1.html',
            ),        
    ]
    Slides = [
        dict(
            Title = 'The Experiment',
            path=SlidePath+'0.html',
            ),
        dict(
            Title = 'Your Decisions',
            path=SlidePath+'1.html'
            ),
        dict(
            Title = 'The product characteristics',
            path=SlidePath+'2.html'
            ),
        dict(
            Title = 'Value of Labels',
            path='InfoMid/InfoValues.html'
            ),
        dict(
            Title = 'Purchasing Platform',
            path=SlidePath+'3.html'
            ),
        dict(
            Title = 'The product characteristics',
            path=SlidePath+'4.html'
            ),
        dict(
            Title = 'Is it all clear? Please answer these questions correctly to proceed:',
            path=SlidePath+'5.html'
            ),
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sTreesLocation      = models.StringField()
    bClickedLocation    = models.BooleanField()
    dPixelRatio         = models.FloatField()
    sSlideSequence      = models.StringField(blank=True)
    sSlideTime          = models.StringField(blank=True)

# PAGES
class Introduction(Page):

    @staticmethod
    def vars_for_template(player):

        return dict(
            UvA_logo = Constants.UvA_logo,
            Slides = Constants.SlidesIntro,
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        part = player.participant
        # Initialize Focus variables#        
        part.startTime          = time.time()
        part.iOutFocus          = 0
        part.iFullscreenChanges = 0
        part.dTimeOutFocus      = 0

class Calibration(Page):
    form_model = 'player'
    form_fields = [ 'dPixelRatio' ]


    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        part = player.participant
        part.dPixelRatio = player.dPixelRatio



class Instructions(Page):
    form_model = 'player'
    form_fields = [ 
        'sTreesLocation',
        'bClickedLocation',
        'sSlideSequence',
        'sSlideTime',
        ]
    
    
    @staticmethod
    def vars_for_template(player):
        return dict(
            Slides = Constants.Slides,
            lAttr = player.participant.lAttr,
    )
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        part = player.participant
        part.sTreesLocation = player.sTreesLocation

    @staticmethod
    def js_vars(player: Player):
        session = player.session
        p = player.participant
        return {
            'bRequireFS'        : session.config['bRequireFS'],
            'bCheckFocus'       : session.config['bCheckFocus'],
            'dPixelRatio'       : p.dPixelRatio,
        }


    # @staticmethod
    # def live_method(player: Player, sLoc):
    #     part = player.participant
    #     part.sTreesLocation = sLoc
    #     print(part.sTreesLocation)



page_sequence = [Introduction, Calibration, Instructions]


