import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, message):
    # Create a MIMEText object to represent the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

# Example usage:
sender_email = 'tripathi1307shubh@gmail.com'
sender_password = 'your_password'
receiver_email = 'tripathi1307shubh@gmail.com'
subject = 'Test Email'
message = 'This is a test email sent from Python.'

send_email(sender_email, sender_password, receiver_email, subject, message)
