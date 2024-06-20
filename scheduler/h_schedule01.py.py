from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import pcmax, happymail, func
import sb_h_day_shift
import s_check_mail_hpj
from datetime import datetime, timedelta



def tick():
    print("Tick! The time is : %s'" % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()  # スケジューラを作る

    # サイト回し
    scheduler.add_job(sb_h_day_shift.sb_h_all_do, 'cron', hour=6, minute=0, args=[20], max_instances=1,misfire_grace_time=60*60)
    scheduler.add_job(sb_h_day_shift.sb_h_all_do, 'cron', hour=8, minute=0, args=[20], max_instances=1,misfire_grace_time=60*60)
    scheduler.add_job(sb_h_day_shift.sb_h_all_do, 'cron', hour=14, minute=0, args=[15], max_instances=1,misfire_grace_time=60*60)
    scheduler.add_job(sb_h_day_shift.sb_h_all_do, 'cron', hour=18, minute=0, args=[15], max_instances=1,misfire_grace_time=60*60)
    scheduler.add_job(sb_h_day_shift.sb_h_all_do, 'cron', hour=20, minute=0, args=[15], max_instances=1,misfire_grace_time=60*60)
    scheduler.add_job(sb_h_day_shift.sb_h_all_do, 'cron', hour=22, minute=0, args=[15], max_instances=1,misfire_grace_time=60*60)

    # scheduler.add_job(tick, 'interval', second=5)  
    print("Press Ctrl+{0} to exit.".format('Break' if os.name == 'nt' else 'C'))
    
    try:
        scheduler.start()  # スタート
    except (KeyboardInterrupt, SystemExit):
        pass