import win32com.client

def create_excel_workbook(file_path):
    excel =win32com.client.Dispatch("Excel.Application")
    excel.Visible =True
    workbook=excel.Workbooks.Add()
    sheet=workbook.Sheets(1)
    sheet.Cells(1,1).Value="Rohit's excel workbook"
    sheet.Cells(2,1).Value="This is a demo"
    workbook.SaveAs(file_path)

    excel.Quit()

create_excel_workbook(r"C:\Users\Administrator\Downloads\test.xlsx")