from twython import Twython
import json
import os
import hashlib


class TweetDataStore:
    def __init__(self, query):
        # Obtain an OAuth2 Access Token
        self.APP_KEY = '96N3B2HWhDOh5gjc3j7PMg'
        self.APP_SECRET = '9QRbarJDJVPQzP9egDKGX5XBa9UEEaN2NKGrnONKY'
        self.twitter = Twython(self.APP_KEY, self.APP_SECRET, oauth_version=2)
        self.ACCESS_TOKEN = self.twitter.obtain_access_token()
        # Use the Access Token
        self.twitter = Twython(self.APP_KEY, access_token=self.ACCESS_TOKEN)
        self.most_early_id = 0
        self.most_recent_id = 0
        self.last_created_at = ""
        self.query = query
        self.set_last_query_status()

    def query_to_folder_name(self, query):
        query = query.replace("#", "_hash_")
        query = query.replace(" ", "_")
        return query

    def write_result(self, content):
        folder_path = 'dumps/' + self.query_to_folder_name(self.query)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        current_path = os.path.abspath(os.curdir)
        os.chdir(folder_path)
        m = hashlib.sha1()
        m.update(str(content))

        with open('tmp' + m.hexdigest() + '.txt', 'w') as handle:
            json.dump(content, handle)

        os.chdir(current_path)
        handle.close()

    def get_search_result(self, num_tweet, direction, id=0):
        if direction == 0:
            result = self.twitter.search(q=self.query, count=num_tweet,
                                         max_id=id)
        elif direction == 1:
            result = self.twitter.search(q=self.query, count=num_tweet,
                                         since_id=id)
        else:
            return False

        if len(result['statuses']) != 0:
            self.set_most_recent_id(result['statuses'][0]['id'])
            for item in result['statuses']:
                self.set_most_early_id(item['id'])
                self.set_last_created_at(item['created_at'])
        return result

    def set_last_query_status(self):
        tweet_status_path = "dumps/" + self.query_to_folder_name(self.query) +\
            "/tweet_status.txt"

        if os.path.exists(tweet_status_path):
            with open(tweet_status_path, 'r') as handle:
                last_tweet_status = json.load(handle)
                self.set_last_created_at(last_tweet_status['last_created_at'])
                self.set_most_early_id(int(last_tweet_status['most_early_id']))
                self.set_most_recent_id(
                    int(last_tweet_status['most_recent_id']))
            handle.close()
        else:
            self.set_most_early_id(0)

    def set_most_early_id(self, max_id):
        if max_id < self.most_early_id or self.most_early_id == 0:
            self.most_early_id = max_id
            self.write_status()

    def set_most_recent_id(self, recent_id):
        if recent_id > self.most_recent_id or self.most_recent_id == 0:
            self.most_recent_id = recent_id
            self.write_status()

    def get_most_early_id(self):
        return self.most_early_id

    def get_most_recent_id(self):
        return self.most_recent_id

    def set_last_created_at(self, created_at):
        self.last_created_at = created_at
        self.write_status()

    def write_status(self):
        tweet_status = {'most_early_id': self.most_early_id,
                        'most_recent_id': self.most_recent_id,
                        'last_created_at': self.last_created_at}

        status_path = "dumps/" + self.query_to_folder_name(self.query)

        if not os.path.exists(status_path):
            os.makedirs(status_path)

        current_path = os.path.abspath(os.curdir)
        os.chdir(status_path)

        with open("tweet_status.txt", 'w') as handle:
            handle.write(json.dumps(tweet_status))

        os.chdir(current_path)
        handle.close()

    def get_last_created_at(self):
        return self.last_created_at

    def show_result(self, query_result):
        for item in query_result['statuses']:
            for i in item:
                print "%s : %s" % (i, item[i])
