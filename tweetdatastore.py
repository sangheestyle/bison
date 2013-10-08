from twython import Twython
import time
import json
import os

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
        self.last_created_at = ""
        self.query = query
        self.set_last_query_result()

    def query_to_folder_name(self, query):
        query = query.replace("#", "_sharp_")
        query = query.replace(" ", "_")
        return query

    def write_file (self, content):
        folder_path = 'dumps/' + self.query_to_folder_name(self.query)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        current_path = os.path.abspath(os.curdir)
        os.chdir(folder_path)

        with open('tmp'+ str(self.most_early_id) + '.txt', 'w') as handle:
            json.dump(content, handle)

        os.chdir(current_path)
        handle.close()

    def get_search_result_backward (self, num_tweet , last_id = 0):
        result = self.twitter.search(q = self.query, count = num_tweet, max_id = last_id)
        for item in result['statuses']:
            self.set_last_max_id(item['id'])
            self.set_last_created_at(item['created_at'])
        return result

    def set_last_query_result (self):
        max_id_path = "dumps/" + self.query_to_folder_name(self.query) + "/max_id.txt"
        created_at_path = "dumps/" + self.query_to_folder_name(self.query) + "/created_at.txt"

        if os.path.exists(max_id_path) and os.path.exists(created_at_path):
            with open(max_id_path, 'r') as handle:
                self.set_last_max_id(int(handle.readline()))
                print self.get_max_id()
            handle.close()
            with open(created_at_path, 'r') as handle:
                self.set_last_created_at(handle.readline())
                print self.last_created_at
            handle.close()
        else:
            self.set_last_max_id(0)

    def set_last_max_id (self, max_id):
        max_id_path = "dumps/" + self.query_to_folder_name(self.query)
        if not os.path.exists(max_id_path):
            os.makedirs(max_id_path)
        current_path = os.path.abspath(os.curdir)
        os.chdir(max_id_path)
        with open("max_id.txt", 'w') as handle:
            handle.write(str(max_id))
        handle.close()
        os.chdir(current_path)
        self.most_early_id = max_id

    def get_max_id (self):
        return self.most_early_id

    def set_last_created_at (self, created_at):
        created_at_path = "dumps/" + self.query_to_folder_name(self.query)
        if not os.path.exists(created_at_path):
            os.makedirs(created_at_path)
        current_path = os.path.abspath(os.curdir)
        os.chdir(created_at_path)
        with open("created_at.txt", 'w') as handle:
            handle.write(created_at)
        handle.close()
        os.chdir(current_path)
        self.last_created_at = created_at

    def get_last_created_at (self):
        return self.last_created_at

    def show_result (self, query_result):
        for item in query_result['statuses']:
            for i in item:
                print "%s : %s" % (i, item[i])