from gtts import gTTS
from tkinter import * #import all function from tkinter
from tkinter import filedialog
import tkinter.messagebox #message box
import textract #extract files from .doc etc.
import sys
import os
root = Tk() #save file as .pyw to not open cmd window (for exe file use pyinstaller)
root.title("Text to speech by Miro 2021") #title of main window

def Browse_button():
    global directory #accesable from all functions but it should be replaced by class
    
    # Get the file location
    directory = filedialog.askopenfilename(initialdir = 'C:/Users/%s', 
                                            title = "Please select a text file file",
                                            filetypes =  (("All","*.doc *.docx .*txt"),
                                                        ("Word 97 - 2003 File ","*.doc"),
                                                        ("Word 2007","*.docx"),
                                                        ("Text file", ".txt")))
    print(directory)

def Open_and_read(): #convert button 

   global u_text_to_read

   text_to_read = textract.process(directory) #reads particular file
   u_text_to_read=str(text_to_read,'utf-8') #convert binary code to a string
   print(u_text_to_read)
   
def Create_file():   

    language = "en"
    voice = gTTS(text=u_text_to_read, lang=language, slow=False) #main command

    voice.save(filedialog.asksaveasfilename(defaultextension='.mp3',filetypes= [('audio (.mp3 file)','.mp3')]))
    
       
    
    

#GUI driver
if __name__ == "__main__":

    root.configure(background = 'light blue')
    root.geometry("380x170")
    v = StringVar()
    button1 = Button(width = 20, height = 3, text = "Text file location: ", command = Browse_button).grid(row=0, column=2)
    button2 = Button(width = 20, height = 3, text = "Convert", command = Open_and_read).grid(row=1, column=2)
    button3 = Button(width = 20, height = 3, text = "Save file as: ", command = Create_file).grid(row=2, column=2)
    
    root.mainloop() 
