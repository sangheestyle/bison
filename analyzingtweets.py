from tweetdataanalyzer import TweetDataAnalyzer
import pandas as pd

x = TweetDataAnalyzer()
#print x.load_json_files('sample')
#print x.load_json_files('../datacenter-for-bision/lg_g2')
data_moto_x = x.load_json_files('dumps/moto_x/')
data_lg_g2 = x.load_json_files('dumps/lg_g2/')
#data_iphone_5 = x.load_json_files('dumps/iphone_5/')
#data_kindlefire = x.load_json_files('dumps/kindlefire/')
data_nexus_5 = x.load_json_files('dumps/nexus_5/')

tweet_fields = ['created_at', 'id']

moto_x = pd.DataFrame(data_moto_x, columns=tweet_fields)
del data_moto_x
moto_x.created_at = pd.to_datetime(moto_x.created_at)
moto_x_gb = moto_x.created_at.groupby(moto_x.created_at).count()
moto_x_gbh = moto_x_gb.resample('H', how='sum')
del moto_x
del moto_x_gb

lg_g2 = pd.DataFrame(data_lg_g2, columns=tweet_fields)
del data_lg_g2
lg_g2.created_at = pd.to_datetime(lg_g2.created_at)
lg_g2_gb = lg_g2.created_at.groupby(lg_g2.created_at).count()
lg_g2_gbh = lg_g2_gb.resample('H', how='sum')
del lg_g2
del lg_g2_gb

nexus_5 = pd.DataFrame(data_nexus_5, columns=tweet_fields)
del data_nexus_5
nexus_5.created_at = pd.to_datetime(nexus_5.created_at)
nexus_5_gb = nexus_5.created_at.groupby(nexus_5.created_at).count()
nexus_5_gbh = nexus_5_gb.resample('H', how='sum')
del nexus_5
del nexus_5_gb

'''
iphone_5 = pd.DataFrame(data_iphone_5, columns=tweet_fields)
del data_iphone_5
iphone_5.created_at = pd.to_datetime(iphone_5.created_at)
iphone_5_gb = iphone_5.created_at.groupby(iphone_5.created_at).count()
iphone_5_gbh = iphone_5_gb.resample('H', how='sum')


kindlefire = pd.DataFrame(data_kindlefire, columns=tweet_fields)
kindlefire.created_at = pd.to_datetime(kindlefire.created_at)
kindlefire_gb = kindlefire.created_at.groupby(kindlefire.created_at).count()
kindlefire_gbh = kindlefire_gb.resample('H', how='sum')
'''
'''
total = moto_x_gbh
total['lg_g2'] = lg_g2_gbh
total.plot()
'''
