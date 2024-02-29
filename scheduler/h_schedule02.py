from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import pcmax, happymail, func
import sb_h_day_shift02
from datetime import datetime, timedelta



def tick():
    print("Tick! The time is : %s'" % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()  # スケジューラを作る

    # サイト回し
    scheduler.add_job(sb_h_day_shift02.sb_h_all_do, 'cron', hour=5, minute=55, args=[27], misfire_grace_time=60*60)
    scheduler.add_job(sb_h_day_shift02.sb_h_all_do, 'cron', hour=9, minute=00, args=[18], misfire_grace_time=60*60)
    scheduler.add_job(sb_h_day_shift02.sb_h_all_do, 'cron', hour=12, minute=10, args=[18], misfire_grace_time=60*60)
    scheduler.add_job(sb_h_day_shift02.sb_h_all_do, 'cron', hour=16, minute=0, args=[18], misfire_grace_time=60*60)
    scheduler.add_job(sb_h_day_shift02.sb_h_all_do, 'cron', hour=18, minute=10, args=[18], misfire_grace_time=60*60)
    scheduler.add_job(sb_h_day_shift02.sb_h_all_do, 'cron', hour=20, minute=20, args=[18], misfire_grace_time=60*60)

    # scheduler.add_job(tick, 'interval', second=5)  
    print("Press Ctrl+{0} to exit.".format('Break' if os.name == 'nt' else 'C'))
    
    try:
        scheduler.start()  # スタート
    except (KeyboardInterrupt, SystemExit):
        pass