import win32api
import win32gui
import win32con

def set_wallpaper(image_path):
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,image_path,win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE)


set_wallpaper(r"C:\Users\Administrator\Downloads\windows-xp-autumn-3840x2160-17201.jpg")