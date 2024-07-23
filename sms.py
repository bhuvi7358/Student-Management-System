from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas
#functionlity part
def iexit():
    result=messagebox.askyesno('confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studenttable.get_children()
    newlist=[]
    for index in indexing:
        content=studenttable.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table=pandas.DataFrame(newlist,columns=['Id','Name','D.O.B','Address','Gender','Mobile No.','E-Mail','Blood Group','Date','Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved successfully.')


def update_student():
    def update_data():
        query='update student set name=%s,dob=%s,address=%s,gender=%s,mobileno=%s,email=%s,blood=%s,date=%s,time=%s where id=%s'
        mycon.execute(query,(nameentry1.get(),dobentry.get(),addressentry.get(),genderentry.get(),mobilenoentry.get(),emailentry.get(),bloodentry.get(),date,time1,identry.get()))
        con.commit()
        messagebox.showinfo('Success',f'Id {identry.get()} is updated successfully.',parent=updatewindow)
        updatewindow.destroy()
        show_student()
    updatewindow=Toplevel()
    updatewindow.resizable(0,0)
    updatewindow.grab_set()
    #addwindow.geometry('300x400')
    updatewindow.title('Update Student')
    idlabel=Label(updatewindow,text='ID',font=('arial',13,'bold'))
    idlabel.grid(row=0,column=0,padx=10,sticky=W)
    identry=Entry(updatewindow,font=('arial',12))
    identry.grid(row=0,column=1,padx=10,pady=20)

    namelabel=Label(updatewindow,text='Name',font=('arial',13,'bold'))
    namelabel.grid(row=1,column=0,padx=5,sticky=W)
    nameentry1=Entry(updatewindow,font=('arial',12))
    nameentry1.grid(row=1,column=1,padx=10,pady=20)

    doblabel=Label(updatewindow,text='D.O.B',font=('arial',13,'bold'))
    doblabel.grid(row=2,column=0,padx=5,sticky=W)
    dobentry=Entry(updatewindow,font=('arial',12))
    dobentry.grid(row=2,column=1,padx=10,pady=20)

    genderlabel=Label(updatewindow,text='Gender',font=('arial',13,'bold'))
    genderlabel.grid(row=3,column=0,padx=5,sticky=W)
    genderentry=Entry(updatewindow,font=('arial',12))
    genderentry.grid(row=3,column=1,padx=10,pady=20)

    mobilenolabel=Label(updatewindow,text='Mobile No.',font=('arial',13,'bold'))
    mobilenolabel.grid(row=4,column=0,padx=5,sticky=W)
    mobilenoentry=Entry(updatewindow,font=('arial',12))
    mobilenoentry.grid(row=4,column=1,padx=10,pady=20)

    emaillabel=Label(updatewindow,text='E-Mail',font=('arial',13,'bold'))
    emaillabel.grid(row=5,column=0,padx=5,sticky=W)
    emailentry=Entry(updatewindow,font=('arial',12))
    emailentry.grid(row=5,column=1,padx=10,pady=20)

    bloodlabel=Label(updatewindow,text='Blood Group',font=('arial',13,'bold'))
    bloodlabel.grid(row=6,column=0,padx=5,sticky=W)
    bloodentry=Entry(updatewindow,font=('arial',12))
    bloodentry.grid(row=6,column=1,padx=10,pady=20)

    addresslabel=Label(updatewindow,text='Address',font=('arial',13,'bold'))
    addresslabel.grid(row=7,column=0,padx=5,sticky=W)
    addressentry=Entry(updatewindow,font=('arial',12))
    addressentry.grid(row=7,column=1,padx=10,pady=20)

    update_student_bt=ttk.Button(updatewindow,text='Update',command=update_data)
    update_student_bt.grid(row=8,columnspan=2)

    indexing=studenttable.focus()
    content=studenttable.item(indexing)
    #print(content)
    listdata=content['values']
    identry.insert(0,listdata[0])
    nameentry1.insert(0,listdata[1])
    dobentry.insert(0,listdata[2])
    addressentry.insert(0,listdata[3])
    genderentry.insert(0,listdata[4])
    mobilenoentry.insert(0,listdata[5])
    emailentry.insert(0,listdata[6])
    bloodentry.insert(0,listdata[7])


def show_student():
    query='select * from student'
    mycon.execute(query)
    fetched_data=mycon.fetchall()
    studenttable.delete(*studenttable.get_children())
    for data in fetched_data:
        studenttable.insert('',END,values=data)

def delete_student():
    indexing=studenttable.focus()
    content=studenttable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycon.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted successfully.')
    query='select * from student'
    mycon.execute(query)
    fetched_data=mycon.fetchall()
    studenttable.delete(*studenttable.get_children())
    for data in fetched_data:
        studenttable.insert('',END,values=data)


def search_student():
    def search_data():
        query='select * from student where id=%s or name=%s or dob=%s or gender=%s or mobileno=%s or email=%s or blood=%s or address=%s'
        mycon.execute(query,(identry.get(),nameentry1.get(),dobentry.get(),genderentry.get(),mobilenoentry.get(),emailentry.get(),bloodentry.get(),addressentry.get()))
        studenttable.delete(*studenttable.get_children())
        fetced_data=mycon.fetchall()
        for data in fetced_data:
            studenttable.insert('',END,values=data)


    searchwindow=Toplevel()
    searchwindow.resizable(0,0)
    searchwindow.grab_set()
    #addwindow.geometry('300x400')
    searchwindow.title('Add Student')
    idlabel=Label(searchwindow,text='ID',font=('arial',13,'bold'))
    idlabel.grid(row=0,column=0,padx=10,sticky=W)
    identry=Entry(searchwindow,font=('arial',12))
    identry.grid(row=0,column=1,padx=10,pady=20)

    namelabel=Label(searchwindow,text='Name',font=('arial',13,'bold'))
    namelabel.grid(row=1,column=0,padx=5,sticky=W)
    nameentry1=Entry(searchwindow,font=('arial',12))
    nameentry1.grid(row=1,column=1,padx=10,pady=20)

    doblabel=Label(searchwindow,text='D.O.B',font=('arial',13,'bold'))
    doblabel.grid(row=2,column=0,padx=5,sticky=W)
    dobentry=Entry(searchwindow,font=('arial',12))
    dobentry.grid(row=2,column=1,padx=10,pady=20)

    genderlabel=Label(searchwindow,text='Gender',font=('arial',13,'bold'))
    genderlabel.grid(row=3,column=0,padx=5,sticky=W)
    genderentry=Entry(searchwindow,font=('arial',12))
    genderentry.grid(row=3,column=1,padx=10,pady=20)

    mobilenolabel=Label(searchwindow,text='Mobile No.',font=('arial',13,'bold'))
    mobilenolabel.grid(row=4,column=0,padx=5,sticky=W)
    mobilenoentry=Entry(searchwindow,font=('arial',12))
    mobilenoentry.grid(row=4,column=1,padx=10,pady=20)

    emaillabel=Label(searchwindow,text='E-Mail',font=('arial',13,'bold'))
    emaillabel.grid(row=5,column=0,padx=5,sticky=W)
    emailentry=Entry(searchwindow,font=('arial',12))
    emailentry.grid(row=5,column=1,padx=10,pady=20)

    bloodlabel=Label(searchwindow,text='Blood Group',font=('arial',13,'bold'))
    bloodlabel.grid(row=6,column=0,padx=5,sticky=W)
    bloodentry=Entry(searchwindow,font=('arial',12))
    bloodentry.grid(row=6,column=1,padx=10,pady=20)

    addresslabel=Label(searchwindow,text='Address',font=('arial',13,'bold'))
    addresslabel.grid(row=7,column=0,padx=5,sticky=W)
    addressentry=Entry(searchwindow,font=('arial',12))
    addressentry.grid(row=7,column=1,padx=10,pady=20)

    search_student_bt=ttk.Button(searchwindow,text='Search',command=search_data)
    search_student_bt.grid(row=8,columnspan=2)

def add_student():
    def add_data():
        if identry.get()=='' or nameentry1.get()=='' or dobentry.get()=='' or genderentry.get()=='' or mobilenoentry.get()=='' or emailentry.get()=='' or bloodentry.get()=='' or addressentry.get()=='':
            messagebox.showerror("Error","All Fields not Filled",parent=addwindow)
        else:
            try:
                query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycon.execute(query,(identry.get(),nameentry1.get(),dobentry.get(),addressentry.get(),genderentry.get(),mobilenoentry.get(),emailentry.get(),bloodentry.get(),date,time1))
                con.commit()
                result=messagebox.askyesno("Confirm","Data added successfully. Do you want to clear the form?",parent=addwindow)
                if result:
                    identry.delete(0,END)
                    nameentry1.delete(0,END)
                    mobilenoentry.delete(0,END)
                    genderentry.delete(0,END)
                    dobentry.delete(0,END)
                    addressentry.delete(0,END)
                    emailentry.delete(0,END)
                    bloodentry.delete(0,END)
                else:
                    pass
            except:
                messagebox.showerror('Error','Id cannot repeated',parent=addwindow)
                return

            query='select * from student'
            mycon.execute(query)
            fetced_data=mycon.fetchall()
            studenttable.delete(*studenttable.get_children())
            for data in fetced_data:
                datalist=list(data)
                studenttable.insert('',END,values=datalist)
    addwindow=Toplevel()
    addwindow.resizable(0,0)
    addwindow.grab_set()
    #addwindow.geometry('300x400')
    addwindow.title('Add Student')
    idlabel=Label(addwindow,text='ID',font=('arial',13,'bold'))
    idlabel.grid(row=0,column=0,padx=10,sticky=W)
    identry=Entry(addwindow,font=('arial',12))
    identry.grid(row=0,column=1,padx=10,pady=20)

    namelabel=Label(addwindow,text='Name',font=('arial',13,'bold'))
    namelabel.grid(row=1,column=0,padx=5,sticky=W)
    nameentry1=Entry(addwindow,font=('arial',12))
    nameentry1.grid(row=1,column=1,padx=10,pady=20)

    doblabel=Label(addwindow,text='D.O.B',font=('arial',13,'bold'))
    doblabel.grid(row=2,column=0,padx=5,sticky=W)
    dobentry=Entry(addwindow,font=('arial',12))
    dobentry.grid(row=2,column=1,padx=10,pady=20)

    genderlabel=Label(addwindow,text='Gender',font=('arial',13,'bold'))
    genderlabel.grid(row=3,column=0,padx=5,sticky=W)
    genderentry=Entry(addwindow,font=('arial',12))
    genderentry.grid(row=3,column=1,padx=10,pady=20)

    mobilenolabel=Label(addwindow,text='Mobile No.',font=('arial',13,'bold'))
    mobilenolabel.grid(row=4,column=0,padx=5,sticky=W)
    mobilenoentry=Entry(addwindow,font=('arial',12))
    mobilenoentry.grid(row=4,column=1,padx=10,pady=20)

    emaillabel=Label(addwindow,text='E-Mail',font=('arial',13,'bold'))
    emaillabel.grid(row=5,column=0,padx=5,sticky=W)
    emailentry=Entry(addwindow,font=('arial',12))
    emailentry.grid(row=5,column=1,padx=10,pady=20)

    bloodlabel=Label(addwindow,text='Blood Group',font=('arial',13,'bold'))
    bloodlabel.grid(row=6,column=0,padx=5,sticky=W)
    bloodentry=Entry(addwindow,font=('arial',12))
    bloodentry.grid(row=6,column=1,padx=10,pady=20)

    addresslabel=Label(addwindow,text='Address',font=('arial',13,'bold'))
    addresslabel.grid(row=7,column=0,padx=5,sticky=W)
    addressentry=Entry(addwindow,font=('arial',12))
    addressentry.grid(row=7,column=1,padx=10,pady=20)

    add_student_bt=ttk.Button(addwindow,text='Submit',command=add_data)
    add_student_bt.grid(row=8,columnspan=2)

def connectdatabase():
    def connect():
        global mycon,con
        try:
            con=pymysql.connect(host=hostentry.get(),user=userentry.get(),password=passwordentry.get())
            mycon=con.cursor()
            
        except:
            messagebox.showerror("error","Invalid Details",parent=connectwindow)
            return
        try:
            query='create database studentmanagementsystem'
            mycon.execute(query)
            query='use studentmanagementsystem'
            mycon.execute(query)
            query='create table student(id int not null primary key,name varchar(30),dob varchar(20),address varchar(100),gender varchar(20),\
                mobileno varchar(10),email varchar(30),blood varchar(10),date varchar(50),time varchar(50))'
            mycon.execute(query)
        except:
            query='use studentmanagementsystem'
            mycon.execute(query)
        messagebox.showinfo("Success","Database connected Successfully",parent=connectwindow)
        connectwindow.destroy()
        addstudentbt.config(state=NORMAL)
        updatestudentbt.config(state=NORMAL)
        searchstudentbt.config(state=NORMAL)
        deletestudentbt.config(state=NORMAL)
        exitbt.config(state=NORMAL)
        exportstudentbt.config(state=NORMAL)
        showstudentbt.config(state=NORMAL)
    connectwindow=Toplevel()
    connectwindow.grab_set()
    connectwindow.geometry('350x250+730+180')
    connectwindow.resizable(0,0)
    connectwindow.title('Database Connection')
    hostnamelabel=Label(connectwindow,text='HostName',font=('arial',13,'bold'))
    hostnamelabel.grid(row=0,column=0,padx=10)

    hostentry=Entry(connectwindow,font=('arial',12))
    hostentry.grid(row=0,column=1,padx=10,pady=20)

    usernamelabel=Label(connectwindow,text='UserName',font=('arial',13,'bold'))
    usernamelabel.grid(row=1,column=0,padx=10)

    userentry=Entry(connectwindow,font=('arial',12))
    userentry.grid(row=1,column=1,padx=10,pady=20)

    passwordlabel=Label(connectwindow,text='Password',font=('arial',13,'bold'))
    passwordlabel.grid(row=2,column=0,padx=10)

    passwordentry=Entry(connectwindow,font=('arial',12))
    passwordentry.grid(row=2,column=1,padx=10,pady=20)

    connectbt=ttk.Button(connectwindow,text='Connect',command=connect)
    connectbt.grid(row=3,columnspan=2)

count=0
text=''
def slide():
    global count,text
    if count==len(s):
        count=0
        text=""
    text=text+s[count]
    slidelabel.config(text=text)
    count+=1
    slidelabel.after(200,slide)



def clock():
    global date,time1
    date=time.strftime('%d/%m/%Y')
    time1=time.strftime('%H:%M:%S')
    datetimelabel.config(text=f"   Date: {date}\nTime: {time1}")
    #After()- update some time 
    datetimelabel.after(1000,clock)
#GUI part
#root=Tk() is similar to this but ttkthemes has theme also.
root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')


root.geometry("1174x680+0+0")

datetimelabel=Label(root,font=('times new romen',15,'bold'))
datetimelabel.place(x=1,y=1)
clock()

s="Student Management System"
slidelabel=Label(root,text=s,font=('arial',25,'italic bold'),width=30)
slidelabel.place(x=200,y=0)
slide()

connectbt=ttk.Button(root,text="Connect Database",command=connectdatabase)
connectbt.place(x=800,y=0)

leftframe=Frame(root)
leftframe.place(x=50,y=80,width=300,height=600)

logo1=PhotoImage(file='students.png')
logolabel=Label(leftframe,image=logo1)
logolabel.grid(row=0,column=0)

addstudentbt=ttk.Button(leftframe,text="Add Student",width=25,state=DISABLED,command=add_student)
addstudentbt.grid(row=1,column=0,pady=20)

searchstudentbt=ttk.Button(leftframe,text="Search Student",width=25,state=DISABLED,command=search_student)
searchstudentbt.grid(row=2,column=0,pady=20)

updatestudentbt=ttk.Button(leftframe,text="Update Student",width=25,state=DISABLED,command=update_student)
updatestudentbt.grid(row=3,column=0,pady=20)

deletestudentbt=ttk.Button(leftframe,text="Delete Student",width=25,state=DISABLED,command=delete_student)
deletestudentbt.grid(row=4,column=0,pady=20)

showstudentbt=ttk.Button(leftframe,text="Show Student",width=25,state=DISABLED,command=show_student)
showstudentbt.grid(row=5,column=0,pady=20)

exportstudentbt=ttk.Button(leftframe,text="Export data",width=25,state=DISABLED,command=export_data)
exportstudentbt.grid(row=6,column=0,pady=20)

exitbt=ttk.Button(leftframe,text="Exit",width=25,state=DISABLED,command=iexit)
exitbt.grid(row=7,column=0,pady=20)

rightframe=Frame(root)
rightframe.place(x=350,y=80,width=820,height=600)

Scrollbarx=Scrollbar(rightframe,orient=HORIZONTAL)
Scrollbary=Scrollbar(rightframe,orient=VERTICAL)
Scrollbarx.pack(side=BOTTOM,fill=X)
Scrollbary.pack(side=RIGHT,fill=Y)
studenttable=ttk.Treeview(rightframe,columns=('ID','Name','D.O.B','Address','Gender','Mobile No.','E-Mail','Blood Group','Date','Time'),
                          xscrollcommand=Scrollbarx.set,yscrollcommand=Scrollbary.set)
Scrollbarx.config(command=studenttable.xview)
Scrollbary.config(command=studenttable.yview)

studenttable.pack(fill=BOTH,expand=1)

studenttable.heading('ID',text="ID")
studenttable.heading('Name',text="Name")
studenttable.heading('D.O.B',text="D.O.B")
studenttable.heading('Address',text="Address")
studenttable.heading('Gender',text="Gender")
studenttable.heading('Mobile No.',text="Mobile No.")
studenttable.heading('E-Mail',text="E-Mail")
studenttable.heading('Blood Group',text="Blood Group")
studenttable.heading('Date',text="Date")
studenttable.heading('Time',text="Time")

studenttable.config(show='headings')


root.mainloop()