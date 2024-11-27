import win32com.client

def read_email(namespace):
    inbox=namespace.GetDefaultFolder(6)
    messages=inbox.Items
    print(f"Total messages in Inbox: {len(messages)}")
    for i in range(min(5,len(messages))):
        message=messages[i]
        print(f"Subject: {message.Subject}")
        print(f"Sender: {message.SenderName}")
        print(f"Recieved: {message.RecievedTime}\n")
    
outlook=win32com.client.Dispatch("Outlook.Application")
namespace=outlook.GetNamespace("MAPI")
read_email(namespace)
