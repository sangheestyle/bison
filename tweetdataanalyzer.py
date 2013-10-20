import json, os
import pandas as pd


class TweetDataAnalyzer:

    def __init__(self):
        pass

    def load_json_file(self, file_path):
        with open(file_path, 'r') as handle:
            loaded_data = json.load(handle)

        handle.close()
        return loaded_data

    def load_json_files(self, root):
        frame = pd.DataFrame()
        for root, dirnames, filenames in os.walk(root):
            for filename in filenames:
                if not filename.endswith('.txt'):
                    continue
                try:
                    path = os.path.join(root, filename)
                    file = open(path)
                    contents = json.load(file)
                    file.close()
                    frame = frame.append(pd.DataFrame(contents['statuses']))
                except Exception, e:
                    print "Failed to make DataFrame: ", e

        return frame
