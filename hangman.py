from enum import Enum

class GameStatus(Enum):
    LETTER_EXIST = 1
    LETTER_DOES_NOT_EXIST = 2
    THIS_IS_NOT_LETTER = 3
    LETTER_ALREADY_USED = 4
    WON = 5
    LOST = 6
    CONTINUE = 7
    EXITGAME = 8

class Hangman:
    def __init__(self, word):
        self.__word = word
        self.__players_view = '_' * len(word)
        self.__mistakes = 0
        self.__chosen_letters = []

    @property
    def word(self):
        return self.__word

    @property
    def players_view(self):
        return self.__players_view

    @property
    def mistakes(self):
        return self.__mistakes

    @property
    def chosen_letters(self):
        return self.__chosen_letters

    def check_letter(self, letter):
        if len(letter) != 1 or not letter.isalpha():
            return GameStatus.THIS_IS_NOT_LETTER
        return True

    def check_words_letter(self, letter):
        if letter in self.__chosen_letters:
            return GameStatus.LETTER_ALREADY_USED
        self.__chosen_letters.append(letter)

        if letter in self.__word:
            self.__players_view = [letter if letter == self.__word[i] else self.__players_view[i] for i in
                                 range(len(self.__word))]
            if '_' not in self.__players_view:
                return GameStatus.WON
            else:
                return GameStatus.CONTINUE
            return GameStatus.LETTER_EXIST
        else:
            self.__mistakes += 1
            if self.__mistakes >= 6:
                return GameStatus.LOST
            return GameStatus.LETTER_DOES_NOT_EXIST

    def exit_game(self, command):
        if command.lower() == "exit":
            return GameStatus.EXITGAME
        return GameStatus.CONTINUE



