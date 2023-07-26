import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import happymail, pcmax
import sys

name = ""

user_age = "30歳"
maji_soushin = False
if len(sys.argv) == 2:
  name = str(sys.argv[1])
elif len(sys.argv) == 3:
  name = str(sys.argv[1])
  user_age = str(sys.argv[2]) + "歳"
elif len(sys.argv) == 4:
  name = str(sys.argv[1])
  user_age = str(sys.argv[2]) + "歳"
  if sys.argv[3] == str(1):
    maji_soushin = True
  elif sys.argv[3] == str(0):
    maji_soushin = False

pcmax.send_fst_mail(name, user_age, maji_soushin)
