from tweetdatastore import TweetDataStore
import time

q_moto_x = TweetDataStore('moto x')
q_lg_g2 = TweetDataStore('lg g2')
q_iphone_5 = TweetDataStore('iphone 5')

loop = 1000
timer = 0

for i in range(loop):
    if timer < 10:
        timer += 1
        print "=== begin: " + str(timer)
        q_iphone_5.write_file(q_iphone_5.get_search_result(100, q_iphone_5.get_max_id()))
        print "iphone 5: " + q_iphone_5.last_created_at
        q_lg_g2.write_file(q_lg_g2.get_search_result(100, q_lg_g2.get_max_id()))
        print "lg g2   : " + q_lg_g2.last_created_at
        q_moto_x.write_file(q_moto_x.get_search_result(100, q_moto_x.get_max_id()))
        print "moto x  : " + q_moto_x.last_created_at
    else:
        print "=== waiting for 15 min"
        timer = 0
        time.sleep(60 * 15)
        print "=== finish waiting then will restart"