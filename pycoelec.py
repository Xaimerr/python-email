"""
This code serves as a basis to automate sending emails. 
    
    Example usages:
        + Notify a user when a python script has been executed, and attached results/PDF/images

"""

import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from libs.info import user, psswd
from libs.html_template import html_start, html_end

def main():
    
    message(
        recipients=['example@domail.com'],
        subject="""This is the subject""",
        text="""This is the body""",
        Files=['file_to_be_attached.extension']
    )


def message(recipients, subject, text, Files):
    """
    Send an email to a certain user/users
    """

    msg = MIMEMultipart()
    msg['From'] = user
    msg['Subject'] = subject
    
    # Put the desired text in the HTML template in `html_template.py`
    html = "".join((html_start,text,html_end))
    
    # Attach parts into message container.
    msg.attach(MIMEText(html, 'html'))



    # Attach any files (PDF, images, csv...)
    if Files:
        for file in Files:
            # Open the files in binary mode.  Let the MIMEImage class automatically
            # guess the specific image type.
            with open(file, 'rb') as fp:
                att = MIMEApplication(fp.read())
                att.add_header('Content-Disposition','attachment',filename=file)
                msg.attach(att)
    
    # Send the message
    HOST = 'smtp.gmail.com'
    PORT = 465 
    
    try:
        server = smtplib.SMTP_SSL(HOST, PORT)
        server.login(user, psswd)
        for recipient in recipients:
            server.sendmail(user, recipient, msg.as_string())        
        server.close()
        print("Email successfully sent!")
    except Exception as e: print(e)


if __name__ == "__main__":
    main()
