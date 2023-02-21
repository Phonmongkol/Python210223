from tkinter import *
from tkinter import ttk # theme of tk
from tkinter import messagebox

GUI = Tk() #นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล')#นี่คือชื่อโปรแกรม
GUI.geometry('500x400')#นี้คือขนาดโปรแกรม

B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
B1.pack(ipadx=20,ipady=20)


L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)
L1.pack(ipadx=80,ipady=50)
################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชี 300'
    messagebox.showinfo('เงินในบัญชี',text)


FB1 = LabelFrame(GUI,text='Money') #คล้ายกระดาน
FB1.place(x=100,y=300)

B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20,padx=30,pady=30)
################
def Button3():
    text = 'Python 101, Math'
    messagebox.showinfo('วิชาเรียนวันที่ 10-20 ก.พ.',text)


FB1 = LabelFrame(GUI,text='Money') #คล้ายกระดาน
FB1.place(x=50,y=80)

B2 = ttk.Button(FB1,text='สัปดาห์นี้เรียนวิชาไร',command=Button3)
B2.pack(ipadx=20,ipady=20,padx=30,pady=30)



GUI.mainloop()
