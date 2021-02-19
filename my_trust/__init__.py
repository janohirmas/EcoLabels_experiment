from otree.api import *


doc = """
Your app description
"""
# FUNCTIONS
def sent_back_amount_choices(group):
    return currency_range(
        c(0),
        group.sent_amount * Constants.multiplication_factor,
        c(1)
    )

def set_payoffs(group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p1.payoff = Constants.endowment - group.sent_amount + group.sent_back_amount
    p2.payoff = group.sent_amount * Constants.multiplication_factor - group.sent_back_amount

# CONSTANTS

class Constants(BaseConstants):
    name_in_url = 'my_trust'
    players_per_group = 2
    num_rounds = 1

    endowment = c(10)
    multiplication_factor = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        label="How much do you want to send to participant B?"
    )
    sent_back_amount = models.CurrencyField(
        label="How much do you want to send back?"
    )

class Player(BasePlayer):
    pass

# PAGES
class Send(Page):
    form_model = 'group'
    form_fields = ['sent_amount']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1

class WaitForP1(WaitPage):
    pass

class SendBack(Page):
    form_model = 'group'
    form_fields = ['sent_back_amount']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 2

    @staticmethod
    def vars_for_template(player):
        return dict(
            tripled_amount=player.group.sent_amount * Constants.multiplication_factor
        )

class ResultsWaitPage(WaitPage):  
    after_all_players_arrive = 'set_payoffs'  

class Results(Page):
    pass


page_sequence = [
    Send,
    WaitForP1,
    SendBack,
    ResultsWaitPage,
    Results,
]
