import json, os
import pandas as pd


class TweetDataframe:

    def __init__(self, path, tweet_fields=None, user_tweet_fields=None):
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
        if os.path.isfile(path) and path.endswith('.csv'):
            input_type = 'csv'
        else:
            input_type = None

        self.path = path
        self.input_type = input_type
        self.tweet_fields = tweet_fields
        self.user_tweet_fields = user_tweet_fields
        self.df = pd.DataFrame()
        self.set_formatted_dataframe()

    def from_json(self, file_path):
        try:
            file = open(file_path)
            contents = json.load(file)
            file.close()
            statuses_df = pd.DataFrame(contents['statuses'])
            return pd.DataFrame(statuses_df, columns=self.tweet_fields)
        except Exception, e:
            print "Failed to make DataFrame: ", e

    def from_csv(self, file_path):
        try:
            file = open(file_path)
            return pd.DataFrame.from_csv(file_path, 0, '\t')
        except Exception, e:
            print "Failed to make DataFrame: ", e

    def from_files(self):
        if os.path.isfile(self.path):
            if self.path.endswith('.txt'):
                self.df = self.df.append(self.from_json(self.path))
            if self.path.endswith('.csv'):
                self.df = self.df.append(self.from_csv(self.path))
        elif os.path.isdir(self.path):
            for root, dir_names, file_names in os.walk(self.path):
                for file_name in file_names:
                    path = os.path.join(root, file_name)
                    if file_name.endswith('.txt'):
                        self.df = self.df.append(self.from_json(path))
                    if file_name.endswith('.csv'):
                        self.df = self.df.append(self.from_csv(path))

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
        self.from_files()
        if self.input_type == None:
            self.move_user_fields_to_columns()

    def to_csv(self, file_name, index=False, sep='\t', encoding='utf=8'):
        self.df.to_csv(file_name, index=index, sep=sep, encoding=encoding)

if __name__ == "__main__":
    from datetime import datetime
    DUMPS_PATH = "dumps/"
    SAMPLE_CSV_PATH = "sample/csv/"

    device_names = ['moto_x',
                    'lg_g2',
                    'nexus_5'
                   ]

    def generate_csv(device_name):
        print "=== BEGIN: " + device_name + " " + str(datetime.now())
        x = TweetDataframe(DUMPS_PATH + device_name)
        print x.df
        print "=== Procesing CSV" + " " + str(datetime.now())
        x.to_csv(device_name + '.csv')
        print "=== END: " + device_name + " " + str(datetime.now())

    dfs = {device_name: TweetDataframe(SAMPLE_CSV_PATH + device_name + ".csv")
           for device_name in device_names}