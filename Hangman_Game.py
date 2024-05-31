# FOURTH TRY

from enum import Enum
import random

class GameStatus(Enum):
        LETTER_EXIST= 1
        LETTER_DOESNOT_EXIST= 2
        THIS_IS_NOT_LETTER = 3
        LETTER_ALREADY_USED= 4
        WON = 5
        LOST = 6

class Word:

    list_with_words = ["people", "school", "family", "student", "country", "problem", "system", "program",
                       "question", "company", "government", "number", "mother", "community", "president", "minute",
                       "information", "parent", "others", "office", "health", "person", "history", "result", "change",
                       "morning", "reason", "research", "teacher", "education", "word", "business", "issue", "kind", "service",
                       "friend", "father", "power", "minute", "moment", "others", "community", "information", "history",
                       "result", "change", "morning", "reason", "research", "teacher", "education", "system", "program",
                       "question", "company", "government", "number", "mother", "community", "president", "minute",
                       "information", "parent", "others", "office", "health", "person", "history", "result", "change",
                       "morning", "reason", "research", "teacher", "education", "problem", "community", "president", "information",
                       "history", "result", "morning", "reason", "research", "teacher", "education", "community",
                       "president", "information", "history", "result", "morning", "research", "teacher"]

    def word_choice():
        word = random.choice(Word.list_with_words)
        return word


class Hangman:
    def __init__(self, word):
        self.word = word
        self.players_view = '_' * len(word)
        self.mistakes = 0
        self.chosen_letters = []
        self.Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    def check_letter(self, letter):
        if len(letter) != 1 or not letter.isalpha():
            return GameStatus.THIS_IS_NOT_LETTER
        elif letter in self.chosen_letters:
            return GameStatus.LETTER_ALREADY_USED
        self.chosen_letters.append(letter)
        return True

    def check_words_letter(self, letter):
        if letter in self.word:
            self.players_view = [letter if letter == self.word[i] else self.players_view[i] for i in range(len(self.word))]
            return GameStatus.LETTER_EXIST
        else:
            self.mistakes += 1
            return GameStatus.LETTER_DOESNOT_EXIST

    def win_or_loss(self):
        if self.mistakes >= 6:
            return GameStatus.LOST
        elif '_' not in self.players_view:
            return GameStatus.WON
        else:
            None

class Game:
    def __init__(self, word):
        self.game_loop = Hangman(word)

    def play_now(self):
        while self.game_loop.mistakes < 6 and '_' in self.game_loop.players_view:
            self.display_state()
            letter = input("Guess a letter:").lower()
            letter_check = self.game_loop.check_letter(letter)
            if  letter_check == GameStatus.LETTER_ALREADY_USED:
                print("You have already chosen this letter")
                continue
            elif not letter_check:
                continue
            status = self.game_loop.check_words_letter(letter)
            if status == GameStatus.LETTER_EXIST:
               print("Good guess")
            elif status == GameStatus.LETTER_DOESNOT_EXIST:
               print("Wrong guess")
            self.display_state()
            result = self.game_loop.win_or_loss()
            if result == GameStatus.WON:
                print("Congratulations!, Yoi found the word")
                break
            elif result == GameStatus.LOST:
                print("You lost! The word was:", self.game_loop.word)
                break

    def display_state(self):
        print("Welcome to Hangman!")
        print(f"Word: {' '.join(self.game_loop.players_view)}")
        print(f"Mistakes: {self.game_loop.mistakes}")
        print(f"Chosen letters: {', '.join(self.game_loop.chosen_letters)}")

    def input(self):
        letter = input("Guess a letter:").lower()
        if self.game_loop.check_letter(letter):
            self.game_loop.check_words_letter()

    def mistakes(self):
        print(f"Wrong guess! Mistakes: {self.game_loop.mistakes}")

    def result(self):
        result = self.game_loop.win_or_loss()
        if result:
            print(result)



word = Word.word_choice()
game1 = Game(word)
game1.play_now()

