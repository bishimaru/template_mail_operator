import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import happymail, pcmax
import sys

name = ""
user_age = ""
if len(sys.argv) == 2:
  name = str(sys.argv[1])
  user_age = "30歳"
elif len(sys.argv) == 3:
  name = str(sys.argv[1])
  user_age = str(sys.argv[2]) + "歳"

pcmax.send_fst_mail(name, user_age)