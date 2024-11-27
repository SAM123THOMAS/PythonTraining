import win32api
import win32com.client
import win32gui

# print("windows version: ",win32api.GetVersion())
# print("Computer Nane: ", win32api.GetComputerName())
# print("System Metrics: ", win32api.GetSystemMetrics(0))


def custom_messagebox():
    result=win32gui.MessageBox(0,"Do you like Python?","Custom Question:",1)
    print(result)
    if(result==1):
        win32gui.MessageBox(0,str(result),"Your Output",1)




custom_messagebox()