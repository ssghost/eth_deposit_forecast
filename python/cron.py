import schedule
import time

from python.forecast import *

if __name__ == '__main__':
    schedule.every().day.at("11:00").do(forecast)

    while True:
        schedule.run_pending()
