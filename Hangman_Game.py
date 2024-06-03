# FIFTH TRY

# Notes

# 1. Terminology
# 2. Consistancy - using Enum
# 3. Encapsulation in hangman class. (properties)
# 4. If statementd are followed by return or continue do not take elif.
# 5. Input - sanitise -  logic.


from enum import Enum
import random


class GameStatus(Enum):
    LETTER_EXIST = 1
    LETTER_DOESNOT_EXIST = 2
    THIS_IS_NOT_LETTER = 3
    LETTER_ALREADY_USED = 4
    WON = 5
    LOST = 6
    CONTINUE = 7


class Word:
    list_with_words = ["people", "school", "family", "student", "country", "problem", "system", "program",
                       "question", "company", "government", "number", "mother", "community", "president", "minute",
                       "information", "parent", "others", "office", "health", "person", "history", "result", "change",
                       "morning", "reason", "research", "teacher", "education", "word", "business", "issue", "kind",
                       "service",
                       "friend", "father", "power", "minute", "moment", "others", "community", "information", "history",
                       "result", "change", "morning", "reason", "research", "teacher", "education", "system", "program",
                       "question", "company", "government", "number", "mother", "community", "president", "minute",
                       "information", "parent", "others", "office", "health", "person", "history", "result", "change",
                       "morning", "reason", "research", "teacher", "education", "problem", "community", "president",
                       "information",
                       "history", "result", "morning", "reason", "research", "teacher", "education", "community",
                       "president", "information", "history", "result", "morning", "research", "teacher"]

    def word_choice():
        word = random.choice(Word.list_with_words)
        return word


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
            return GameStatus.LETTER_EXIST
        else:
            self.__mistakes += 1
            return GameStatus.LETTER_DOESNOT_EXIST

    def win_or_loss(self):
        if self.__mistakes >= 6:
            return GameStatus.LOST

        if '_' not in self.__players_view:
            return GameStatus.WON
        else:
            return GameStatus.CONTINUE


class Game:
    def __init__(self, word):
        self.hangman = Hangman(word)

    def play_now(self):
        while self.hangman.mistakes < 6 and '_' in self.hangman.players_view:

            self.display_state()

            letter = input("Guess a letter:").lower()

            letter_sanitize = self.hangman.check_letter(letter)
            if letter_sanitize == GameStatus.THIS_IS_NOT_LETTER:
                print("This is not a letter, Try again")

            letter_logic = self.hangman.check_words_letter(letter)
            if letter_logic == GameStatus.LETTER_ALREADY_USED:
                print("You have already chosen this letter")

            if letter_logic == GameStatus.LETTER_EXIST:
                print("Good guess")

            if letter_logic == GameStatus.LETTER_DOESNOT_EXIST:
                print("Wrong guess")

            result = self.hangman.win_or_loss()
            if result == GameStatus.WON:
                print("Congratulations!, You found the word!")
                break
            if result == GameStatus.LOST:
                print("You lost! The word was:", self.hangman.word)
                break

    def display_state(self):
        print("Welcome to Hangman!")
        print(f"Word: {' '.join(self.hangman.players_view)}")
        print(f"Mistakes: {self.hangman.mistakes}")
        print(f"Chosen letters: {', '.join(self.hangman.chosen_letters)}")

    def input(self):
        letter = input("Guess a letter:").lower()
        if self.hangman.check_letter(letter):
            self.hangman.check_words_letter()

    def mistakes(self):
        print(f"Wrong guess! Mistakes: {self.hangman.mistakes}")

    def result(self):
        result = self.hangman.win_or_loss()
        if result:
            print(result)


word = Word.word_choice()
game1 = Game(word)
game1.play_now()
