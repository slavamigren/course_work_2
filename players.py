class Player:
    def __init__(self, name):
        self.name = name
        self.used_words = set()


    def get_used_words(self):
        '''возвращает количество угаданных слов'''
        return len(self.used_words)


    def set_used_words(self, word):
        '''добавляет новое угаданное слово'''
        self.used_words.add(word)


    def check_used_words(self, word):
        '''проверяет не было ли слово уже угадано'''
        return word in self.used_words


    def __str__(self):
        return self.name