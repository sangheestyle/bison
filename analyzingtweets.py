from tweetdataanalyzer import TweetDataAnalyzer
import pandas as pd

x = TweetDataAnalyzer()
loaded_data = x.load_json_file('sample/tmp386568911145426944.txt')
print pd.DataFrame(loaded_data['statuses'])