import re
import pandas as pd
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

    def top_n_source(self, n=None):
        df_source = self.df.source
        source_counts = df_source.value_counts()[:n]
        n_source = self.text_only_source(source_counts)
        return pd.DataFrame(n_source, columns=['source', 'count'])

    def top_official_twitter_apps(self):
        sources = self.top_n_source()
        platforms = sources[sources.source.str.contains('Twitter for')]
        total_count = platforms['count'].sum()
        platforms['percent'] = platforms['count'] * 100 / total_count
        return platforms

    def text_only_source(self, series):
        refined_source = []
        counts = []
        n_source = {}
        for source, count in series.iteritems():
            result = self.text_from_href(source)
            refined_source.append(result)
            counts.append(count)
        n_source['source'] = refined_source
        n_source['count'] = counts
        return n_source

    def text_from_href(self, source):
        result = re.search('>(.*)</a>', source)
        if result == None:
            result = source
        else:
            result = result.group(1)
        return result

if __name__ == "__main__":
    SAMPLE_CSV_PATH = "sample/csv/moto_x.csv"
    SAMPLE_JSON_PATH = "sample/json/moto_x.json"
    x = Analyzer(SAMPLE_JSON_PATH)
    print x.top_official_twitter_apps()