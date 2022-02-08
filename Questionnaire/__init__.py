from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Questionnaire'
    players_per_group = None
    num_rounds = 1
    ## Path for images
    imgFile_Quality     = '/static/global/figures/Infographic_graphs/qual_lin.png'
    imgFile_QualityCv    = '/static/global/figures/Infographic_graphs/qual_concave.png'
    imgFile_QualityCx     = '/static/global/figures/Infographic_graphs/qual_convex.png'
    imgFile_Linear      = '/static/global/figures/Infographic_graphs/sus_linear.png'
    imgFile_Concave     = '/static/global/figures/Infographic_graphs/sus_concave.png'
    imgFile_Convex      = '/static/global/figures/Infographic_graphs/sus_convex.png' 



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Variables for Demographics
    D1 = models.StringField()
    D2 = models.StringField()
    D3 = models.StringField()
    D4 = models.StringField()
    D5 = models.StringField()
    D6 = models.StringField(blank=True)
    D7 = models.StringField(blank=True)
    D8 = models.StringField()
    D9 = models.StringField()
    

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
    # QT15 = models.StringField()
    # QT16= models.StringField()
    # QT17= models.StringField()
    # QT18= models.StringField()
    # QT19= models.StringField()
    # QT20= models.StringField()
    # QT21= models.StringField()
    # QT22 = models.StringField()
    # QT23 = models.StringField()
    # QT24= models.StringField()
    # QT25 = models.StringField()
    # QT26 = models.StringField()
    # QT27 = models.StringField()

    # Validation Questions
    V1 = models.StringField()
    V2 = models.StringField()
    V3 = models.StringField()


# PAGES
class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 
    'QT1', 'QT2', 'QT3', 'QT4', 'QT5', 'QT6', 'QT7','QT8', 'QT9', 'QT10', 'QT11', 'QT12','QT13', 'QT14', 
    'V1','V2','V3']
    @staticmethod
    def js_vars(player: Player):
        return dict(
            Ql = Constants.imgFile_Quality,
            Qcv = Constants.imgFile_QualityCv,
            Qcx = Constants.imgFile_QualityCx,
            Sl = Constants.imgFile_Linear, 
            Scv = Constants.imgFile_Concave,
            Scx = Constants.imgFile_Convex,
        )

    @staticmethod
    def before_next_page(player, timeout_happened):
        # Validate questionnaire
        valid1 = int(int(player.V1)==2)
        valid2 = int(int(player.V2)==4)
        valid3 = int(int(player.V3)==1)
        player.participant.validQuestionnaire = valid1 + valid2 + valid3



page_sequence = [Questionnaire]
