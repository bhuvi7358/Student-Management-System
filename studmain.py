from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
#PIL - Python Image Library

def login():
    if userentry.get()=="" and passentry.get()=="":
        messagebox.showerror("Error","Blank Not Allowed.")
    elif userentry.get()=="admin" and passentry.get()=="admin":
        messagebox.showinfo("Success",f"Welcome {userentry.get()} ")
        root.destroy()
        import sms
    else:
        messagebox.showerror("Error","Invalid Username or Password")

root=Tk()

root.geometry("1280x700")
root.title("Login")
root.resizable(False,False)
bgimage=ImageTk.PhotoImage(file='bg.jpg')
#ImageTk is only applying for jpg file.
#PhotoImage is only photo image class is sufficient
lb=Label(root,image=bgimage)
lb.place(x=0,y=0)

loginframe=Frame(root,bg='white')
loginframe.place(x=400,y=150)

logoimage=PhotoImage(file='studentlogo.png')
llogo=Label(loginframe,image=logoimage)
llogo.grid(row=0,column=0,columnspan=2,pady=10,padx=20)

userlogo=PhotoImage(file='user.png')
userlabel=Label(loginframe,image=userlogo,text="Username",compound=LEFT,font=('times new romen',15,'bold'),bg='white')
userlabel.grid(row=1,column=0,padx=20,pady=10)

passlogo=PhotoImage(file='pass.png')
passlable=Label(loginframe,image=passlogo,text="Password",compound=LEFT,font=('times new romen',15,'bold'),bg='white')
passlable.grid(row=2,column=0,padx=20,pady=10)

userentry=Entry(loginframe,bd=3)
userentry.grid(row=1,column=1,padx=20,pady=10)

passentry=Entry(loginframe,bd=3)
passentry.grid(row=2,column=1,padx=20,pady=10)

loginbt=Button(loginframe,text="Login",font=('times new romen',13,'bold'),fg="white",bg='cornflowerblue',
               cursor='hand2',width=14,command=login)
loginbt.grid(row=3,column=1,pady=10)

root.mainloop()
