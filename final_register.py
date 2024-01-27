from tkinter import *
from tkinter.messagebox import *
from tkinter import messagebox
from tkinter import PhotoImage
import mysql.connector
import random
from datetime import *


background = '#FFFFFF'
button_mode1 = True
button_mode2 = True


window_register = Tk()
window_register.title('REGISTER')
window_register.geometry('900x400+260+150')
window_register.config(bg = background)
window_register.resizable(False,False)
    
            

def clear():
    user.delete(0,END)
    PasswordEntry.delete(0,END)
    PasswordConfirm.delete(0,END)
    
##Confirm Button
def Confirm():
    username = user.get()
    usernamecheck = [user.get()]
    password1 = PasswordEntry.get()
    password2 = PasswordConfirm.get()
    adminCODE = AdminAccess.get()
    
    ##print(username,password,adminCODE)   
    if adminCODE == "113801":
        if (username == "" or username == "ID" or password1 == "" or password1 == "Password" or password2 == "" or password2 == "Confirm Password"):
            messagebox.showerror("Login error","Type username or password!!")
            L2.configure(text = "")
            
        elif password1 != password2:
            L2.configure(text = "Your passwords don't match!!")
        
        else:
            L2.configure(text = "")
            try:
                #Connect to mysql
                myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
                cur = myconn.cursor()
                print("Connected to Database!!")
            except:
                messagebox.showerror("Connection","Database connection not stablish!!")
                return
            
            cur.execute("use userlogin")
            
            command = "select * from employee_info where Username=%s"
            cur.execute(command,(usernamecheck))
            myresult = cur.fetchone()
            #print(myresult)
            if myresult != None:
                messagebox.showerror("Error","User Name already exists!!")
                
            else:
                a = random.randint(1000,9999)
                c = random.randint(20,99)
                b = "SY"
                d = b+str(c)+str(a)
                
                today = date.today()
                
                command = "insert into employee_info(employee_ID,fullname,position,Username,Password,worker_since) values(%s,'đổi tên','Nhân viên',%s,%s,%s)"
                cur.execute(command,(d,username,password1,today))
                myconn.commit()
                myconn.close()
                    
                messagebox.showinfo("Register","Successfully created new user!!")
                clear()
                window_register.destroy()
                import final_login
            
            
    else:
        messagebox.showerror("Admin Code","Input Correct Admin code to create new user!!")
    

def login():
    window_register.destroy()
    import final_login
    


def key(event):
    username = user.get()
    usernamecheck = [user.get()]
    password1 = PasswordEntry.get()
    password2 = PasswordConfirm.get()
    adminCODE = AdminAccess.get()
    
    if adminCODE == "113801":
        if event.keysym == "Return":    
            if (username == "" or username == "ID" or password1 == "" or password1 == "Password" or password2 == "" or password2 == "Confirm Password"):
                messagebox.showerror("Login error","Type username or password!!")
                L2.configure(text = "")
                
            elif password1 != password2:
                L2.configure(text = "Your passwords don't match!!")
            
            else:
                L2.configure(text = "")
                try:
                    #Connect to mysql
                    myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
                    cur = myconn.cursor()
                    print("Connected to Database!!")
                except:
                    messagebox.showerror("Connection","Database connection not stablish!!")
                    return
                
                cur.execute("use userlogin")
                
                command = "select * from employee_info where Username=%s"
                cur.execute(command,(usernamecheck))
                myresult = cur.fetchone()
                #print(myresult)
                if myresult != None:
                    messagebox.showerror("Error","User Name already exists!!")
                    
                else:
                    command = "insert into employee_info(Username,Password) values(%s,%s)"
                    cur.execute(command,(username,password1))
                    myconn.commit()
                    myconn.close()
                        
                    messagebox.showinfo("Register","Successfully created new user!!")
                    clear()
                    window_register.destroy()
                    import final_login
            
            
    else:
        messagebox.showerror("Admin Code","Input Correct Admin code to create new user!!")   
        
         
#### ENTER
window_register.bind('<Return>',key)



########################## REGISTER
#icon img
icon = 'C:\\Users\\Admin\\Documents\\Tai_lieu_mon_hoc\\HKII_2022_2023\\Applied Programming in Engineering\\Final\\Image\\icon_register.png'
icon_img = PhotoImage(file = icon)
window_register.iconphoto(False,icon_img) 
    
#background img
frame = Frame(window_register,bg = background)
frame.pack(fill=Y)
    
bg_img = 'C:\\Users\\Admin\\Documents\\Tai_lieu_mon_hoc\\HKII_2022_2023\\Applied Programming in Engineering\\Final\\Image\\pts_background_register.png'
backgroundimg = PhotoImage(file = bg_img)
Label(frame,image = backgroundimg).pack()
    
    
#Admin access

AdminAccess = Entry(frame, width = 34,fg = "#000",border = 0, bg = "#fff", 
                        font = ("Arial Regular",12),show = "*")
AdminAccess.focus()
AdminAccess.place(x = 278, y = 107)
    
    
## user entry
def user_enter(e):
    user.config(fg = "#000")
    user.delete(0,'end')
    
def user_leave(e):
    name = user.get()
    if name == "":
        user.config(fg = "#D0D0D0")
        user.insert(0,"ID")
            
user = Entry(frame, width = 34, fg = "#D0D0D0",border = 0, bg = "#fff", font = ("Arial Regular",12))
user.insert(0,"ID")
user.bind("<FocusIn>",user_enter)
user.bind("<FocusOut>",user_leave)
user.place(x = 278, y = 150)
    
    
## password entry 
def password_enter1(e):
    PasswordEntry.config(fg = "#000")
    PasswordEntry.delete(0,'end')
        
    
def password_leave1(e):
    if PasswordEntry.get() == "":
        PasswordEntry.config(fg = "#D0D0D0")
        PasswordEntry.insert(0,"Password")
            
PasswordEntry = Entry(frame, width = 34, fg = "#D0D0D0",border = 0, bg = "#fff", font = ("Arial Regular",12))
PasswordEntry.insert(0,"Password")
PasswordEntry.bind("<FocusIn>",password_enter1)
PasswordEntry.bind("<FocusOut>",password_leave1)
PasswordEntry.place(x = 278, y = 195)
    
    
## password confirm
def password_enter2(e):
    PasswordConfirm.config(fg = "#000")
    PasswordConfirm.delete(0,'end')
        
    
def password_leave2(e):
    if PasswordConfirm.get() == "":
        PasswordConfirm.config(fg = "#D0D0D0")
        PasswordConfirm.insert(0,"Confirm Password")
            
PasswordConfirm = Entry(frame, width = 34, fg = "#D0D0D0",border = 0, bg = "#fff", font = ("Arial Regular",12))
PasswordConfirm.insert(0,"Confirm Password")
PasswordConfirm.bind("<FocusIn>",password_enter2)
PasswordConfirm.bind("<FocusOut>",password_leave2)
PasswordConfirm.place(x = 278, y = 237)
    
    
## Hide and show button 1111111
def show_and_hide1():
    global button_mode1
    if button_mode1 == True:
        eyeButton1.config(image = hiddeneye,activebackground = '#EBEBEB')
        if PasswordEntry.get() == "":
            PasswordEntry.config(show = "")
        else:
            PasswordEntry.config(show = "*")
        button_mode1 = False
    else:
        eyeButton1.config(image = openeye,activebackground = '#EBEBEB')
        PasswordEntry.config(show = "")
        button_mode1 = True
    
opeye = 'C:\\Users\\Admin\\Documents\\Tai_lieu_mon_hoc\\HKII_2022_2023\\Applied Programming in Engineering\\Final\\Image\\open_eye.png'
hdeye = 'C:\\Users\\Admin\\Documents\\Tai_lieu_mon_hoc\\HKII_2022_2023\\Applied Programming in Engineering\\Final\\Image\\hidden_eye.png'
openeye = PhotoImage(file = opeye)
hiddeneye = PhotoImage(file = hdeye)
    
eyeButton1 = Button(frame, image = openeye, bg = '#fff', border = 0,command = show_and_hide1)
eyeButton1.place(x = 590, y = 187)
    
    
    
## Hide and show button 22222222
def show_and_hide2():
    global button_mode2
    if button_mode2 == True:
        eyeButton2.config(image = hiddeneye,activebackground = '#EBEBEB')
        if PasswordConfirm.get() == "":
            PasswordConfirm.config(show = "")
        else:
            PasswordConfirm.config(show = "*")
        button_mode2 = False
    else:
        eyeButton2.config(image = openeye,activebackground = '#EBEBEB')
        PasswordConfirm.config(show = "")
        button_mode2 = True

    
eyeButton2 = Button(frame, image = openeye, bg = '#fff', border = 0,command = show_and_hide2)
eyeButton2.place(x = 590, y = 228)

    
    
    
#### ADD NEW USER
ConfirmButton = Button(window_register,text = "CONFIRM",fg = "#E8E9ED" , bg = "#2D3B55",width = 15, height = 1,border = 0,
                        font = ("Arial Bold",12),activebackground = "#2D3B55",command = Confirm)
ConfirmButton.place(x = 475, y = 300)
    
    
# Back Button
BackButton = Button(window_register,text = 'BACK',fg = "#2D3B55" , bg = "#E8E9ED",width = 15, height = 1,border = 0,
                        font = ("Arial Bold",12),activebackground = "#E8E9ED",command = login)
BackButton.place(x = 270, y = 300)
    
    
L2 = Label(text = "",fg = "red",bg = "white",border = 0)
L2.place(x = 370 , y = 265)
    
L1 = Label(window_register,text = "Admin Code",fg = "red",bg = "white",font = ("Arial Bold",12),border = 0)
L1.place(x = 278, y = 80)
    
window_register.mainloop()