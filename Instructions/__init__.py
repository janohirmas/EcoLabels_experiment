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
    ## Friendly Checks
    bRequireFS = True
    bCheckFocus = True
    ## Variables that are not fully defined yet
    MaxBonus = int(3)
    NumTrials = int(66) 
    AvgDur = "15-25"
    TreesOrg = "One Tree Planted"

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Terms & conditions
    #! Do you need this saved? If they say no, they cannot proceed
    # TC                  = models.StringField()

    # Variables for instructions
    # Q1                  = models.IntegerField()
    # Q2                  = models.StringField()
    # Q3                  = models.StringField()

    # Fullscreen and FocusChecks 
    iFullscreenChange   = models.IntegerField(blank=True)
    iFocusLost          = models.IntegerField(blank=True)
    dFocusLostT         = models.FloatField(blank=True)


# PAGES
class Introduction(Page):

    @staticmethod
    def vars_for_template(player):
        return dict(
            UvA_logo = Constants.UvA_logo,
        )

class ConsentForm(Page):
    pass
    # form_model = 'player'
    # form_fields = ['TC']

class Instructions(Page):

    @staticmethod
    def js_vars(player):
        return dict(
            bRequireFS = Constants.bRequireFS,
            bCheckFocus = Constants.bCheckFocus,
        )

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


