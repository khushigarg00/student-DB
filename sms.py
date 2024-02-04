from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox,filedialog
import pymysql
import pandas as pd


def exit_button():
    result = messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def export_data():
    # gives the path of the url entered
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    
    # get all the data on the treeview)
    indexing = studentTable.get_children()
    newlist = []
    for index in indexing:
        content = studentTable.item(index)
        datalist = content['values']
        newlist.append(datalist)

    # convert into tabular form using pandas
    table = pd.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time'])
    table.to_csv(url,index=False)

def update_student():

    def update_data():
        query = 'update student set name=%s,mobile=%s,email=%s, address=%s, gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(query,(nameEntry.get(),mobileEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currentTime,idEntry.get()))
        connector.commit()
        messagebox.showinfo('Success',f'Id {idEntry.get()} is modified successfully',parent=update_window)
        update_window.destroy()
        show_student()


    update_window = Toplevel()
    update_window.title('Update Student')
    update_window.resizable(0,0)
    update_window.grab_set()
    idLabel = Label(update_window,text='Id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column = 0,padx=30,pady=15,sticky=W)
    idEntry = Entry(update_window,font=('romana',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel = Label(update_window,text='Name',font=('times new roman',20,'bold'))
    nameLabel.grid(row=1,column = 0,padx=30,pady=15,sticky=W)
    nameEntry = Entry(update_window,font=('romana',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,pady=15,padx=10)

    mobileLabel = Label(update_window,text='Mobile No.',font=('times new roman',20,'bold'))
    mobileLabel.grid(row=2,column = 0,padx=30,pady=15,sticky=W)
    mobileEntry = Entry(update_window,font=('romana',15,'bold'),width=24)
    mobileEntry.grid(row=2,column=1,pady=15,padx=10)

    emailLabel = Label(update_window,text='Email',font=('times new roman',20,'bold'))
    emailLabel.grid(row=3,column = 0,padx=30,pady=15,sticky=W)
    emailEntry = Entry(update_window,font=('romana',15,'bold'),width=24)
    emailEntry.grid(row=3,column=1,pady=15,padx=10)

    addressLabel = Label(update_window,text='Address',font=('times new roman',20,'bold'))
    addressLabel.grid(row=4,column = 0,padx=30,pady=15,sticky=W)
    addressEntry = Entry(update_window,font=('romana',15,'bold'),width=24)
    addressEntry.grid(row=4,column=1,pady=15,padx=10)

    genderLabel = Label(update_window,text='Gender',font=('times new roman',20,'bold'))
    genderLabel.grid(row=5,column = 0,padx=30,pady=15,sticky=W)
    genderEntry = Entry(update_window,font=('romana',15,'bold'),width=24)
    genderEntry.grid(row=5,column=1,pady=15,padx=10)

    dobLabel = Label(update_window,text='DOB',font=('times new roman',20,'bold'))
    dobLabel.grid(row=6,column = 0,padx=30,pady=15,sticky=W)
    dobEntry = Entry(update_window,font=('romana',15,'bold'),width=24)
    dobEntry.grid(row=6,column=1,pady=15,padx=10)

    update_student_button = ttk.Button(update_window,text="Update Text",command=update_data)
    update_student_button.grid(row=7,columnspan=2,pady=15)

    indexing = studentTable.focus()
    content = studentTable.item(indexing)
    listdata = content['values']
    idEntry.insert(0,listdata[0])
    nameEntry.insert(0,listdata[1])
    mobileEntry.insert(0,listdata[2])
    emailEntry.insert(0,listdata[3])
    addressEntry.insert(0,listdata[4])
    genderEntry.insert(0,listdata[5])
    dobEntry.insert(0,listdata[6])


def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)


def delete_student():

    # get the index number of the selected row in DB
    indexing = studentTable.focus()

    # get the content of the selected row 
    content = studentTable.item(indexing)

    # get the ID of the selected row
    contentId = content['values'][0]

    # delete by id of the row
    query = ' delete from student where id=%s'
    mycursor.execute(query,contentId)
    connector.commit()
    messagebox.showinfo('Deleted',f'ID {contentId} is deleted successfully')

    # show the updated rows  
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)

def search_student():

    def search_data():
        query = 'select * from student where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender = %s or dob = %s'
        mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),mobileEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data = mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('',END,values=data)

    search_window = Toplevel()
    search_window.title('Search Student')
    search_window.resizable(0,0)
    search_window.grab_set()
    idLabel = Label(search_window,text='Id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column = 0,padx=30,pady=15,sticky=W)
    idEntry = Entry(search_window,font=('romana',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel = Label(search_window,text='Name',font=('times new roman',20,'bold'))
    nameLabel.grid(row=1,column = 0,padx=30,pady=15,sticky=W)
    nameEntry = Entry(search_window,font=('romana',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,pady=15,padx=10)

    mobileLabel = Label(search_window,text='Mobile No.',font=('times new roman',20,'bold'))
    mobileLabel.grid(row=2,column = 0,padx=30,pady=15,sticky=W)
    mobileEntry = Entry(search_window,font=('romana',15,'bold'),width=24)
    mobileEntry.grid(row=2,column=1,pady=15,padx=10)

    emailLabel = Label(search_window,text='Email',font=('times new roman',20,'bold'))
    emailLabel.grid(row=3,column = 0,padx=30,pady=15,sticky=W)
    emailEntry = Entry(search_window,font=('romana',15,'bold'),width=24)
    emailEntry.grid(row=3,column=1,pady=15,padx=10)

    addressLabel = Label(search_window,text='Address',font=('times new roman',20,'bold'))
    addressLabel.grid(row=4,column = 0,padx=30,pady=15,sticky=W)
    addressEntry = Entry(search_window,font=('romana',15,'bold'),width=24)
    addressEntry.grid(row=4,column=1,pady=15,padx=10)

    genderLabel = Label(search_window,text='Gender',font=('times new roman',20,'bold'))
    genderLabel.grid(row=5,column = 0,padx=30,pady=15,sticky=W)
    genderEntry = Entry(search_window,font=('romana',15,'bold'),width=24)
    genderEntry.grid(row=5,column=1,pady=15,padx=10)

    dobLabel = Label(search_window,text='DOB',font=('times new roman',20,'bold'))
    dobLabel.grid(row=6,column = 0,padx=30,pady=15,sticky=W)
    dobEntry = Entry(search_window,font=('romana',15,'bold'),width=24)
    dobEntry.grid(row=6,column=1,pady=15,padx=10)

    search_student_button = ttk.Button(search_window,text="Search",command= search_data)
    search_student_button.grid(row=7,columnspan=2,pady=15)


def add_student():

    # adding data to the database
    def add_data():

        # if any or all entries are empty then show error
        if idEntry.get()=='' or nameEntry.get() == '' or mobileEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
            messagebox.showerror('Error','All fields are required',parent=add_window)
        else:
            # query to add data into database
            try:
                query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(idEntry.get(),nameEntry.get(),mobileEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currentTime))
                connector.commit()
                result = messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the box.')
                if result:
                    idEntry.delete(0,END)
                    nameEntry.delete(0,END)
                    mobileEntry.delete(0,END)
                    emailEntry.delete(0,END)
                    addressEntry.delete(0,END)
                    genderEntry.delete(0,END)
                    dobEntry.delete(0,END)
                else:
                    pass
            except:
                messagebox.showerror('Error','Another student with same id already exists')
                return

            query = 'select * from student'
            mycursor.execute(query)

            # fetch the data from table
            fetched_data = mycursor.fetchall()

            # delete all the previous data
            studentTable.delete(*studentTable.get_children())
            # insert the data in the treeview as list 
            for data in fetched_data:
                dataList = list(data)
                studentTable.insert('',END,values=dataList)
    
    add_window = Toplevel()
    add_window.resizable(0,0)
    add_window.grab_set()
    idLabel = Label(add_window,text='Id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column = 0,padx=30,pady=15,sticky=W)
    idEntry = Entry(add_window,font=('romana',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel = Label(add_window,text='Name',font=('times new roman',20,'bold'))
    nameLabel.grid(row=1,column = 0,padx=30,pady=15,sticky=W)
    nameEntry = Entry(add_window,font=('romana',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,pady=15,padx=10)

    mobileLabel = Label(add_window,text='Mobile No.',font=('times new roman',20,'bold'))
    mobileLabel.grid(row=2,column = 0,padx=30,pady=15,sticky=W)
    mobileEntry = Entry(add_window,font=('romana',15,'bold'),width=24)
    mobileEntry.grid(row=2,column=1,pady=15,padx=10)

    emailLabel = Label(add_window,text='Email',font=('times new roman',20,'bold'))
    emailLabel.grid(row=3,column = 0,padx=30,pady=15,sticky=W)
    emailEntry = Entry(add_window,font=('romana',15,'bold'),width=24)
    emailEntry.grid(row=3,column=1,pady=15,padx=10)

    addressLabel = Label(add_window,text='Address',font=('times new roman',20,'bold'))
    addressLabel.grid(row=4,column = 0,padx=30,pady=15,sticky=W)
    addressEntry = Entry(add_window,font=('romana',15,'bold'),width=24)
    addressEntry.grid(row=4,column=1,pady=15,padx=10)

    genderLabel = Label(add_window,text='Gender',font=('times new roman',20,'bold'))
    genderLabel.grid(row=5,column = 0,padx=30,pady=15,sticky=W)
    genderEntry = Entry(add_window,font=('romana',15,'bold'),width=24)
    genderEntry.grid(row=5,column=1,pady=15,padx=10)

    dobLabel = Label(add_window,text='DOB',font=('times new roman',20,'bold'))
    dobLabel.grid(row=6,column = 0,padx=30,pady=15,sticky=W)
    dobEntry = Entry(add_window,font=('romana',15,'bold'),width=24)
    dobEntry.grid(row=6,column=1,pady=15,padx=10)

    add_student_button = ttk.Button(add_window,text="ADD STUDENT",command=add_data)
    add_student_button.grid(row=7,columnspan=2,pady=15)
    

def connect_database():

    def connect():
        global mycursor,connector
        try:
            connector = pymysql.connect(host='localhost',user='root',password=passwordEntry.get())

            # help in execution of mysql commands
            mycursor = connector.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return

        try:
            query = 'create database studentmanagementsystem'
            mycursor.execute(query)

            query = 'use studentmanagementsystem'
            mycursor.execute(query)

            query = 'create table student(id int not null primary key, name varchar(50),mobile varchar(10),email varchar(50),address varchar(100),gender varchar(10), dob varchar(20),date varchar(40),time varchar(50))'
            mycursor.execute(query)
        except:
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success','Database connection is successful',parent=connectWindow)
        connectWindow.destroy()

        addStudentButton.config(state=NORMAL)
        searchButton.config(state=NORMAL)
        updateButton.config(state=NORMAL)
        showButton.config(state=NORMAL)
        exportButton.config(state=NORMAL)
        deleteButton.config(state=NORMAL)




    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostNameLabel = Label(connectWindow,text="Host Name",font=('arial',20,'bold'))
    hostNameLabel.grid(row=0,column=0,padx=20)

    hostEntry = Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row= 0,column=1,padx=40,pady=20)

    userNameLabel = Label(connectWindow,text="Username",font=('arial',20,'bold'))
    userNameLabel.grid(row=1,column=0,padx=20)

    userNameEntry = Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    userNameEntry.grid(row= 1,column=1,padx=40,pady=20)

    passwordLabel = Label(connectWindow,text="Password",font=('arial',20,'bold'))
    passwordLabel.grid(row=2,column=0,padx=20)

    passwordEntry = Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    passwordEntry.grid(row= 2,column=1,padx=40,pady=20)

    connectButton = ttk.Button(connectWindow,text="Connect",command=connect)
    connectButton.grid(row=3,columnspan=2)


count = 0
text = ''
def slider():
    global text,count
    if count == len(s):
        count=0
        text = ''
    text = text + s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(150,slider)

def clock():
    global date,currentTime
    date = time.strftime('%d/%m/%Y')
    currentTime = time.strftime('%H:%M:%S')

    # config is used to assign to somethinig
    dateTimeLabel.config(text=f'   Date: {date}\nTime: {currentTime}')

    #after is used to do something again after some interval
    dateTimeLabel.after(1000,clock)


#create object of Tk class
root = ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

#provide size to the window and starting coordinates
root.geometry('1274x780+0+0')
root.resizable(0,0)
root.title('Student Management System')

dateTimeLabel = Label(root,font=('times new roman',18,'bold'))
dateTimeLabel.place(x=5,y=5)
clock()


s = "Student Management System"
sliderLabel = Label(root, font=('arial',28,'italic bold'),width=30)

# place is used to display something on the screen with provided coordinates
sliderLabel.place(x=200,y=0)
slider()

connectButton = ttk.Button(root,text="Connect Database",command=connect_database)
connectButton.place(x=980,y=0)

leftFrame = Frame(root)
leftFrame.place(x=50,y=80)

logoImage = PhotoImage(file = 'student.png')
logoLabel = Label(leftFrame,image= logoImage)
logoLabel.grid(row=0,column=0)

addStudentButton = ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=add_student)
addStudentButton.grid(row=1,column=0,pady=20)

searchButton = ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=search_student)
searchButton.grid(row=2,column=0,pady=20)

deleteButton = ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deleteButton.grid(row=3,column=0,pady=20)

updateButton = ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED,command=update_student)
updateButton.grid(row=4,column=0,pady=20)

showButton = ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_student)
showButton.grid(row=5,column=0,pady=20)

exportButton = ttk.Button(leftFrame,text='Export Student',width=25,state=DISABLED,command=export_data)
exportButton.grid(row=6,column=0,pady=20)

exitButton = ttk.Button(leftFrame,text='Exit',width=25,command=exit_button)
exitButton.grid(row=7,column=0,pady=20)

rightFrame = Frame(root)
rightFrame.place(x=350,y=80,width = 850,height= 670)

scrollBarX = Scrollbar(rightFrame,orient=HORIZONTAL)

scrollBarY = Scrollbar(rightFrame,orient=VERTICAL)

studentTable = ttk.Treeview(rightFrame,columns=('Id','Name','Mobile','Email','Address','Gender','DOB','AddedDate','AddedTime'),xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

# to show the scrollbar and change accordingly
scrollBarY.config(command=studentTable.yview)
scrollBarX.config(command=studentTable.xview)

# similar as place but used when complexity is very less

scrollBarX.pack(side=BOTTOM,fill=X)

scrollBarY.pack(side=RIGHT,fill=Y)

# to fill the frame
studentTable.pack(fill=BOTH, expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile',text='Mobile No.')
studentTable.heading('Email',text='Email')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('DOB',text='DOB')
studentTable.heading('AddedDate',text='Added Date')
studentTable.heading('AddedTime',text='Added Time')

studentTable.column('Id',width=50,anchor=CENTER)
studentTable.column('Name',width=300,anchor=CENTER)
studentTable.column('Email',width=300,anchor=CENTER)
studentTable.column('Mobile',width=200,anchor=CENTER)
studentTable.column('Address',width=300,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('DOB',width=100,anchor=CENTER)
studentTable.column('AddedDate',width=200,anchor=CENTER)
studentTable.column('AddedTime',width=200,anchor=CENTER)

style = ttk.Style()

style.configure('Treeview',rowheight=40,font = ('arial',12,'bold'))
style.configure('Treeview.Heading',font=('arial',14,'bold'))

studentTable.config(show='headings')


root.mainloop()