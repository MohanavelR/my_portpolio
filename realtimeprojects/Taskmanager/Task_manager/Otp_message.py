from email.message import EmailMessage
import ssl
import smtplib
import random
def Otp_generate():
  num=random.randint(1000,9999)
  return num
def Send_Email(otp,email_receiver):
 try:    
  email_sender = "taskmanager8000@gmail.com"
  email_password = 'gmuz jbuj pdne wlro'
  sub = "OTP for password reset"
  body = f"Your OTP for password reset is: {otp}"

  em = EmailMessage()
  em['From'] = email_sender
  em['To'] = email_receiver
  em['Subject'] = sub
  em.set_content(body) 
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
             smtp.login(email_sender, email_password)
             smtp.sendmail(email_sender, email_receiver, em.as_string())
  return 'Successfully send email'        
 except Exception as error:
   return str(error)          
            
