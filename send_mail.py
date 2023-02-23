import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

def send_mail(fromaddr, toaddr, recipients, m_subject, m_body, m_filename, m_attachment_dir, m_smtp_server):
    # MIMEMultipart 
    msg = MIMEMultipart() 

    # senders email address 
    msg['From'] = fromaddr 

    # receivers email address 
    msg['To'] = toaddr 
    recipients = recipients

    # the subject of mail
    msg['Subject'] = m_subject

    # the body of the mail 
    body = m_body

    # attaching the body with the msg 
    msg.attach(MIMEText(m_body, 'plain')) 

    # open the file to be sent
    # rb is a flag for readonly 
    filename = m_filename
    attachment_dir = m_attachment_dir
    attachment = open(attachment_dir, "rb") 

    # MIMEBase
    attac= MIMEBase('application', 'octet-stream') 

    # To change the payload into encoded form 
    attac.set_payload((attachment).read()) 

    # encode into base64 
    encoders.encode_base64(attac) 

    attac.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

    # attach the instance 'p' to instance 'msg' 
    msg.attach(attac) 

    # creates SMTP session 
    smtp_server = m_smtp_server
    email = smtplib.SMTP(smtp_server) 

    # TLS for security 
    # email.starttls()

    # Converts the Multipart msg into a string 
    message = msg.as_string() 

    # sending the mail 
    email.sendmail(fromaddr, recipients, message)
