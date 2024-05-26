# Notes:

# 1. Import a hidden word.

import random
class Word:
    list_with_words = ["people", "school", "family", "student", "country", "problem", "system", "program", "question",
                           "company", "government", "number", "mother", "community", "president", "minute", "information",
                           "parent", "others", "office", "health", "person", "history", "result", "change", "morning", "reason",
                           "research", "teacher", "education", "word", "business", "issue", "kind", "service", "friend",
                           "father", "power", "minute", "moment", "others", "community", "information", "history", "result",
                           "change", "morning", "reason", "research", "teacher", "education", "system", "program", "question",
                           "company", "government", "number", "mother", "community", "president", "minute", "information",
                           "parent", "others", "office", "health", "person", "history", "result", "change", "morning", "reason",
                           "research", "teacher", "education", "problem", "community", "president", "information", "history",
                           "result", "morning", "reason", "research", "teacher", "education", "community", "president",
                           "information", "history", "result", "morning", "research", "teacher"]

    def word_choice():
        word = random.choice(Word.list_with_words)
        return word


# 2. Create a list with all the letters of the alphabet that checks which letter have used.

Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]



# 3. Create a function of the players view.
# 3.1. Print the len of the word with _.
# 3.2 If the guessing letter is in word replace it.

class Display:
    def display_word(word):
        players_view = []

        for _ in range(len(word)):
             players_view.append("_")
        players_view_str = ''.join(players_view)
        return players_view_str, players_view


# 4. Create an input for the player to guess a letter.
# 4.1 Create a method that checks if the letter is in the hidden word.
    # 4.1.1 Create a method that counts the mistakes.
    # 4.1.2 Input a letter.
    # 4.1.3 Be sure that is one letter and not anything else.
# 4.2 If the letter is in the word, replace the _ with the letter.
    # 4.2.1 If the letter is not in the word, add to the mistakes.
# 4.3 Create a method that checks if the player guess all the letters.
    # 4.3.1 If the player guess all the letters, the player win.
 # 4.4 Create a method that checks if the player lost.
    # 4.4.1 If the mistakes is more than 6, the player lose.

class Game:
    def __init__(self, word):
        self.word = word
        self.players_view_str, self.players_view = Display.display_word(word)
        self.mistakes = 0
        self.chosen_letters = []
        self.Alphabet = Alphabet

    def check_letter(self):

        while self.mistakes < 6 and ''.join(self.players_view) != self.word:
            print(f"Word: {self.players_view_str}")
            letter = input("Guess a letter:").lower()

            if len(letter) != 1 or not letter.isalpha():
                print('You should chose one letter from the alphabet')
                continue
            elif letter in self.chosen_letters:
                print('You have already chosen this letter')
                continue
            else:
                self.Alphabet.remove(letter)
                self.chosen_letters.append(letter)
                print(self.chosen_letters)

            if letter in self.word:
                for i in range (len(word)):
                    if letter == self.word[i]:
                        self.players_view[i] = letter
                self.players_view_str = ''.join(self.players_view)
                
            else:
                self.mistakes += 1
                print(f"Wrong guess! Mistakes: {self.mistakes}")

        if self.mistakes >= 6:
            print("You lost")
        else:
            print("congratulation! You guessed the word")


word = Word.word_choice()
print(word)
game = Game(word)
game.check_letter()
print(word)
