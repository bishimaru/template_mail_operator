import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import happymail, pcmax
import sys

name = ""
if len(sys.argv) == 2:
  name = str(sys.argv[1])



happymail.send_fst_message(name)