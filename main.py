from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if(usernameEntry.get() == '' or passwordEntry.get() == ''):
        messagebox.showerror('Error',"Fields can't be empty")
    elif(usernameEntry.get() == 'Admin' and passwordEntry.get() == 'Admin'):
        messagebox.showinfo("Success","Welcome Admin")
        window.destroy()
        import sms
        
    else:
        messagebox.showerror("Error","Incorrect Credentials")

window = Tk()

window.geometry('1280x720+0+0')
window.title('Login system of student management system')

window.resizable(False,False)

backgroundImage = ImageTk.PhotoImage(file = 'image1.jpg')
bgLabel = Label(window,image = backgroundImage)
bgLabel.place(x=0,y=0)

loginFrame = Frame(window,bg='#b4c2cf')
loginFrame.place(x=450,y=150)

logoimage = PhotoImage(file='logo.png')
logoLabel = Label(loginFrame,image=logoimage)
logoLabel.grid(row = 0,column = 0,columnspan=2,pady=10)

userNameImage = PhotoImage(file = 'user.png')
userNameLabel = Label(loginFrame,image=userNameImage,text="Username",compound=LEFT,font=('times new roman',20,'bold'))
userNameLabel.grid(row=1,column=0,pady=10,padx=10)

usernameEntry = Entry(loginFrame,font=('times new roman',20,'bold'),bd=5)
usernameEntry.grid(row= 1,column=1,pady=10,padx=10)

passwordImage = PhotoImage(file = 'lock.png')
passwordLabel = Label(loginFrame,image=passwordImage,text="Password",compound=LEFT,font=('times new roman',20,'bold'))
passwordLabel.grid(row=2,column=0,pady=10,padx=10)

passwordEntry = Entry(loginFrame,font=('times new roman',20,'bold'),bd=5)
passwordEntry.grid(row= 2,column=1,pady=10,padx=10)

loginButton = Button(loginFrame,text = "Login",font=('times new roman',14,'bold'),width=15,bg='royalblue',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)

window.mainloop()