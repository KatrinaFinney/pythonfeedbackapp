import smtplib
from email.mime.text import MIMEText

def send_mail(username, position, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '8e676d0bddb743'
    password = '38f39ebe97e30c'
    message = f"<h3>New Feedback Submission<h3><ul><li>Name: {username}</li><li>Position: {position}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'email@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Portfolio Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

    
