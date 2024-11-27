import win32com.client

def send_email(subject,body,to_email):
    outlook=win32com.client.Dispatch("Outlook.Application")
    mail=outlook.CreateItem(0)
    mail.Subject=subject
    mail.Body=body
    mail.Send()
send_email("Hey Sam","Hey tesing Sam","U77606@ust.com")
