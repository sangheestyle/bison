import json, os
import pandas as pd


class TweetDataAnalyzer:

    def __init__(self):
        pass

    def load_json_file(self, file_path):
        try:
            file = open(file_path)
            contents = json.load(file)
            file.close()
            data_frame = pd.DataFrame(contents['statuses'])
            return data_frame
        except Exception, e:
            print "Failed to make DataFrame: ", e

    def load_json_files(self, root):
        data_frame = pd.DataFrame()
        for root, dirnames, filenames in os.walk(root):
            for filename in filenames:
                if not filename.endswith('.txt'):
                    continue
                path = os.path.join(root, filename)
                data_frame = data_frame.append(self.load_json_file(path))
        return data_frame