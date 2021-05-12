from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'EcoLabels'
    players_per_group = None
    num_rounds = 1
    

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    condition = models.StringField()

    def creating_session(subsession):
    # randomize to treatments
        for player in subsession.get_players():
            player.condition = random.choice(['linear', 'nonlinear'])
            print('set player.credibility to', player.condition)


    # variables for instructions
    Q1 = models.IntegerField()
    Q2 = models.StringField()
    Q3 = models.StringField()
    Q4 = models.IntegerField()

    # Variables for Demographics
    D1 = models.StringField()
    D2 = models.StringField()
    D3 = models.StringField()
    D4 = models.StringField()
    D5 = models.StringField()
    D6 = models.StringField()
    D7 = models.StringField()

    # variables for Questionnaire
    QT1 = models.StringField()
    QT2 = models.StringField()
    QT3 = models.StringField()
    QT4 = models.StringField()
    QT5 = models.StringField()
    QT6 = models.StringField()
    QT7 = models.StringField()
    QT8 = models.StringField()
    QT9 = models.StringField()
    QT10 = models.StringField()
    QT11= models.StringField()
    QT12= models.StringField()
    QT13 = models.StringField()
    QT14 = models.StringField()
    QT15 = models.StringField()
    QT16= models.StringField()
    QT17= models.StringField()
    QT18= models.StringField()
    QT19= models.StringField()
    QT20= models.StringField()
    QT21= models.StringField()
    QT22 = models.StringField()
    QT23 = models.StringField()
    QT24= models.StringField()
    QT25 = models.StringField()
    QT26 = models.StringField()
    QT27 = models.StringField()

# PAGES
class Introduction(Page):
    pass

class Instructions(Page):
    form_model = 'player'
    form_fields = ['Q1', 'Q2', 'Q3', 'Q4']

class Infographics(Page):

    @staticmethod
    def vars_for_template(player):
        condition = 2
        quality = 'global/EcoLabels_visual/quality.png'
        cred_linear = 'global/EcoLabels_visual/sus_linear.png'
        cred_nonlinear_high = 'global/EcoLabels_visual/sus_nonlin_high.png'
        cred_nonlinear_low = 'global/EcoLabels_visual/sus_nonlin_low.png'

        import random
         
        if condition == 1:
            pick_image1 = random.choice([quality, cred_linear])
            if  pick_image1 == quality:
                pick_image2 = cred_linear
            else:
                pick_image2 = quality
        else:
            pick_nonlinear = random.choice([cred_nonlinear_high, cred_nonlinear_low])
            pick_image1 = random.choice([quality, pick_nonlinear])
            if pick_image1 == quality:
                pick_image2 = pick_nonlinear
            else:
                pick_image2 = quality

        return dict(
            slide_1_img = 'global/EcoLabels_visual/instruction.png',
            slide_2_img = pick_image1,
            slide_3_img = pick_image2,
        )



class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'QT1', 'QT2', 'QT3','QT4', 'QT5', 'QT6', 'QT7','QT8', 'QT9', 'QT10', 'QT11', 'QT12', 'QT13', 'QT14', 'QT15','QT16', 'QT17', 'QT18','QT19', 'QT20', 'QT21', 'QT22','QT23', 'QT24', 'QT25','QT26', 'QT27']

    def is_displayed(self):
        return True

class Results(Page):
    pass


page_sequence = [Instructions, Infographics, Questionnaire, Introduction, Results]


