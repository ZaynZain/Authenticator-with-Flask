
# This is for testing the email is sending or not??
import smtplib

EMAIL_USER = 'zayn69zain@gmail.com'
EMAIL_PASS = 'scwu xqsx tgsn gmem'

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASS)
    server.sendmail(EMAIL_USER, 'bad2003547@gmail.com', 'Test email sent from Python!')
