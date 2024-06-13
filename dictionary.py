import random
import json
import os

class DctChoice:

    REQUIRED_KEYS = {'description', 'filename', 'level', 'words'}
    LEVEL_MINIMUM = 1

    def __init__(self, folder):
        self.dicts_folder = folder
        self.file_paths = [os.path.join(self.dicts_folder, p) for p in os.listdir(self.dicts_folder) 
                           if p.endswith('.dct')]
        self.dictionaries = [self.load_dict(p) for p in self.file_paths]
        self.dictionaries = sorted(self.dictionaries, key=lambda d: d['level'])


    def load_dict(self, path):
        try:
            with open(path) as json_data:
                d = json.load(json_data)

            if not self.REQUIRED_KEYS.issubset(d.keys()):
                raise ValueError(f"Dictionary file {path} is missing required keys.")
            if d ['level'] < self.LEVEL_MINIMUM:
                print(f"Dictionary file {path} has a level below the minimum required level.")
            return d

        except json.JSONDecodeError:
            print(f"Error: File {path} is not a valid JSON.")
        except FileNotFoundError:
            print(f"Error: File {path} not found.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    def get_file_paths(self):
        try:
            if not os.path.exists(self.dicts_folder):
                print(f"Directory '{self.dicts_folder}' does not exist.")
            if not os.listdir(self.dicts_folder):
                print(f"Error: The folder '{self.dicts_folder}' is empty.")
                return []
            if not os.path.isdir(self.dicts_folder):
                raise FileNotFoundError(f"The path '{self.dicts_folder}' is not a directory.")

            file_paths = [os.path.join(self.dicts_folder, f) for f in os.listdir(self.dicts_folder) if
                          f.endswith('.dct')]
            if not file_paths:
                print(f"Error: No JSON files found in the folder'{self.dicts_folder}'.")
                return []
            return file_paths
        except Exception as e:
            print(f"Unexpected error: {e}")
            return[]

    def get_dictionaries_by_level(self, level):
        return [d for d in self.dictionaries if d['level']==level]

    def get_all_descriptions(self):
        return [(d['description'], d['level']) for d in self.dictionaries]

    def choose_random_dictionary(self):
        return random.choice(self.dictionaries)

