from tweetdatastore import TweetDataStore
import time

x = TweetDataStore()
loop = 40
timer = 0

for i in range(loop):
    if timer < 20:
        timer += 1
        print timer
        result = x.get_search_result('lg g2', 100, x.get_max_id())
        x.write_file(result)
        print x.get_max_id()
        print x.get_last_created_at()
    else:
        timer = 0
        time.sleep(60 * 2)