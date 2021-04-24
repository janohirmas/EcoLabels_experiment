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
    Q1 = models.IntegerField()
    Q2 = models.StringField()
    Q3 = models.StringField()
    Q4 = models.IntegerField()

    D0 = models.StringField()
    D1 = models.StringField()
    D2 = models.StringField()

    # variables for Questionnaire
    QT1 = models.IntegerField(label=' I plan tasks carefully.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT2 = models.IntegerField(label=' I do things without thinking.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT3 = models.IntegerField(label=' I make-up my mind quickly.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT4 = models.IntegerField(label=' I am happy-go-lucky.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT5 = models.IntegerField(label=' I don’t “pay attention.”',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT6 = models.IntegerField(label=' I have “racing” thoughts.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT7 = models.IntegerField(label=' I plan trips well ahead of time.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT8 = models.IntegerField(label=' I am self controlled.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT9 = models.IntegerField(label=' I concentrate easily.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT10 = models.IntegerField(label=' I save regularly.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT11 = models.IntegerField(label=' I “squirm” at plays or lectures.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT12 = models.IntegerField(label=' I am a careful thinker.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT13 = models.IntegerField(label=' I plan for job security.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT14 = models.IntegerField(label=' I say things without thinking.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT15 = models.IntegerField(label=' I like to think about complex problems.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT16 = models.IntegerField(label=' I change jobs.', choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                                                 [4, 'Almost Always/Always']],
                               widget=widgets.RadioSelectHorizontal)
    QT17 = models.IntegerField(label=' I act “on impulse.”',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT18 = models.IntegerField(label=' I get easily bored when solving thought problems.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT19 = models.IntegerField(label=' I act on the spur of the moment.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT20 = models.IntegerField(label=' I am a steady thinker.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT21 = models.IntegerField(label=' I change residences.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT22 = models.IntegerField(label=' I buy things on impulse.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT23 = models.IntegerField(label=' I can only think about one thing at a time.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT24 = models.IntegerField(label=' I change hobbies.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT25 = models.IntegerField(label=' I spend or charge more than I earn.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT26 = models.IntegerField(label=' I often have extraneous thoughts when thinking.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT27 = models.IntegerField(label=' I am more interested in the present than the future.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT28 = models.IntegerField(label=' I am restless at the theater or lectures.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT29 = models.IntegerField(label=' I like puzzles.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT30 = models.IntegerField(label=' I am future oriented.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT_check = models.IntegerField(label='Please indicate "Often" in this question.',
                                   choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                            [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)


# PAGES
class Introduction(Page):
    pass

class Instructions(Page):
    form_model = 'player'
    form_fields = ['Q1', 'Q2', 'Q3', 'Q4']

class Demographics(Page):
    form_model = 'player'
    form_fields = ['D0', 'D1', 'D2']

class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['QT1', 'QT2', 'QT3', 'QT4', 'QT5', 'QT6', 'QT7', 'QT8', 'QT9', 'QT10', 'QT11', 'QT12', 'QT13', 'QT14', 'QT15', 'QT_check', 'QT16', 'QT17', 'QT18', 'QT19', 'QT20', 'QT21', 'QT22', 'QT23', 'QT24', 'QT25', 'QT26', 'QT27', 'QT28', 'QT29', 'QT30']

    def is_displayed(self):
        return True

class Results(Page):
    pass


page_sequence = [Demographics, Questionnaire, Introduction, Instructions, Results]


