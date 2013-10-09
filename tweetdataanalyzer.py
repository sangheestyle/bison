import json


class TweetDataAnalyzer:

    def __init__(self):
        pass

    def load_json_file(self, file_path):
        with open(file_path, 'r') as handle:
            loaded_data = json.load(handle)

        handle.close()
        return loaded_data

    def load_json_files(self, folder_path):
        pass
