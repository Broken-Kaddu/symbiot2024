import smtplib
from email.message import EmailMessage


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    #sender email
    user = "input2098@gmail.com"
    password = "hjeddzqtphngqamo"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    email_alert("ALERT!!", "A PERSON HAS FALLEN PLEASE PICK HIM UP!!!!", "sinhegde05@gmail.com") #reciever email