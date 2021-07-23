from otree.api import *

doc = """
This app includes the introduction page, consent form and instructions of the experiment itself. 
"""

class Constants(BaseConstants):
    name_in_url = 'Instructions'
    players_per_group = None
    num_rounds = 1
    ## Symbols directory
    UvA_logo = 'EcoTask/figures/UvA_logo.png'
    OTP_logo = 'EcoTask/figures/Logo_OneTreePlanted.png'
    revealed_task = 'EcoTask/figures/revealed_task_img.png'
    circled_task = 'EcoTask/figures/circled_task_img.png'
    leaf_symbol = 'EcoTask/figures/one_leaf.png'
    star_symbol = 'EcoTask/figures/one_star.png'
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
    ProlificID          = models.StringField(initial='test')


# PAGES
class Introduction(Page):

    @staticmethod
    def vars_for_template(player):
        return dict(
            UvA_logo = Constants.UvA_logo,
        )


class ConsentForm(Page):
    pass

class Instructions(Page):
    @staticmethod
    def vars_for_template(player):
        return dict(
            OTP_logo = Constants.OTP_logo,
            revealed_task = Constants.revealed_task,
            circled_task = Constants.circled_task,
            leaf_symbol = Constants.leaf_symbol,
            star_symbol = Constants.star_symbol,
        )



page_sequence = [Introduction, ConsentForm, Instructions]


