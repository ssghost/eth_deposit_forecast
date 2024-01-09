import schedule
import time

from python.forecast import *

if __name__ == '__main__':
    schedule.every().month.do(train)
    schedule.every().day.do(forecast)

    while True:
        schedule.run_pending()
        time.sleep(1)