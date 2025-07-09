import tkinter
import signal

import customtkinter
from customtkinter import *
from customtkinter import filedialog

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")
app = CTk()
app.resizable(width=False, height=False)
app.configure(fg_color='#282e2c')
app.title("Compare text files")

l1 = customtkinter.CTkLabel(master=app, text="Choose a file", font=('Century Gothic', 20))
l1.place(x=140,y=45)
frame = customtkinter.CTkFrame(master=app, width=500, height=500, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
frame.configure(bg_color='#1e3ac7', fg_color='#282e2c')

def fileUpload1():
   global readFile1
   filepath = filedialog.askopenfilename()
   file1 = open(filepath, 'r')
   buttonLabel.configure(text='Successfully uploaded 1 file')
   readFile1 = file1.readlines()

def fileUpload2():
   filepath = filedialog.askopenfilename()
   file2 = open(filepath, 'r')
   buttonLabel.configure(text='Successfully uploaded 2 files')
   readFile2 = file2.readlines()

   if readFile1 == readFile2:
       label.configure(text="Match")

   else:
       label.configure(text="Not a Match")




app.geometry("400x400")
choose = CTkLabel(master=app, text="Choose a file")
button1 = customtkinter.CTkButton(master=frame, text="Upload", command=fileUpload1)
button2 = customtkinter.CTkButton(master=frame, text="Upload", command=fileUpload2)
label = CTkLabel(master=app, text="Waiting Results", font=('Century Gothic', 30))
label.place(x=125, y=350)
button1.pack(side="left", padx=20)
buttonLabel = CTkLabel(master=app, text='No files Uploaded')
buttonLabel.place(x=125, y=250)

button2.pack(padx=20)

if __name__ == '__main__':
   app.mainloop()



