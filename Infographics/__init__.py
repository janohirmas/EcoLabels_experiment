from otree.api import *
import random

doc = """
This app creates the inforgraphics page with three images (instruction, sustainability, quality).
The treatment (linear(1), concave(2), convex(3)) determines which sustainability image is shown.
The order of quality and sustainability images is randomized. 
"""


class Constants(BaseConstants):
    name_in_url = 'Infographics'
    players_per_group = None
    num_rounds = 1
    
    # Image files for infographics (instructions, quality, sustainability: linear/concave/convex)
    imgFile_Inst = 'global/EcoLabels_visual/instruction.png'
    imgFile_Quality = 'global/EcoLabels_visual/quality.png'
    imgFile_Linear = 'global/EcoLabels_visual/sus_linear.png'
    imgFile_Concave = 'global/EcoLabels_visual/sus_nonlin_high.png'
    imgFile_Convex = 'global/EcoLabels_visual/sus_nonlin_low.png'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    treatment = models.StringField()
    PresOrder = models.StringField()

# Functions
def creating_session(subsession):
    # randomize to treatments
    if subsession.round_number == 1:
        for player in subsession.get_players():
            participant = player.participant
            print(participant)
            participant.treatment = random.choice([1, 2, 3])
            print(participant.treatment)
            participant.PresOrder = random.choice(['Qual', 'Sus'])
            print(participant.PresOrder)


# PAGES

class Infographics(Page):

    @staticmethod
    def vars_for_template(player):
        # Define images as variables
        img1 = Constants.imgFile_Inst
        Qual = Constants.imgFile_Quality
        participant = player.participant
        
        # Pick images based on treatment for sustainability info
        if participant.treatment == 1:
            Sus = Constants.imgFile_Linear
        elif participant.treatment == 2:
            Sus = Constants.imgFile_Concave
        else:
            Sus = Constants.imgFile_Convex

        # assign presentation order of quality and sustainability      
        if participant.PresOrder == 'Qual':
            img2 = Qual
            img3 = Sus
        else:
            img2 = Sus
            img3 = Qual

        # These images will be shown in this order on Infographic(Page) slides 
        return dict(
            slide_1_img = img1,
            slide_2_img = img2,
            slide_3_img = img3,
        )

page_sequence = [Infographics]


