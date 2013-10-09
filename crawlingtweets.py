from tweetdatastore import TweetDataStore
import time

keywords = ['lg g2',
             'moto x',
             'iphone 5',
             'ipad',
             'surface',
             'kindlefire',
             'surface2',
             'nexus10'
             ]
data_source = {name: TweetDataStore(name) for name in keywords}

LOOP_COUNT = 1000
SLEEP_TIME = 60 * 1
TIMER = 0

for i in range(LOOP_COUNT):
    if TIMER < 10:
        TIMER += 1
        print "=== BEGIN: " + str(TIMER)
        for keyword in data_source:
            current_instance = data_source[keyword]
            current_instance.write_result(
                current_instance.get_search_result(100, 0, current_instance.get_most_early_id()))
            print "* <<: " + keyword + ": " + current_instance.last_created_at
            current_instance.write_result(
                current_instance.get_search_result(100, 1, current_instance.get_most_recent_id()))
            print "* >>: " + keyword + ": " + current_instance.last_created_at
    else:
        print "=== WAIT: waiting for " + str(SLEEP_TIME) + " sec"
        TIMER = 0
        time.sleep(SLEEP_TIME)
        print "=== WAIT: finish waiting then will restart"
