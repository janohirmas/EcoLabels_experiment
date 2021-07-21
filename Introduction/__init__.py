from otree.api import *

doc = """
This app includes the introduction page, consent form and instructions of the experiment itself. 
"""

class Constants(BaseConstants):
    name_in_url = 'Instructions2'
    players_per_group = None
    num_rounds = 1
    ## Symbols directory
    UvA_logo = 'EcoTask/figures/UvA_logo.png'
    OTP_logo = 'EcoTask/figures/Logo_OneTreePlanted.png'
    revealed_task = 'EcoTask/figures/revealed_task_img.png'
    circled_task = 'EcoTask/figures/circled_task_img.png'
    leaf_symbol = 'EcoTask/figures/one_leaf.png'
    star_symbol = 'EcoTask/figures/one_star.png'
    ## Friendly Checks
    bRequireFS = True
    bCheckFocus = True
    ## Variables that are not fully defined yet
    MaxBonus = int(3)
    NumTrials = int(66) 
    AvgDur = "15-25"
    TreesOrg = "One Tree Planted"
    ## Slides for introduction
    SlidePath = 'Instructions/slide'
    Slides = [
        dict(
            Title = 'The Experiment',
            path=SlidePath+'1.html',
            ),
        dict(
            Title = 'Your Decisions',
            path=SlidePath+'2.html'
            ),
        dict(
            Title = 'The product characteristics',
            path=SlidePath+'3.html'
            ),
        dict(
            Title = 'Purchasing Platform',
            path=SlidePath+'4.html'
            ),
        dict(
            Title = 'The product characteristics',
            path=SlidePath+'5.html'
            ),
        dict(
            Title = 'The product characteristics',
            path=SlidePath+'6.html'
            ),
        # dict(
        #     Title = 'The product characteristics',
        #     path=SlidePath+'7.html'
        #     ),
    ]



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    iFullscreenChange   = models.IntegerField(blank=True)
    iFocusLost          = models.IntegerField(blank=True)
    dFocusLostT         = models.FloatField(blank=True)

    ProlificID          = models.StringField(initial='test')


# PAGES
class Instructions2(Page):

    @staticmethod
    def js_vars(player):
        return dict(
            bRequireFS = Constants.bRequireFS,
            bCheckFocus = Constants.bCheckFocus,
        )







page_sequence = [Instructions2]


