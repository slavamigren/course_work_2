import requests
import random
from players import Player
from basic_word import BasicWord


def load_random_word(url):
    '''загружает данные с url и выдаёт один объект BasicWord'''
    data_list = requests.get(url).json()
    random.shuffle(data_list)
    return BasicWord(data_list[0]['word'], data_list[0]['subwords'])


def check_word(word, player, basic_word):
    '''проверяет слово пользователя на длинну, существование и использованность'''
    if len(word) < 3:
        return 'слишком короткое слово'
    elif not basic_word.check_option(word):
        return 'неверно'
    elif player.check_used_words(word):
        return 'уже использовано'
    else:
        return None


def get_statistic(player):
    '''возвращает строку с количеством угаданных слов'''
    return f'Игра завершена, вы угадали {player.get_used_words()} слов!'

