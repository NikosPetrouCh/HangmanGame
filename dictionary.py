import random
import json
import os


class Words:

    REQUIRED_KEYS = {'description', 'filename', 'level', 'words'}
    LEVEL_MINIMUM = 1

    def __init__(self, folder):
        self.files_folder = folder
        self.dictionaries = []
        self.files_loaded = False

    def load_words_from_filopen(self, path):

        if not os.path.exists(path):
            raise FileNotFoundError(f"The path {path} does not exist")

        with open(path) as json_data:
            d = json.load(json_data)

        if not self.REQUIRED_KEYS.issubset(d.keys()):
            raise ValueError(f"Dictionary file {path} is missing required keys.")
        if not isinstance(d['level'], int) or d ['level'] < self.LEVEL_MINIMUM:
            raise ValueError(f"Words file {path} is not a string or has a level below the minimum required level.")
        return d


    def get_all_words_files(self):
        if self.files_loaded:
            return

        if not os.path.exists(self.files_folder):
            raise FileNotFoundError(f"The path '{self.files_folder}' does not exist.")

        if not os.path.isdir(self.files_folder):
            raise FileNotFoundError(f"The path '{self.dicts_folder}' is not a directory.")


        file_paths = [os.path.join(self.files_folder, f) for f in os.listdir(self.files_folder) if
                      f.endswith('.dct')]

        if file_paths:
            for p in file_paths:
                try:
                    self.dictionaries.append(self.load_words_from_filopen(p))
                except (FileNotFoundError, ValueError) as e:
                    pass
            self.dictionaries = [self.load_words_from_filopen(p) for p in file_paths]
            self.dictionaries = sorted(self.dictionaries, key=lambda d: d['level'])
        self.files_loaded = True
        return

    def get_wordsfiles_by_level(self, level):
        if not self.files_loaded:
            self.get_all_words_files()
        return [d for d in self.dictionaries if d['level']==level]

    def get_all_descriptions(self):
        if not self.files_loaded:
            self.get_all_words_files()
        return [(d['description'], d['level']) for d in self.dictionaries]

    def choose_random_word_file(self):
        if not self.files_loaded:
            self.get_all_words_files()
        return random.choice(self.dictionaries)


# Testing the code

# if __name__ == "__main__":
#     # w = Words("dictionaries")
#     # try:
#     #     print(w.get_all_descriptions())
#     # except Exception as e:
#     #     print(e)
#
#     # w = Words("dictionaries_does_not_exist")
#     # try:
#     #     print(w.get_all_descriptions())
#     # except Exception as e:
#     #     print(e)
#
#     # w = Words("with_error_files_decode_dictionary")
#     # try:
#     #     print(w.get_all_descriptions())
#     # except Exception as e:
#     #
#     #     print(e)
#
#     # w = Words("with_error_files_level_dictionary")
#     # try:
#     #     print(w.get_all_descriptions())
#     # except Exception as e:
#     #     print(e)
#
#     w = Words("dictionaries")
#     files_meta = w.get_all_descriptions()
#     print(files_meta)
#     for idx, value in enumerate(files_meta):
#         print(value[0], value[1])
#         w_file = os.path.join(os.curdir ,w.files_folder, w.dictionaries[idx]['filename'])
#         _words = w.load_words_from_filopen(w_file)
#         print(_words['words'])
