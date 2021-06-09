from otree.api import *

doc = """
This app includes the introduction page, consent form and instructions of the experiment itself. 
"""

class Constants(BaseConstants):
    name_in_url = 'Instructions'
    players_per_group = None
    num_rounds = 1

    leaf_symbol = 'global/EcoLabels_visual/one_leaf.png'
    star_symbol = 'global/EcoLabels_visual/one_star.png'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Terms & conditions
    TC = models.StringField()

    # Variables for instructions
    Q1 = models.IntegerField()
    Q2 = models.StringField()
    Q3 = models.StringField()

# PAGES
class Introduction(Page):
    pass

class ConsentForm(Page):
    form_model = 'player'
    form_fields = ['TC']

class Instructions(Page):
    form_model = 'player'
    form_fields = ['Q1', 'Q2', 'Q3']

    @staticmethod
    def vars_for_template(player):
        return dict(
            leaf_symbol = Constants.leaf_symbol,
            star_symbol = Constants.star_symbol,
        )


page_sequence = [Introduction, ConsentForm, Instructions]


