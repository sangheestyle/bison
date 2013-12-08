from tweetdataframe import TweetDataframe

class Analyzer(TweetDataframe):
    def __init__(self, path):
        TweetDataframe.__init__(self, path)

    def top_n_retweet(self, n):
        pass

    def location(self):
        pass

    def time_trend(self):
        pass

    def week_day_trend(self):
        pass

    def top_n_influencer(self, n):
        pass

    def top_n_source(self, n):
        pass

if __name__ == "__main__":
    SAMPLE_CSV_PATH = "sample/csv/moto_x.csv"
    x = Analyzer(SAMPLE_CSV_PATH)
    print x.df