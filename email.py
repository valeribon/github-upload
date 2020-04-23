import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login('val.sixdegrees@gmail.com', 'intern12345!')
conn.sendmail('val.sixdegrees@gmail.com','valeribon@gmail.com', 'Subject: Testeando \n\nDear Val,\n hello')
