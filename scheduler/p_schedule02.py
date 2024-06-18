from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, time, timedelta
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import pcmax, happymail, func
import h_footprint01
import sb_h_day_shift
import s_check_mail_hpj
from fst_mail_pcmax import template_multiple_fst_mail, chara_order_fstmail
from datetime import datetime, timedelta



def tick():
    print("Tick! The time is : %s'" % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()  # スケジューラを作る

    # fst_mail
    chara_name_list = {
        "はづき":{},"ハル":{}, "めあり":{},
        "りこ":{}, "りな":{}, "ゆうな":{}, 
        "ゆっこ":{}, "ゆかり":{}, "わかな":{}, 
    }
    
    # 朝のジョブ
    scheduler.add_job(chara_order_fstmail.main, 'cron', hour=8, minute=50, args=[1, chara_name_list, 11, 0],  misfire_grace_time=60*60)
    # 昼のジョブ
    scheduler.add_job(chara_order_fstmail.main, 'cron', hour=14, minute=15, args=[1, chara_name_list, 15, 15], misfire_grace_time=60*60)
    # 夜のジョブ
    scheduler.add_job(chara_order_fstmail.main, 'cron', hour=18, minute=10, args=[1, chara_name_list, 22, 0], misfire_grace_time=60*60)
    print("Press Ctrl+{0} to exit.".format('Break' if os.name == 'nt' else 'C'))
    
    try:
        scheduler.start()  # スタート
    except (KeyboardInterrupt, SystemExit):
        pass