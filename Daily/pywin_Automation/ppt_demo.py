import win32com.client

def create_ppt(file_path):

    powerpoint=win32com.client.Dispatch("PowerPoint.Application")
    powerpoint.Visible=True

    #create a new Presentation
    presentation=powerpoint.Presentation.Add()
    #Add a slide (ppLayoutTitle=1)
    slide=presentation.Slides.Add(1,1)
    slide.Shapes[0].TextFrame.TextRange.Text="Automating PowerPoint"
    slide.Shapes[1].TextFrame.TextRange.Text="Using PyWin32 for Automation"

    #Save
    presentation.SaveAs(file_path)
    #powerpoint.Quit()
    print(f"Presentation saved to {file_path}")

create_ppt(r"C:\Users\Administrator\Downloads\Sample.pptx")
