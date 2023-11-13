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
    "アスカ":{},"あやか":{},"えりか":{},"きりこ":{},
    "すい":{}, "波留（は...":{}, "ハル":{}, "めあり":{},
    "りこ":{}, "りな":{}, "ゆっこ":{},   "ゆかり":{}, 
    }
    
    # 朝のジョブ
    start_day_shift = time(6, 0)
    start_datetime = datetime.combine(datetime.now(), start_day_shift)
    end_day_shift = time(9, 30)
    end_datetime = datetime.combine(datetime.now(), end_day_shift)
    scheduler.add_job(chara_order_fstmail.main, 'cron', hour=6, minute=0, args=[0], kwargs={'chara_name_list': chara_name_list}, misfire_grace_time=60*60)
    scheduler.add_job(scheduler.shutdown, 'date', run_date=end_datetime)
    
    # 夜のジョブ
    start_night_shift = time(17, 0)
    start_datetime = datetime.combine(datetime.now(), start_night_shift)
    end_night_shift = time(21, 30)
    end_datetime = datetime.combine(datetime.now(), end_night_shift)
    scheduler.add_job(chara_order_fstmail.main, 'cron', hour=17, minute=0, args=[0], kwargs={'chara_name_list': chara_name_list}, misfire_grace_time=60*60)
    scheduler.add_job(scheduler.shutdown, 'date', run_date=end_datetime)
    print("Press Ctrl+{0} to exit.".format('Break' if os.name == 'nt' else 'C'))
    
    try:
        scheduler.start()  # スタート
    except (KeyboardInterrupt, SystemExit):
        pass