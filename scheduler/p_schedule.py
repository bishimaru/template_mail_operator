from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import pcmax, happymail, func
import h_footprints01
import sb_h_all_do
import s_check_mail
from fst_mail_pcmax import template_multiple_fst_mail
from datetime import datetime, timedelta



def tick():
    print("Tick! The time is : %s'" % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()  # スケジューラを作る

    # fst_mail
    scheduler.add_job(template_multiple_fst_mail.main, 'cron', hour=22, minute=53, args=[False], kwargs={'chara_name_list': {"めあり":{}, "ゆうこ":{},"ハル":{}, "彩香":{}, }}, misfire_grace_time=60*60)
    
    # scheduler.add_job(tick, 'interval', second=5)  
    print("Press Ctrl+{0} to exit.".format('Break' if os.name == 'nt' else 'C'))
    
    try:
        scheduler.start()  # スタート
    except (KeyboardInterrupt, SystemExit):
        pass