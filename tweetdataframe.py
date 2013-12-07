import json, os
import pandas as pd


class TweetDataframe:

    def __init__(self, root, tweet_fields=None, user_tweet_fields=None):
        if tweet_fields == None:
            tweet_fields = ['created_at',
                             'id',
                             'favorite_count',
                             'retweet_count',
                             'text',
                             'source',
                             'user'
                            ]
        if user_tweet_fields == None:
            user_tweet_fields = ['profile_image_url',
                                 'screen_name',
                                 'name',
                                 'time_zone',
                                 'followers_count',
                                 'friends_count'
                                ]
        self.root = root
        self.tweet_fields = tweet_fields
        self.user_tweet_fields = user_tweet_fields
        self.df = pd.DataFrame()
        self.set_formatted_dataframe()

    def from_json_file(self, file_path):
        try:
            file = open(file_path)
            contents = json.load(file)
            file.close()
            statuses_df = pd.DataFrame(contents['statuses'])
            return pd.DataFrame(statuses_df, columns=self.tweet_fields)
        except Exception, e:
            print "Failed to make DataFrame: ", e

    def from_json_files(self):
        for root, dir_names, file_names in os.walk(self.root):
            for file_name in file_names:
                if not file_name.endswith('.txt'):
                    continue
                else:
                    path = os.path.join(root, file_name)
                    self.df = self.df.append(self.from_json_file(path))

    def get_user_field(self, users, field):
        new_column = []
        for user in users:
            new_column.append(user[field])
        return new_column

    def move_user_fields_to_columns(self):
        users = self.df.user
        for user_tweet_field in self.user_tweet_fields:
            new_column_name = "user_" + user_tweet_field
            new_column = self.get_user_field(users, user_tweet_field)
            self.df[new_column_name] = new_column
        del self.df['user']

    def set_formatted_dataframe(self):
        self.from_json_files()
        self.move_user_fields_to_columns()

if __name__ == "__main__":
    tdf = TweetDataframe('dumps/moto_x')
    print tdf.df