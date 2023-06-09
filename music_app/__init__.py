from otree.api import *

doc = """
This experiment investigates the relationship between music listening and performance.
"""

class C(BaseConstants):
    NAME_IN_URL = 'music_app'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    participation_payoff = 3

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    nickname = models.StringField()
    age = models.IntegerField(min=1, max=99)
    occupation = models.StringField(label="What is your occupation?",
    choices=['Sales and Retail Workers', 'Teacher', 'Healthcare Professional', 'Administrative and Secretarial Staff', 'Customer Service Representative', 'Engineer', 'Accountant or Financial Professional', 'Hospitality and Tourism Worker', 'Construction Worker', 'Lawyers or Legal Professional', 'PhD Student', 'University Student', 'High School Student', 'Researcher or Scientist', 'Human Resources Professional', 'Marketing and Advertising Professional', 'Social Worker or Counselor', 'Security Guard', 'Agricultural Worker', 'Other', 'Unemployed', 'Retired']
    )
    hours_listening_music = models.CharField(
    choices=['Less than 1', 'Between 1 and 2', 'Between 2 and 3', 'Between 3 and 5', 'More than 5'],
    widget=widgets.RadioSelect
    )
    hours_reading = models.CharField(
    choices=['Less than 1', 'Between 1 and 2', 'Between 2 and 3', 'Between 3 and 5', 'More than 5'],
    widget=widgets.RadioSelect
    )
    hours_studying = models.CharField(
    choices=['Less than 1', 'Between 1 and 2', 'Between 2 and 3', 'Between 3 and 5', 'More than 5'],
    widget=widgets.RadioSelect
    )
    hours_physical_activity = models.CharField(
    choices=['Less than 1', 'Between 1 and 2', 'Between 2 and 3', 'Between 3 and 5', 'More than 5'],
    widget=widgets.RadioSelect
    )
    genres_most_listened = models.StringField(
    choices=['Blues', 'Classical', 'Country', 'Dance', 'Electronic', 'Folk', 'Funk', 'Gospel', 'Hip-hop', 'Indie', 'Jazz', 'Metal', 'Pop', 'Punk', 'Rock', 'R&B', 'Soul']
    )
    genres_least_listened = models.StringField(
    choices=['Blues', 'Classical', 'Country', 'Dance', 'Electronic', 'Folk', 'Funk', 'Gospel', 'Hip-hop', 'Indie', 'Jazz', 'Metal', 'Pop', 'Punk', 'Rock', 'R&B', 'Soul']
    )
    music_while_study = models.CharField(
    choices=['Very Frequently', 'Frequently', 'Occasionally', 'Rarely', 'Never'],
    widget=widgets.RadioSelect
    )
    music_while_work = models.CharField(
    choices=['Very Frequently', 'Frequently', 'Occasionally', 'Rarely', 'Never'],
    widget=widgets.RadioSelect
    )
    music_in_free_time = models.CharField(
    choices=['Very Frequently', 'Frequently', 'Occasionally', 'Rarely', 'Never'],
    widget=widgets.RadioSelect
    )
    wrong_word_silent = models.CharField(
    choices=['Waterfall', 'Spoon', 'Moon', 'Apple', 'Piano'],
    widget=widgets.RadioSelectHorizontal
    )
    wrong_word_music = models.CharField(
    choices=['Wrong', 'Nipple', 'Robot', 'Kitten', 'Violin'],
    widget=widgets.RadioSelectHorizontal
    )
    conf_silent = models.CharField(
    choices=['Very confident', 'Moderately confident', 'Slightly confident', 'Not very confident', 'Not confident at all'],
    widget=widgets.RadioSelect
    )
    conf_music = models.CharField(
    choices=['Very confident', 'Moderately confident', 'Slightly confident', 'Not very confident', 'Not confident at all'],
    widget=widgets.RadioSelect
    )
    #word_silent_check = models.CharField(initial="")
    #word_music_check = models.CharField(initial="")
    #silence_task_payoff = models.IntegerField()
    #music_task_payoff = models.IntegerField()
    #reward = models.IntegerField()
   
def set_payoff_app(player: Player):
    if player.wrong_word_silent == 'Spoon':
        player.word_silent_check = 'correct'  # Use assignment operator '=' instead of '=='
    else:
        player.word_silent_check = 'wrong'  # Use assignment operator '=' instead of '=='
    if player.wrong_word_music == 'Wrong':
        player.word_music_check = 'correct'  # Use assignment operator '=' instead of '=='
    else:
        player.word_music_check = 'wrong'  # Use assignment operator '=' instead of '=='
    if player.wrong_word_silent == 'Spoon':
        player.silence_task_payoff = 1.5  # Use assignment operator '=' instead of '=='
    else:
        player.silence_task_payoff = 0  # Use assignment operator '=' instead of '=='
    
    if player.word_music_check == "Wrong":
        player.music_task_payoff = 1.5  # Use assignment operator '=' instead of '=='
    else:
        player.music_task_payoff = 0  # Use assignment operator '=' instead of '=='
    player.payoff = player.participation_payoff + player.silence_task_payoff + player.music_task_payoff
    print(player.reward)

# Pages

class Intro(Page):
    form_model = 'player'
    form_fields = ['nickname']

class Demographic(Page):
    form_model = 'player'
    form_fields = ['age', 'occupation','hours_listening_music', 'hours_reading',
    'hours_studying', 'hours_physical_activity', 'genres_most_listened',
    'genres_least_listened', 'music_while_study', 'music_while_work',
    'music_in_free_time']

class SilenceTask_info(Page):
    pass

class SilenceTask_words(Page):
    timeout_seconds = 30
    timer_text = 'Time left to remember all words:'

class SilenceTask_question(Page):
    form_model = 'player'
    form_fields = ['wrong_word_silent']

class MusicTask_info(Page):
    pass

class MusicTask_words(Page):
    timeout_seconds = 30
    timer_text = 'Time left to remember all words:'

class MusicTask_question(Page):
    form_model = 'player'
    form_fields = ['wrong_word_music']

class PerceptionTask(Page):
    form_model = 'player'
    form_fields = ['conf_silent', 'conf_music']

class Results(Page):
    pass
    ##form_model = 'player'
    ##form_fields = ['word_silent_check', 'word_music_check', 'reward']

page_sequence = [Intro, Demographic, SilenceTask_info, SilenceTask_words, SilenceTask_question, MusicTask_info, MusicTask_words, MusicTask_question, PerceptionTask, Results]