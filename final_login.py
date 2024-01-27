from tkinter import *
from tkinter.messagebox import *
from tkinter import messagebox
from tkinter import PhotoImage
import mysql.connector


background = '#FFFFFF'
button_mode = True
trial_no = 0


window_login = Tk()
window_login.title('LOGIN')
window_login.geometry('900x400+260+150')
window_login.config(bg = background)
window_login.resizable(False,False) 

def Forgot():
    window_login.destroy()
    import final_forgot_password

def Register():
    window_login.destroy()
    import final_register
 

################################### LOGIN
#LOGIN TIMES
def trial():
            global trial_no
            trial_no +=1
            print("trial no: ",trial_no)
            if trial_no > 3:
                messagebox.showwarning("Warning","You have tried more then 3 times!!")
                window_login.destroy()


#LOGIN
def login():
        username = user.get()
        password = code.get()
            
        if (username == "" or username == "ID" or password == "" or password == "Password"):
                messagebox.showerror("Login error","Type username or password!!")
        else:
            try:
                #Connect to mysql
                myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
                cur = myconn.cursor()
                print("Connected to Database!!")
            except:
                messagebox.showerror("Connection","Database connection not stablish!!")
                return
               
        command = "use userlogin"
        cur.execute(command)     
               
        command = "update employee_info set status = 'offline'"
        cur.execute(command)
        myconn.commit()

                
        command = "select * from employee_info where Username=%s and Password=%s"
        cur.execute(command,(username,password))
        myresult = cur.fetchone()
        #print(myresult)
                
        if myresult == None:
            messagebox.showinfo("Invalid","Invalid ID or Password!!")
            trial()
                    
        else:
            messagebox.showinfo("Login","Successfully Login!!")
            window_login.destroy()
            
            command = "update employee_info set status=%s where Username=%s"
            cur.execute(command,("online",username))
            myconn.commit()
            myconn.close()
            import final_main


### ENTER
def key(event):
        username = user.get()
        password = code.get()
        if event.keysym == "Return":
            if (username == "" or username == "ID" or password == "" or password == "Password"):
                    messagebox.showerror("Login error","Type username or password!!")
            else:
                try:
                    #Connect to mysql
                    myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
                    cur = myconn.cursor()
                    print("Connected to Database!!")
                except:
                    messagebox.showerror("Connection","Database connection not stablish!!")
                    return
                
        command = "use userlogin"
        cur.execute(command)     
               
        command = "update employee_info set status = 'offline'"
        cur.execute(command)
        myconn.commit()

                
        command = "select * from employee_info where Username=%s and Password=%s"
        cur.execute(command,(username,password))
        myresult = cur.fetchone()
        #print(myresult)
                
        if myresult == None:
            messagebox.showinfo("Invalid","Invalid ID or Password!!")
            trial()
                    
        else:
            messagebox.showinfo("Login","Successfully Login!!")
            window_login.destroy()
            
            command = "update employee_info set status=%s where Username=%s"
            cur.execute(command,("online",username))
            myconn.commit()
            myconn.close()
            import final_main

#### ENTER
window_login.bind("<Return>",key)


#icon img
icon = 'C:\\Users\\Admin\\Documents\\Tai_lieu_mon_hoc\\HKII_2022_2023\\Applied Programming in Engineering\\Final\\Image\\login_icon2.png'
icon_img = PhotoImage(file = icon)
window_login.iconphoto(False,icon_img)

 
#background img
frame = Frame(window_login,bg = background)
frame.pack(fill=Y)
    
bg_img = 'C:\\Users\\Admin\\Documents\\Tai_lieu_mon_hoc\\HKII_2022_2023\\Applied Programming in Engineering\\Final\\Image\\pts_background.png'
backgroundimg = PhotoImage(file = bg_img)
Label(frame,image = backgroundimg).pack()


## user entry
def user_enter(event):
    user.config(fg = "#000")
    user.delete(0,'end')
    
def user_leave(event):
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
def password_enter(event):
    code.config(fg = "#000")
    code.delete(0,'end')

def password_leave(event):
    if code.get() == "":
        code.config(fg = "#D0D0D0")
        code.insert(0,"Password")
            
code = Entry(frame, width = 34, fg = "#D0D0D0",border = 0, bg = "#fff", font = ("Arial Regular",12))
code.insert(0,"Password")
code.bind("<FocusIn>",password_enter)
code.bind("<FocusOut>",password_leave)
code.place(x = 278, y = 195)


## Hide and show button
def show_and_hide():
    global button_mode
    if button_mode == True:
        eyeButton.config(image = hiddeneye,activebackground = '#EBEBEB')
        if code.get() == "":
            code.config(show = "")
        else:
            code.config(show = "*")
        button_mode = False
    else:
        eyeButton.config(image = openeye,activebackground = '#EBEBEB')
        code.config(show = "")
        button_mode = True


opeye = 'C:\\Users\\Admin\\Documents\\Tai_lieu_mon_hoc\\HKII_2022_2023\\Applied Programming in Engineering\\Final\\Image\\open_eye.png'
hdeye = 'C:\\Users\\Admin\\Documents\\Tai_lieu_mon_hoc\\HKII_2022_2023\\Applied Programming in Engineering\\Final\\Image\\hidden_eye.png'
openeye = PhotoImage(file = opeye)
hiddeneye = PhotoImage(file = hdeye)
    
eyeButton = Button(frame, image = openeye, bg = '#fff', border = 0,command = show_and_hide)
eyeButton.place(x = 590, y = 187)
    
    
#Login Button
LoginButton = Button(window_login,text = 'LOGIN',fg = "#E8E9ED" , bg = "#2D3B55",width = 15, height = 1,border = 0,
                        font = ("Arial Bold",12),activebackground = "#2D3B55",command = login)
LoginButton.place(x = 475, y = 300)


#Register Button
RegisterButton = Button(window_login,text = 'REGISTER',fg = "#2D3B55" , bg = "#E8E9ED",width = 15, height = 1,border = 0,
                            font = ("Arial Bold",12),activebackground = "#E8E9ED",command = Register)
RegisterButton.place(x = 270, y = 300)


#Foget password
ForgetPassword = Button(window_login, text = "Forgot your password?", fg = "#4765EC", bg = "#fff",
                        border = 0,activebackground = "#fff",command = Forgot)
ForgetPassword.place(x = 385, y = 245)

window_login.mainloop()