import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

mailaddress = 'kenta.bishi777@gmail.com'
password = 'rjdzkswuhgfvslvd'

subject = 'タイトル'
text = '本文'
address_from = 'kenta.bishi777@gmail.com'
address_to = 'bidato@wanko.be'

smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.starttls()
smtpobj.login(mailaddress, password)

msg = MIMEText(text)
msg['Subject'] = subject
msg['From'] = address_from
msg['To'] = address_to
msg['Date'] = formatdate()

smtpobj.send_message(msg)
smtpobj.close()