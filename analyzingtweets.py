from tweetdataanalyzer import TweetDataAnalyzer
import pandas as pd

tweet_fields = ['created_at', 'id']
x = TweetDataAnalyzer()

moto_x = x.load_jsons_to_dataframe('dumps/moto_x', tweet_fields)
moto_x.created_at = pd.to_datetime(moto_x.created_at)
moto_x = moto_x.created_at.groupby(moto_x.created_at).count()
moto_x = moto_x.resample('H', how='sum')

lg_g2 = x.load_jsons_to_dataframe('dumps/lg_g2', tweet_fields)
lg_g2.created_at = pd.to_datetime(lg_g2.created_at)
lg_g2 = lg_g2.created_at.groupby(lg_g2.created_at).count()
lg_g2 = lg_g2.resample('H', how='sum')

nexus_5 = x.load_jsons_to_dataframe('dumps/nexus_5', tweet_fields)
nexus_5.created_at = pd.to_datetime(nexus_5.created_at)
nexus_5 = nexus_5.created_at.groupby(nexus_5.created_at).count()
nexus_5 = nexus_5.resample('H', how='sum')