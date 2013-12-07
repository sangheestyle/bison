from tweetdataframe import TweetDataAnalyzer
import pandas as pd

x = TweetDataAnalyzer()
moto_x = x.get_formatted_dataframe('dumps/moto_x')