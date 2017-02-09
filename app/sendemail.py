import smtplib
#def send_email(from_name, from_email, from_subject, from_message):
 

from_addr = "winston13lindsay@gmail.com"
to_addr = "winston13lindsay@gmail.com"
from_name = "Winston"
to_name = "Winston"
subject = "Sub"  
msg = "Info3180"
message = """From: {} <{}>
        To: {} <{}>
        
        Subject: {}
        {}
        """
message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)
        
        # Credentials (if needed)
username = 'winston13lindsay@@gmail.com'
password = 'dayxfnyfhmtprxai'
        # The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()
    
    #password - dayxfnyfhmtprxai