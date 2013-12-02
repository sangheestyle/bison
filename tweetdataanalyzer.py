import json, os
import pandas as pd


class TweetDataAnalyzer:

    def __init__(self):
        pass

    def load_json_to_dataframe(self, file_path, fields):
        try:
            file = open(file_path)
            contents = json.load(file)
            file.close()
            data_frame = pd.DataFrame(contents['statuses'], columns=fields)
            return data_frame
        except Exception, e:
            print "Failed to make DataFrame: ", e

    def load_jsons_to_dataframe(self, root, fields):
        data_frame = pd.DataFrame()
        for root, dirnames, filenames in os.walk(root):
            for filename in filenames:
                if not filename.endswith('.txt'):
                    continue
                path = os.path.join(root, filename)
                data_frame = data_frame.append(self.load_json_to_dataframe(path, fields))
        return data_frame
