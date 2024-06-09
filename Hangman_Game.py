# SIXTH TRY

# Notes

# 1. If statements.
# 2. Display - Welcome and loop.
# 3. Win Loss function inside the check letter
# 4. I deleted the function  def mistakes(self): from the  class - Game
# 5. Runtime, file saving, loading, menu.
# 6. Use match

# -- Choose Disctionary :  επιλογή dictionary.
# -- Random Choose dictionary:  Τυχαία επιλογή από όλα τα dictionaries.
# -- Level : Απεικόνιση των dictionaries από το αντίστοιχο level.
# -- Exit : Στο αρχικό menu το προγραμμα κάνει exit. Στη φάση επιλογής dictionary παει πισω στο αρχικό menu. Στη διάρκεια του παιχνιδιού πάει πάλι στο αρχικό menu.



from enum import Enum
import random
import json
import os



class GameStatus(Enum):
    LETTER_EXIST = 1
    LETTER_DOESNOT_EXIST = 2
    THIS_IS_NOT_LETTER = 3
    LETTER_ALREADY_USED = 4
    WON = 5
    LOST = 6
    CONTINUE = 7


class Dictionary:

    def __init__(self):
        self.dicts_folder = "dictionaries"

        # self.file_names = [
        #     "simplewords.dct",
        #     "averagewords.dct",
        #     "complicatedwords.dct",
        #     "reallycomplicatedwords.dct",
        # ]

        self.file_paths = [
            os.path.join(self.dicts_folder, p) for p in os.listdir(self.dicts_folder)
        ]
        self.dictionaries = [self.load_dict(p) for p in self.file_paths]
        self.dictionaries = sorted(self.dictionaries, key=lambda d: d['level'])
    
    def load_dict(self, path):
        with open(path) as json_data:
            d = json.load(json_data)
        return d

    # def dictionaries(self):
    #     return [
    #         self.load_dict(p) for p in self.file_paths
    #     ]
    # dictionaries = [
    #     {
    #         "filename": "<simplewords.dct>",
    #         "description": "Simple Words",
    #         "level": 1,
    #         "words": ["people", "school", "family", "student", "country", "problem", "system", "program",
    #               "question", "company", "number", "mother", "community", "parent", "others", "office",
    #               "health", "person", "word", "friend", "father", "moment", "power", "reason", "kind"]
    #     },
    #     {
    #         "filename": "<averagewords.dct>",
    #         "description": "Average Words",
    #         "level": 2,
    #         "words": ["information", "president", "service", "business", "issue", "teacher", "education",
    #               "research", "morning", "change", "history", "result", "minute"]
    #     },
    #     {
    #         "filename": "<complicatedwords.dct>",
    #         "description": "Complicated Words",
    #         "level": 3,
    #         "words": ["government", "program", "question", "complicated", "average", "difficult", "medium",
    #               "research", "challenging", "change", "education"]
    #     },
    #     {
    #         "filename": "<reallycomplicatedwords.dct>",
    #         "description": "Really Complicated Words",
    #         "level": 4,
    #         "words": ["president", "community", "complicated", "information", "government", "reason",
    #               "education", "research", "teacher", "morning", "complicated", "complex", "government",
    #               "challenging"]
    #     }
    # ]

    def get_dictionaries_by_level(self, level):
        return [d for d in self.dictionaries if d['level']==level]

    def get_all_descriptions(self):
        return [(d['description'], d['level']) for d in self.dictionaries]

    def choose_random_dictionary(self):
        return random.choice(self.dictionaries)


class MainMenu:

    def __init__(self):
        self.dictionary = Dictionary()

    def show_menu(self):
        while True:
            print("Welcome to Hangman!")
            print("Main Menu:")
            print("1. Choose Dictionary")
            print("2. Random Choose Dictionary")
            print("3. Exit")

            choice = input("Select an option:")
            match choice:
                case "1":
                    dictionary = self.choose_dictionary()
                    if dictionary:
                        game1 = Game(dictionary)
                        game1.play_now()
                case "2":
                    dictionary = self.dictionary.choose_random_dictionary()
                    game1 = Game(dictionary)
                    game1.play_now()
                case "3":
                    print ("Exiting the game. Goodbye!")
                    break
                case _:
                   print ("Invalid choice. Please try again.")

    def choose_dictionary(self):
        while True:
            print ("Dictionary Menu:")


            descriptions = self.dictionary.get_all_descriptions()
            for i, (description,level) in enumerate(descriptions):
                print(f"{i+1}.{description}(Level{level})")
            print(f"{len(self.dictionary.dictionaries) + 1}. Back to main menu")

            choice = input("Select a dictionary: ")
            choice = int(choice)

            if 1 <= choice <=4:
                level = descriptions[choice - 1][1]
                dictionaries = self.dictionary.get_dictionaries_by_level(level)
                if dictionaries:
                    return random.choice(dictionaries)
            if choice == 5:
                self.show_menu()
            else:
                print("Invalid input. Please enter a number between 1 and 5.")


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
            return GameStatus.LETTER_DOESNOT_EXIST


class Game:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.hangman = Hangman(random.choice(dictionary['words']))

    def play_now(self):
        while self.hangman.mistakes < 6 and '_' in self.hangman.players_view:

            self.display_state()

            letter = input("Guess a letter:").lower()

            letter_sanitize = self.hangman.check_letter(letter)
            if letter_sanitize == GameStatus.THIS_IS_NOT_LETTER:
                print("This is not a letter, Try again")
                continue

            letter_logic = self.hangman.check_words_letter(letter)
            if letter_logic == GameStatus.LETTER_ALREADY_USED:
                print("You have already chosen this letter")
                continue

            if letter_logic == GameStatus.LETTER_EXIST:
                print("Good guess")

            if letter_logic == GameStatus.LETTER_DOESNOT_EXIST:
                print("Wrong guess")

            if letter_logic == GameStatus.WON:
                print("Congratulations!, You found the word!")
                break
            if letter_logic == GameStatus.LOST:
                print("You lost! The word was:", self.hangman.word)
                break

    def display_state(self):
        print(f"Word: {' '.join(self.hangman.players_view)}")
        print(f"Mistakes: {self.hangman.mistakes}/6")
        print(f"Chosen letters: {', '.join(self.hangman.chosen_letters)}")

    def input(self):
        letter = input("Guess a letter:").lower()
        if self.hangman.check_letter(letter):
            self.hangman.check_words_letter()

    def result(self):
        result = self.hangman.check_words_letter()
        if result:
            print(result)

mymainmenu = MainMenu()
mymainmenu.show_menu()
