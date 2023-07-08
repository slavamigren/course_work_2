class BasicWord:
    def __init__(self, word, options):
        self.word = word
        self.options = [i for i in options]


    def __str__(self):
        return self.word.upper()


    def check_option(self, option):
        '''проверяет наличие предложенного слова в возможных'''
        return option in self.options


    def get_options_amount(self):
        '''возвращает количество возможных слов'''
        return len(self.options)