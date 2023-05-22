import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import func

def send_gmail_yua_sumire():
  func.send_gmail()
  

if __name__ == '__main__':
  send_gmail_yua_sumire()