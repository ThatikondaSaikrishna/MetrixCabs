from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

import smtplib


def send_manager_email(emp_logout,emp_name,emp_login,manager_email,name):
    from_email = "thatikondasaikrishna111@gmail.com"
    from_password = "s@iKRISHN@12345"
    to_email = manager_email

    # msg=MIMEText(message,'html')
    # msg['Subject']=subject
    # msg['To']=to_email
    # msg['From']=from_email

    msg = MIMEMultipart()
    msg['Subject'] = "Logout updated @ %s" % emp_name
    msg["From"] = from_email
    msg["To"] = to_email

    plain_text = " Testing the message "
    html_text = "<h1>Hello %s,</h1><br> <h3><font size='3px'>%s</font> has updated his logout time to <font size='5px'> %s </font> were his login time is <font size='5px'>%s</font>.<a href='https://cab-management-system.herokuapp.com/'>Click Here for details.</a> <br> <br><img src='https://cdn.dribbble.com/users/35310/screenshots/2893503/london-black-cab-glyph.png'/> <br> <h2> Kind Regards, <br> Metrixlab Inc </h2>" % (
    name.title(), emp_name.title(),emp_logout,emp_login)

    msg.attach(MIMEText(html_text, 'html'))

    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    server.sendmail(from_email, to_email, text)

    # part_1=MIMEText(plain_text,'plain')
    # part_2=MIMEText(html_text,'html')

    # the_msg.attach(part_1)
    # the_msg.attach(part_2)

    # email_conn=smtplib.SMTP('smtp.gmail.com',587)
    # email_conn.ehlo()
    # email_conn.starttls()
    # email_conn.login(from_email,from_password)
    # email_conn.sendmail(from_email,to_email,msg.as_string())
    # email_conn.quit()

