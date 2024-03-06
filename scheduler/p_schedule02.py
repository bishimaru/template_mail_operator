from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, time, timedelta
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import pcmax, happymail, func
import h_footprint01
import sb_h_day_shift
import s_check_mail_hp
from fst_mail_pcmax import template_multiple_fst_mail, chara_order_fstmail
from datetime import datetime, timedelta



def tick():
    print("Tick! The time is : %s'" % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()  # スケジューラを作る

    # fst_mail
    chara_name_list = {
      "はづき":{}, "めあり":{},"りこ":{},
     "りな":{}, "ゆっこ":{}, "ゆかり":{}, 
    }
    
    # 朝のジョブ
    scheduler.add_job(chara_order_fstmail.main, 'cron', hour=9, minute=20, args=[1, chara_name_list, 15, 0],  misfire_grace_time=60*60)
    # scheduler.add_job(scheduler.shutdown, 'date', run_date=end_datetime)

    # 夜のジョブ
    scheduler.add_job(chara_order_fstmail.main, 'cron', hour=17, minute=10, args=[1, chara_name_list, 21, 30], misfire_grace_time=60*60)
    print("Press Ctrl+{0} to exit.".format('Break' if os.name == 'nt' else 'C'))
    
    try:
        scheduler.start()  # スタート
    except (KeyboardInterrupt, SystemExit):
        pass