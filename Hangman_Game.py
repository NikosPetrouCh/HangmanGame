# NINTH TRY

from hangman import Hangman, GameStatus
from words import Words
import random


class MainMenu:
    def __init__(self, folder):
        self.words = Words(folder)

    def show_menu(self):
        while True:
            print("Welcome to Hangman!")
            print("Main Menu:")
            print("1. Choose Dictionary from list")
            print("2. Random Choose Dictionary")
            print("3. Choose Dictionary by level")
            print("4. Exit")

            choice = input("Select an option:")
            match choice:
                case "1":
                    dictionary = self.choose_dictionary()
                    if dictionary:
                        game1 = Game(dictionary)
                        game1.play_now()
                case "2":
                    dictionary = self.words.choose_random_word_file()
                    game1 = Game(dictionary)
                    game1.play_now()
                case "3":
                    dictionary = self.choose_dictionary_by_level()
                    if dictionary:
                        game1 = Game(dictionary)
                        game1.play_now()
                case "4":
                    print ("Exiting the game. Goodbye!")
                    break
                case _:
                   print ("Invalid choice. Please try again.")

    def choose_dictionary(self):
        while True:
            print ("Dictionary Menu:")

            descriptions = self.words.get_all_descriptions()
            for i, (description,level) in enumerate(descriptions):
                print(f"{i+1}. {description}")
            print(f"{len(self.words.dictionaries) + 1}. Back to main menu")

            choice = input("Select a dictionary: ")
            choice = int(choice)

            if 1 <= choice <= len(self.words.dictionaries):
                level = descriptions[choice - 1][1]
                dictionaries = self.words.get_wordsfiles_by_level(level)
                if dictionaries:
                    return random.choice(dictionaries)
            if choice == len(self.words.dictionaries)+1:
                self.show_menu()
            else:
                print(f"Invalid input. Please enter a number between 1 and {len(self.words.dictionaries)+1}.")


    def choose_dictionary_by_level(self):

        print("\nChoose Dictionary by Level:")
        word_files_load = self.words.get_all_words_files()
        levels = {d['level'] for d in self.words.dictionaries}
        print(f"Available levels: {', '.join(map(str, sorted(levels)))}")
        print(f"Or press {len(self.words.dictionaries) + 1} to go back to the main menu")

        while True:
            try:
                level = int(input("Enter the level: "))
                if level in levels:
                    dictionaries = self.words.get_wordsfiles_by_level(level)
                    if dictionaries:
                        return random.choice(dictionaries)
                    else:
                        print(f"No dictionaries found for level {level}.")
                if level == len(self.words.dictionaries) + 1:
                    self.show_menu()
                else:
                    print("Invalid level. Please enter one of the available levels.")
            except ValueError:
                print("Invalid input. Please enter a number.")



class Game:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.hangman = Hangman(random.choice(dictionary['words']))

    def play_now(self):
        print("Are you ready to tackle the Hangman challenge? \n")
        print("Your mission: Uncover the hidden word before exhausting your attempts!")
        print("Remember, you have 6 chances to make mistakes.")
        print("Type 'exit' anytime to quit the game.")

        while self.hangman.mistakes < 6 and '_' in self.hangman.players_view:

            self.display_state()

            letter = input("Guess a letter:").lower()

            if self.exit_game(letter):
                return

            letter_sanitize = self.hangman.check_letter(letter)
            if letter_sanitize == GameStatus.THIS_IS_NOT_LETTER:
                print("This is not a letter, Try again")
                continue

            letter_logic = self.hangman.check_words_letter(letter)
            match letter_logic:
                case GameStatus.LETTER_ALREADY_USED:
                    print("You have already chosen this letter")
                    continue

                case GameStatus.LETTER_EXIST:
                    print("Good guess")

                case GameStatus.LETTER_DOES_NOT_EXIST:
                    print("Wrong guess")

                case GameStatus.WON:
                    print("Congratulations!, You found the word!")
                    break
                case GameStatus.LOST:
                    print("You lost! The word was:", self.hangman.word)
                    break

    def display_state(self):
        print(f"Word: {' '.join(self.hangman.players_view)}")
        print(f"Mistakes: {self.hangman.mistakes}/6")
        print(f"Chosen letters: {', '.join(self.hangman.chosen_letters)}")

    def exit_game(self, command):
        if command.lower() == "exit":
            print("Exiting Game!")
            return True
        return False


try:
    folder = "dictionaries"
    mymainmenu = MainMenu(folder)
    mymainmenu.show_menu()
except KeyboardInterrupt:
    print("\n Game interrupted. Exiting...")

