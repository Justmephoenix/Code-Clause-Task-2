import sys
from tkinter import *
from tkinter import messagebox
import time
import datetime
import playsound
from playsound import playsound
from PIL import ImageTk,Image

root=Tk()
root.title("Alarm Clock")
root.geometry('400x300')
alarmTime=StringVar()
msgii=StringVar()

def alarm():
    a=alarmTime.get()
    AlarmTime=a
    currt=time.strftime("%H:%M")
    while AlarmTime != currt:
        currt=time.strftime("%H:%M")
    
    if AlarmTime==currt:
        msg=messagebox.showinfo('Info ','f{msgi.get()}')
        playsound('alert1.wav')



head=Label(root,text="Alarm CLock",font=('comic sans',20))
head.grid(row=0,columnspan=3)
inputt=Label(root,text="Input Time ",font=('comic snas',15))
inputt.grid(row=1,column=1)
altime=Entry(root,textvariable=alarmTime,font=('comic snas',18),width=7)
altime.grid(row=1,column=2)
msg=Label(root,text="Message",font=('comic snas',15))
msg.grid(row=2,column=1)

msginput=Entry(root,textvariable=msgii,font=('comic snas',18))
msginput.grid(row=3,column=1)

submit=Button(root,text="SUBMIT",font=('comic sans',18),command=alarm)
submit.grid(row=4,column=1)
root.mainloop()