import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import happymail, pcmax


name = "えりか"
pcmax.send_fst_mail(name)