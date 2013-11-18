from tweetdataanalyzer import TweetDataAnalyzer
import pandas as pd

tweet_fields = ['created_at',
                'id',
                'in_reply_to_status_id',
                'in_reply_to_screen_name',
                'source',
                'retweeted',
                'retweet_count',
                'favorite_count',
                'screen_name',
                'hashtags',
                'text'
                ]

x = TweetDataAnalyzer()

data_moto_x = x.load_json_files('dumps/moto_x/')
moto_x = pd.DataFrame(data_moto_x, columns=tweet_fields)
moto_x.to_csv('moto_x_raw.csv', sep='\t', encoding='utf-8')
del data_moto_x
del moto_x

data_lg_g2 = x.load_json_files('dumps/lg_g2/')
lg_g2 = pd.DataFrame(data_lg_g2, columns=tweet_fields)
lg_g2.to_csv('lg_g2_raw.csv', sep='\t', encoding='utf-8')
del data_lg_g2
del lg_g2

data_nexus_5 = x.load_json_files('dumps/nexus_5/')
nexus_5 = pd.DataFrame(data_nexus_5, columns=tweet_fields)
nexus_5.to_csv('nexus_5_raw.csv', sep='\t', encoding='utf-8')
del data_nexus_5
del nexus_5
