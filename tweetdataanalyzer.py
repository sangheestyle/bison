import json
import os

class TweetDataAnalyzer:

    def __init__(self):
        pass

    def load_json_file(self, file_path):
        with open(file_path, 'r') as handle:
            print json.load(handle)

        handle.close()

    def load_json_files(self, folder_path):
        pass
