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

    def top_n_source(self, n):
        df_source = self.df.source
        source_counts = df_source.value_counts()[:n]
        n_source = self.text_only_source(source_counts)
        return pd.DataFrame(n_source, columns=['source', 'count'])

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
    x = Analyzer(SAMPLE_CSV_PATH)
    #print x.df
    x_tns = x.top_n_source(10)
    print x_tns