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

moto_x = x.load_jsons_to_dataframe('dumps/moto_x', tweet_fields)
moto_x.to_csv('moto_x_raw.csv', index=False, sep='\t', encoding='utf-8')

lg_g2 = x.load_jsons_to_dataframe('dumps/lg_g2', tweet_fields)
lg_g2.to_csv('lg_g2_raw.csv', index=False, sep='\t', encoding='utf-8')

nexus_5 = x.load_jsons_to_dataframe('dumps/nexus_5', tweet_fields)
nexus_5.to_csv('nexus_5_raw.csv', index=False, sep='\t', encoding='utf-8')
