from tweetdataanalyzer import TweetDataAnalyzer
import pandas as pd

x = TweetDataAnalyzer()
#print x.load_json_files('sample')
#print x.load_json_files('../datacenter-for-bision/lg_g2')
data_moto_x = x.load_json_files('dumps/moto_x/')
data_lg_g2 = x.load_json_files('dumps/lg_g2/')
tweet_fields = ['created_at', 'id']

moto_x = pd.DataFrame(data_moto_x, columns=tweet_fields)
moto_x.created_at = pd.to_datetime(moto_x.created_at)
moto_x_gb = moto_x.created_at.groupby(moto_x.created_at).count()
moto_x_gbh = moto_x_gb.resample('H', how='sum')

lg_g2 = pd.DataFrame(data_lg_g2, columns=tweet_fields)
lg_g2.created_at = pd.to_datetime(lg_g2.created_at)
lg_g2_gb = lg_g2.created_at.groupby(lg_g2.created_at).count()
lg_g2_gbh = lg_g2_gb.resample('H', how='sum')

'''
total = moto_x_gbh
total['lg_g2'] = lg_g2_gbh
total.plot()
'''
