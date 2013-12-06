import json, os
import pandas as pd


class TweetDataAnalyzer:

    def __init__(self):
        self.tweet_fields = ['created_at',
                             'id',
                             'favorite_count',
                             'retweet_count',
                             'text',
                             'source',
                             'user'
                            ]
        self.user_tweet_fields = ['profile_image_url',
                                  'screen_name',
                                  'name',
                                  'time_zone',
                                  'followers_count',
                                  'friends_count'
                                  ]

    def load_json_to_dataframe(self, file_path, fields=None):
        try:
            file = open(file_path)
            contents = json.load(file)
            file.close()
            data_frame = pd.DataFrame(contents['statuses'])
            if fields == None:
                return data_frame
            elif fields != None:
                selected_field = pd.DataFrame(data_frame, columns=fields)
                return selected_field
        except Exception, e:
            print "Failed to make DataFrame: ", e

    def load_jsons_to_dataframe(self, root, fields=None):
        data_frame = pd.DataFrame()
        for root, dirnames, filenames in os.walk(root):
            for filename in filenames:
                if not filename.endswith('.txt'):
                    continue
                path = os.path.join(root, filename)
                data_frame = data_frame.append(self.load_json_to_dataframe(path, fields))
        return data_frame

    def get_user_field(self, users, field):
        new_column = []
        for user in users:
            new_column.append(user[field])
        return new_column

    def move_user_fields_to_columns(self, df, fields):
        users = df.user
        for field in fields:
            new_column_name = "user_" + field
            new_column = self.get_user_field(users, field)
            df[new_column_name] = new_column
        del df['user']

    def get_formatted_dataframe(self, root):
        df = self.load_jsons_to_dataframe(root, self.tweet_fields)
        self.move_user_fields_to_columns(df, self.user_tweet_fields)
        return df