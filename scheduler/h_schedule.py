from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import pcmax, happymail, func
import h_footprints01
import sb_h_all_do
from datetime import datetime, timedelta



def tick():
    print("Tick! The time is : %s'" % datetime.now())

def foot_print():
    driver, wait = func.get_driver()
    h_footprints01.happymail_footprints(driver, wait)


if __name__ == '__main__':
    scheduler = BlockingScheduler()  # スケジューラを作る

    # 足跡付け
    # 現在の日時に1分を加えた日時を計算
    execute_time = datetime.now() + timedelta(minutes=1)
    # scheduler.add_job(foot_print, 'date', run_date=execute_time)

    # サイト回し
    scheduler.add_job(sb_h_all_do.sb_h_all_do, 'cron', hour=1, minute=15, args=[30])
    scheduler.add_job(sb_h_all_do.sb_h_all_do, 'cron', hour=7, minute=40, args=[20])
    scheduler.add_job(sb_h_all_do.sb_h_all_do, 'cron', hour=11, minute=0, args=[20])

    scheduler.add_job(tick, 'interval', seconds=11)  
    print(
        "Press Ctrl+{0} to exit.".format('Break' if os.name == 'nt' else 'C'))
    
    try:
        scheduler.start()  # スタート
    except (KeyboardInterrupt, SystemExit):
        pass