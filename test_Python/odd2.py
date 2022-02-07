from datetime import datetime

import random
import time

odds = [1,  3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 57, 59 ]

#关键的在于三个点：次数（range）、暂停（time.sleep）、随机数（random.randint）
for i in range(5):
    right_this_time = datetime.today().minute
    if right_this_time in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")
    wait_time = random.randint(1,60)
    time.sleep(wait_time)
