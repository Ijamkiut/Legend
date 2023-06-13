import tkinter

def combine():
    name1 = str(entry1.get())
    name2 = str(entry2.get())
    com = name1 + name2
    entry3.insert(0,com + '@gmail.com')

def clear():
    entry1.delete(first=0,last=30)
    entry2.delete(first=0,last=30)
    entry3.delete(first=0,last=30)

def exit():
    username.destroy()


username = tkinter.Tk()
username.title('Automatic Username')
username.minsize(height=240,width=400)

labelframe = tkinter.LabelFrame(text='Username Suggestion',width=350,height=170)
labelframe.place(x=20,y=10)

label1name = tkinter.Label(text='First Name : ',font=10)
label1name.place(x=52,y=33)
entry1 = tkinter.Entry(bd=3,width=30)
entry1.place(x=160,y=35)

label2name = tkinter.Label(text='Second Name : ',font=10)
label2name.place(x=30,y=68)
entry2 = tkinter.Entry(bd=3,width=30)
entry2.place(x=160,y=70)

label3name = tkinter.Label(text='Suggested : ',font=10)
label3name.place(x=54,y=102)
entry3 = tkinter.Entry(bd=3,width=30)
entry3.place(x=160,y=105)

buttoncom = tkinter.Button(text='Combine',command=combine,width=11)
buttoncom.place(x=160,y=132)

buttonclear = tkinter.Button(text='Clear',command=clear,width=11)
buttonclear.place(x=260,y=132)

buttonexit = tkinter.Button(text='Exit',command=exit,width=25)
buttonexit.place(x=160,y=185)

username.mainloop()