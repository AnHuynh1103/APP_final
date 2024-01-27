from tkinter import *
from tkinter.messagebox import *
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import ttk
from datetime import *
from tkinter.scrolledtext import ScrolledText

import mysql.connector
import customtkinter
import os
import random


background = '#FFE7CE'

window_main = customtkinter.CTk()
window_main.title('PET STORE SAYU')
window_main.geometry('1400x750+70+30')
window_main.config(bg = background)
window_main.resizable(False,False)


#==================================================================#    FUNCTIONS
def login():
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
    
    window_main.destroy()
    import final_login

def home():
    global home_img,background_home,StoreName
    Label(frame_operating,image=background_home,bg="#FFE7CE").place(x=0,y=0)
    StoreName = Label(frame_operating,text="SAYU STORE",font = ("Times New Roman Bold",40),bd=0,fg = "#000000",bg="#947257")
    StoreName.place(x = 555,y = 130)
    
def product():
    global NameEntry,IDEntry,TypeEntry,PriceEntry,AmountEntry,BrandEntry,StatusEntry
    #==========================================================================#    STORE NAME
    #==========================================================================#
    StoreName = Label(frame_operating,text="SAYU STORE",font = ("Times New Roman Bold",45),bd=0,fg = "#000000",bg="#F2BED1",width=40)
    StoreName.place(x = 0,y = 0)
    
    #==========================================================================#    PRODUCT INFO
    #==========================================================================#
    
    InfoProD = Label(frame_operating,font = ("Arial Bold",16),bg="#FFCDA8",width=55,height=14)
    InfoProD.place(x = 0, y = 70)
    ###0
    Name_INFO = Label(frame_operating,text="PRODUCT INFORMATION",font = ("Arial Bold",16),bg="#FFCDA8")
    Name_INFO.place(x=10,y=80)
    
    ###1
    NameLabel = Label(frame_operating,text="NAME",font = ("Arial",15),bg="#FFCDA8")          
    NameLabel.place(x=20,y=125)
    
    NameEntry = Entry(frame_operating,width = 37,font = ("Arial",12),bg="#FFE7CE")
    NameEntry.place(x=20,y=160)
    
    ###2
    IDLabel = Label(frame_operating,text="PRODUCT ID",font = ("Arial",15),bg="#FFCDA8")
    IDLabel.place(x=20,y=200)
    
    IDEntry = Entry(frame_operating,width = 37,font = ("Arial",12),bg="#FFE7CE")
    IDEntry.place(x=20,y=235)
    
    ###3
    TypeLabel = Label(frame_operating,text="TYPE",font = ("Arial",15),bg="#FFCDA8")
    TypeLabel.place(x=20,y=275)
    
    TypeEntry = Entry(frame_operating,width = 37,font = ("Arial",12),bg="#FFE7CE")
    TypeEntry.place(x=20,y=305)
    
    ###4
    PriceLabel = Label(frame_operating,text="PRICE (VND)",font = ("Arial",15),bg="#FFCDA8")
    PriceLabel.place(x=380,y=70)
    
    PriceEntry = Entry(frame_operating,width = 36,font = ("Arial",12),bg="#FFE7CE")
    PriceEntry.place(x=380,y=105)
    
    ###5
    AmountLabel = Label(frame_operating,text="AMOUNT",font = ("Arial",15),bg="#FFCDA8")
    AmountLabel.place(x=380,y=145)
    
    AmountEntry = Entry(frame_operating,width = 36,font = ("Arial",12),bg="#FFE7CE")
    AmountEntry.place(x=380,y=180)
    
    ###6
    BrandLabel = Label(frame_operating,text="BRAND",font = ("Arial",15),bg="#FFCDA8")
    BrandLabel.place(x=380,y=220)
    
    BrandEntry = Entry(frame_operating,width = 36,font = ("Arial",12),bg="#FFE7CE")
    BrandEntry.place(x=380,y=255)
    
    
    ###7
    StatusLabel = Label(frame_operating,text="STATUS",font = ("Arial",15),bg="#FFCDA8")
    StatusLabel.place(x=380,y=295)
    
    StatusEntry = Entry(frame_operating,width = 36,font = ("Arial",12),bg="#FFE7CE")
    StatusEntry.place(x=380,y=330)
    
    
    #==========================================================================#    FINDING PRODUCT
    #==========================================================================#
    
    FindProD = Label(frame_operating,font = ("Arial Bold",16),bg="#FFABAB",width=37,height=14)
    FindProD.place(x=720,y=70)
    ###0
    Name_FIND = Label(frame_operating,text="FIND PRODUCT",font = ("Arial Bold",16),bg="#FFABAB")
    Name_FIND.place(x=730,y=80)
    
    ###1
    NameFindLabel = Label(frame_operating,text="NAME",font = ("Arial",15),bg="#FFABAB")          
    NameFindLabel.place(x=740,y=125)
    
    NameFindEntry = Entry(frame_operating,width = 25,font = ("Arial",12))
    NameFindEntry.place(x=740,y=160)
    
    ###2
    IDFindLabel = Label(frame_operating,text="PRODUCT ID",font = ("Arial",15),bg="#FFABAB")          
    IDFindLabel.place(x=740,y=200)
    
    IDFindEntry = Entry(frame_operating,width = 25,font = ("Arial",12))
    IDFindEntry.place(x=740,y=235)
    
    #==========================================================================#    AVATAR
    #==========================================================================#
    AvatarInfo = Label(frame_operating,font = ("Arial Bold",16),fg="#000000",bg="#FFFFFF",height=14,width=22)
    AvatarInfo.place(x = 1200, y = 70)
    
    try:
        #Connect to mysql
        myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
        cur = myconn.cursor()
        #print("Connected to Database!!")
    except:
        messagebox.showerror("Connection","Database connection not stablish!!")
        return
    
    command = "use userlogin"
    cur.execute(command)
    
    command = "select * from employee_info where status ='online'"
    cur.execute(command)
    
    myresult = cur.fetchone()
    #print(myresult)

    command = "Select fullname from employee_info where status ='online'"
    cur.execute(command)
    name_result = cur.fetchone()
    name_result = ''.join(name_result)

    command = "Select position from employee_info where status ='online'"
    cur.execute(command)
    position_result = cur.fetchone()
    position_result = ''.join(position_result)

    Name_employ_label = Label(frame_operating,text="STAFF ON DUTY",font = ("Arial Bold",15),fg="#000000",bg="#FFFFFF")
    Name_employ_label.place(x=1210,y=80)
    
    Name_employee = Label(frame_operating,text="Name",font = ("Arial Bold",12),fg="#000000",bg="#FFFFFF")
    Name_employee.place(x = 1220,y = 150)
    
    Position_employee = Label(frame_operating,text="Position",font = ("Arial Bold",12),fg="#000000",bg="#FFFFFF")
    Position_employee.place(x = 1220,y = 225)
    
    
    DataName_Label = Label(frame_operating,text = name_result ,font = ("Arial",12),fg="#000000",bg="#FFFFFF")
    DataName_Label.place(x = 1220,y=175)
    
    
    DataPosition_Label = Label(frame_operating,text = position_result ,font = ("Arial",12),fg="#000000",bg="#FFFFFF")
    DataPosition_Label.place(x = 1220,y=250)
    
    
    #================================================================================#  BUTTONS FUNCTION
    #================================================================================#
    def search():
        name = NameFindEntry.get()
        namecheck = [name]
        ID = IDFindEntry.get()
        IDcheck = [ID]
        
        if (name == "" and ID == ""):
            NameEntry.delete(0,END)
            IDEntry.delete(0,END)
            TypeEntry.delete(0,END)
            PriceEntry.delete(0,END)
            AmountEntry.delete(0,END)
            BrandEntry.delete(0,END)
            StatusEntry.delete(0,END)
            messagebox.showerror("Error","Please enter the Name or ID of Products")
        
        elif (name!="" and ID!=""):
            try:
                #Connect to mysql
                myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
                cur = myconn.cursor()
                #print("Connected to Database!!")
            except:
                messagebox.showerror("Connection","Database connection not stablish!!")
                return 
        
            command = "use userlogin"
            cur.execute(command)
            
            command = "select PRODUCT from product where PRODUCT =%s and ProductID =%s"
            cur.execute(command,(name,ID))
            myname_product = cur.fetchone()
            if myname_product == None:
                messagebox.showerror("Error","The Product Name or ID are incorrect or doesn't exist!!!")
                NameFindEntry.delete(0,END)
                IDFindEntry.delete(0,END)
            else:
                myname_product = ''.join(myname_product)
            
            
            command = "select ProductID from product where PRODUCT =%s and ProductID =%s"
            cur.execute(command,(name,ID))
            myID_product = cur.fetchone()
            myID_product = ''.join(myID_product)
            
            
            command = "select TYPE from product where PRODUCT =%s and ProductID =%s"
            cur.execute(command,(name,ID))
            myType_product = cur.fetchone()
            myType_product = ''.join(myType_product)
            
            
            command = "select PRICE from product where PRODUCT =%s and ProductID =%s"
            cur.execute(command,(name,ID))
            myPrice_product = cur.fetchone()
            #myPrice_product = ''.join(myPrice_product)
            
            
            command = "select AMOUNT from product where PRODUCT =%s and ProductID =%s"
            cur.execute(command,(name,ID))
            myAmount_product = cur.fetchone()
            #myAmount_product = ''.join(myAmount_product)
            
            
            command = "select BRAND from product where PRODUCT =%s and ProductID =%s"
            cur.execute(command,(name,ID))
            myBrand_product = cur.fetchone()
            myBrand_product = ''.join(myBrand_product)
            
            command = "select STATUS from product where PRODUCT =%s and ProductID =%s"
            cur.execute(command,(name,ID))
            myStatus_product = cur.fetchone()
            myStatus_product = ''.join(myStatus_product)
            
            NameEntry.delete(0,END)
            IDEntry.delete(0,END)
            TypeEntry.delete(0,END)
            PriceEntry.delete(0,END)
            AmountEntry.delete(0,END)
            BrandEntry.delete(0,END)
            StatusEntry.delete(0,END)
            
            NameEntry.insert(0,myname_product)
            IDEntry.insert(0,myID_product)
            TypeEntry.insert(0,myType_product)
            PriceEntry.insert(0,myPrice_product)
            AmountEntry.insert(0,myAmount_product)
            BrandEntry.insert(0,myBrand_product)
            StatusEntry.insert(0,myStatus_product)
        
        elif name!="":
            try:
                #Connect to mysql
                myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
                cur = myconn.cursor()
                #print("Connected to Database!!")
            except:
                messagebox.showerror("Connection","Database connection not stablish!!")
                return
            
            command = "use userlogin"
            cur.execute(command)
            
            command = "select PRODUCT from product where PRODUCT =%s"
            cur.execute(command,(namecheck))
            myname_product = cur.fetchone()
            if myname_product == None:
                messagebox.showerror("Error","The Product Name or ID are incorrect or doesn't exist!!!")
                NameFindEntry.delete(0,END)
            else:
                myname_product = ''.join(myname_product)
            
            
            command = "select ProductID from product where PRODUCT =%s"
            cur.execute(command,(namecheck))
            myID_product = cur.fetchone()
            myID_product = ''.join(myID_product)
            
            
            command = "select TYPE from product where PRODUCT =%s"
            cur.execute(command,(namecheck))
            myType_product = cur.fetchone()
            myType_product = ''.join(myType_product)
            
            
            command = "select PRICE from product where PRODUCT =%s"
            cur.execute(command,(namecheck))
            myPrice_product = cur.fetchone()
            #myPrice_product = ''.join(myPrice_product)
            
            
            command = "select AMOUNT from product where PRODUCT =%s"
            cur.execute(command,(namecheck))
            myAmount_product = cur.fetchone()
            #myAmount_product = ''.join(myAmount_product)
            
            
            command = "select BRAND from product where PRODUCT =%s"
            cur.execute(command,(namecheck))
            myBrand_product = cur.fetchone()
            myBrand_product = ''.join(myBrand_product)
            
            command = "select STATUS from product where PRODUCT =%s"
            cur.execute(command,(namecheck))
            myStatus_product = cur.fetchone()
            myStatus_product = ''.join(myStatus_product)
            
            NameEntry.delete(0,END)
            IDEntry.delete(0,END)
            TypeEntry.delete(0,END)
            PriceEntry.delete(0,END)
            AmountEntry.delete(0,END)
            BrandEntry.delete(0,END)
            StatusEntry.delete(0,END)
            
            #===
            IDFindEntry.delete(0,END)
            IDFindEntry.insert(0,myID_product)
            #===
            
            NameEntry.insert(0,myname_product)
            IDEntry.insert(0,myID_product)
            TypeEntry.insert(0,myType_product)
            PriceEntry.insert(0,myPrice_product)
            AmountEntry.insert(0,myAmount_product)
            BrandEntry.insert(0,myBrand_product)
            StatusEntry.insert(0,myStatus_product)
            
        elif ID!="":
            try:
                #Connect to mysql
                myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
                cur = myconn.cursor()
                #print("Connected to Database!!")
            except:
                messagebox.showerror("Connection","Database connection not stablish!!")
                return
            
            command = "use userlogin"
            cur.execute(command)
            
            command = "select PRODUCT from product where ProductID =%s"
            cur.execute(command,(IDcheck))
            myname_product = cur.fetchone()
            if myname_product == None:
                messagebox.showerror("Error","The Product Name or ID are incorrect or doesn't exist!!!")
                IDFindEntry.delete(0,END)
            else:
                myname_product = ''.join(myname_product)
            
            
            command = "select ProductID from product where ProductID =%s"
            cur.execute(command,(IDcheck))
            myID_product = cur.fetchone()
            myID_product = ''.join(myID_product)
            
            
            command = "select TYPE from product where ProductID =%s"
            cur.execute(command,(IDcheck))
            myType_product = cur.fetchone()
            myType_product = ''.join(myType_product)
            
            
            command = "select PRICE from product where ProductID =%s"
            cur.execute(command,(IDcheck))
            myPrice_product = cur.fetchone()
            #myPrice_product = ''.join(myPrice_product)
            
            
            command = "select AMOUNT from product where ProductID =%s"
            cur.execute(command,(IDcheck))
            myAmount_product = cur.fetchone()
            #myAmount_product = ''.join(myAmount_product)
            
            
            command = "select BRAND from product where ProductID =%s"
            cur.execute(command,(IDcheck))
            myBrand_product = cur.fetchone()
            myBrand_product = ''.join(myBrand_product)
            
            command = "select STATUS from product where ProductID =%s"
            cur.execute(command,(IDcheck))
            myStatus_product = cur.fetchone()
            myStatus_product = ''.join(myStatus_product)
            
            NameEntry.delete(0,END)
            IDEntry.delete(0,END)
            TypeEntry.delete(0,END)
            PriceEntry.delete(0,END)
            AmountEntry.delete(0,END)
            BrandEntry.delete(0,END)
            StatusEntry.delete(0,END)
            #===
            NameFindEntry.delete(0,END)
            NameFindEntry.insert(0,myname_product)
            #===
            
            NameEntry.insert(0,myname_product)
            IDEntry.insert(0,myID_product)
            TypeEntry.insert(0,myType_product)
            PriceEntry.insert(0,myPrice_product)
            AmountEntry.insert(0,myAmount_product)
            BrandEntry.insert(0,myBrand_product)
            StatusEntry.insert(0,myStatus_product)
                
    def delete():
        NameEntry.delete(0,END)
        IDEntry.delete(0,END)
        TypeEntry.delete(0,END)
        PriceEntry.delete(0,END)
        AmountEntry.delete(0,END)
        BrandEntry.delete(0,END)
        StatusEntry.delete(0,END)
        
        
        NameFindEntry.delete(0,END)
        IDFindEntry.delete(0,END)

    def addtocart():
        name = NameEntry.get()
        ID = IDEntry.get()
        price = PriceEntry.get()
        type = TypeEntry.get()
        brand = BrandEntry.get()
        status = StatusEntry.get()
        amount = AmountEntry.get()
        if status == "Còn":
            try:
                #Connect to mysql
                myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
                cur = myconn.cursor()
                #print("Connected to Database!!")
            except:
                messagebox.showerror("Connection","Database connection not stablish!!")
                return
            
            left = int(amount)-1
            try:
                command = "use userlogin"
                cur.execute(command)

                command = "select IDProduct from shopping_cart where IDProduct=%s"
                cur.execute(command,(ID,))
                my_result = cur.fetchone()
                if my_result != None:
                    messagebox.showerror("Error","Your Product is available!!")
                else:
                    command = "insert into shopping_cart(NameProduct,IDProduct,Type,Price,AmountBuy,Brand,AmountStore,AmountLeft, StatusOLD) values(%s,%s,%s,%s,1,%s,%s,%s,%s)"
                    cur.execute(command,(name,ID,type,price,brand,amount,left,status))
                    myconn.commit()
                    
                    
                    command = "select AMOUNT from product where ProductID = %s"
                    cur.execute(command,(ID,))
                    number = cur.fetchone()
                    for i in number:
                        c = i
                    b = int(c) - 1
                    print(c,b)

                    
                    command = "update product set AMOUNT=%s where ProductID =%s"
                    cur.execute(command,(b,ID))
                    myconn.commit()
                    messagebox.showinfo("Notification","The product is added in your cart!!")
            except:
                    messagebox.showwarning("Warning","Your have to create the Shopping Cart first!!")
        else:
            messagebox.showwarning("Warning","The product is currently out of stock, please choose another product!!!")
        
    def display():
        try:
            #Connect to mysql
            myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
            cur = myconn.cursor()
            #print("Connected to Database!!")
        except:
            messagebox.showerror("Connection","Database connection not stablish!!")
            return
        
        
        
        command = "use userlogin"
        cur.execute(command)
        col = ("id","ProductID","PRODUCT","TYPE","PRICE","AMOUNT","STATUS","BRAND")

        ProductTable = Scrollbar(frame_operating,orient=VERTICAL)
        ListProduct = ttk.Treeview(frame_operating,columns = col,yscrollcommand=ProductTable.set,show="headings")
        ProductTable.config(command = ListProduct.yview)

        ListProduct.column("id",width=50)
        ListProduct.column("ProductID",width=150)
        ListProduct.column("PRODUCT",width=350)
        ListProduct.column("TYPE",width=200)
        ListProduct.column("PRICE",width=200)
        ListProduct.column("AMOUNT",width=150)
        ListProduct.column("STATUS",width=150)
        ListProduct.column("BRAND",width=200)


        ListProduct.heading("id",text="ID",anchor="center")
        ListProduct.heading("ProductID",text="PRODUCT ID",anchor="center")
        ListProduct.heading("PRODUCT",text="PRODUCT NAME",anchor="center")
        ListProduct.heading("TYPE",text="TYPE",anchor="center")
        ListProduct.heading("PRICE",text="PRICE",anchor="center")
        ListProduct.heading("AMOUNT",text="AMOUNT",anchor="center")
        ListProduct.heading("STATUS",text="STATUS",anchor="center")
        ListProduct.heading("BRAND",text="BRAND",anchor="center")

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")    

        command = 'select * from product'
        cur.execute(command)
        
        myresult = cur.fetchall()
        for i in range (len(myresult)):
            myresult[i] = list(myresult[i])
            myresult[i].pop(0)
            myresult[i].insert(0,i+1)
            
        for i in range(len(myresult)):
            ListProduct.insert("",END,value = myresult[i],tags= "font")
        style.configure("Heading",font = ("Arial Bold",12))
        ListProduct.tag_configure("font",font = ("Arial",12))
        ListProduct.place(x = 0, y = 408,height=522)
        
        def mouse_enter(e):
            for sel in ListProduct.selection():
                item = ListProduct.item(sel)
                ID = [item['values'][1]]

            try:
                myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
                cur = myconn.cursor()
                #print("Connected to Database!!")
            except:
                messagebox.showerror("Connection","Database connection not stablish!!")
                return
            
            command = "use userlogin"
            cur.execute(command)
            
            command = "select PRODUCT from product where ProductID =%s"
            cur.execute(command,(ID))
            myname_product = cur.fetchone()
            myname_product = ''.join(myname_product)
            
            
            command = "select ProductID from product where ProductID =%s"
            cur.execute(command,(ID))
            myID_product = cur.fetchone()
            myID_product = ''.join(myID_product)
            
            
            command = "select TYPE from product where ProductID =%s"
            cur.execute(command,(ID))
            myType_product = cur.fetchone()
            myType_product = ''.join(myType_product)
            
            
            command = "select PRICE from product where ProductID =%s"
            cur.execute(command,(ID))
            myPrice_product = cur.fetchone()
            #myPrice_product = ''.join(myPrice_product)
            
            
            command = "select AMOUNT from product where ProductID =%s"
            cur.execute(command,(ID))
            myAmount_product = cur.fetchone()
            #myAmount_product = ''.join(myAmount_product)
            
            
            command = "select BRAND from product where ProductID =%s"
            cur.execute(command,(ID))
            myBrand_product = cur.fetchone()
            myBrand_product = ''.join(myBrand_product)
            
            command = "select STATUS from product where ProductID =%s"
            cur.execute(command,(ID))
            myStatus_product = cur.fetchone()
            myStatus_product = ''.join(myStatus_product)
            
            NameEntry.delete(0,END)
            IDEntry.delete(0,END)
            TypeEntry.delete(0,END)
            PriceEntry.delete(0,END)
            AmountEntry.delete(0,END)
            BrandEntry.delete(0,END)
            StatusEntry.delete(0,END)
            
            
            NameEntry.insert(0,myname_product)
            IDEntry.insert(0,myID_product)
            TypeEntry.insert(0,myType_product)
            PriceEntry.insert(0,myPrice_product)
            AmountEntry.insert(0,myAmount_product)
            BrandEntry.insert(0,myBrand_product)
            StatusEntry.insert(0,myStatus_product)
    
        
        ListProduct.bind("<<TreeviewSelect>>",mouse_enter)

    def mouse_enter(e):
            for sel in ListProduct.selection():
                item = ListProduct.item(sel)
                ID = [item['values'][1]]

            try:
                myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
                cur = myconn.cursor()
                #print("Connected to Database!!")
            except:
                messagebox.showerror("Connection","Database connection not stablish!!")
                return
            
            command = "use userlogin"
            cur.execute(command)
            
            command = "select PRODUCT from product where ProductID =%s"
            cur.execute(command,(ID))
            myname_product = cur.fetchone()
            myname_product = ''.join(myname_product)
            
            
            command = "select ProductID from product where ProductID =%s"
            cur.execute(command,(ID))
            myID_product = cur.fetchone()
            myID_product = ''.join(myID_product)
            
            
            command = "select TYPE from product where ProductID =%s"
            cur.execute(command,(ID))
            myType_product = cur.fetchone()
            myType_product = ''.join(myType_product)
            
            
            command = "select PRICE from product where ProductID =%s"
            cur.execute(command,(ID))
            myPrice_product = cur.fetchone()
            #myPrice_product = ''.join(myPrice_product)
            
            
            command = "select AMOUNT from product where ProductID =%s"
            cur.execute(command,(ID))
            myAmount_product = cur.fetchone()
            #myAmount_product = ''.join(myAmount_product)
            
            
            command = "select BRAND from product where ProductID =%s"
            cur.execute(command,(ID))
            myBrand_product = cur.fetchone()
            myBrand_product = ''.join(myBrand_product)
            
            command = "select STATUS from product where ProductID =%s"
            cur.execute(command,(ID))
            myStatus_product = cur.fetchone()
            myStatus_product = ''.join(myStatus_product)
            
            
            NameEntry.delete(0,END)
            IDEntry.delete(0,END)
            TypeEntry.delete(0,END)
            PriceEntry.delete(0,END)
            AmountEntry.delete(0,END)
            BrandEntry.delete(0,END)
            StatusEntry.delete(0,END)
            
            
            NameEntry.insert(0,myname_product)
            IDEntry.insert(0,myID_product)
            TypeEntry.insert(0,myType_product)
            PriceEntry.insert(0,myPrice_product)
            AmountEntry.insert(0,myAmount_product)
            BrandEntry.insert(0,myBrand_product)
            StatusEntry.insert(0,myStatus_product)
    
    def createshoppingcart():
        try:
            #Connect to mysql
            myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
            cur = myconn.cursor()
            #print("Connected to Database!!")
        except:
            messagebox.showerror("Connection","Database connection not stablish!!")
            return
            

        try:
            command = "create table shopping_cart(id int not null auto_increment key, NameProduct varchar(250) null, IDProduct varchar(45) null, Type varchar(45) null, Price int null, AmountBuy int default null, Brand varchar(45) null, AmountStore int default null, AmountLeft int default null, StatusOLD varchar(20) null)"
            cur.execute(command)
            
            messagebox.showinfo("Notification","Your Shopping cart is created!!")
        except:
            messagebox.showerror("Error","Your Shopping cart is available!!")
        
    def cancelshoppingcart():
        try:
            #Connect to mysql
            myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
            cur = myconn.cursor()
            #print("Connected to Database!!")
        except:
            messagebox.showerror("Connection","Database connection not stablish!!")
            return
        
        try:
            command = "drop table shopping_cart"
            cur.execute(command)
            messagebox.showinfo("Notification","Your Shopping cart is canceled!!")
        except:
            messagebox.showerror("Error","Your don't have any Shopping Cart!!")

    #================================================================================#  BUTTONS LAYOUT
    #================================================================================#
    SearchButton = Button(frame_operating,text="Search",font = ("Arial",14),width=6,command=search)
    SearchButton.place(x=1025,y=158)
        
    DeleteButton = Button(frame_operating,text="Delete",font = ("Arial",14),width=6,command=delete)
    DeleteButton.place(x=1112,y=158)
    
    
    AddButton = Button(frame_operating,text="Add to cart",font = ("Arial",14),width=14,command=addtocart)
    AddButton.place(x=1025,y=233)
    
    DisplayButton = Button(frame_operating,text="Display",font = ("Arial",14),width=14,command=display)
    DisplayButton.place(x=1025,y=308)
    
    CreateShoppingCart = Button(frame_operating,text="Create Cart",font = ("Arial",14),command=createshoppingcart)
    CreateShoppingCart.place(x = 740, y = 300)
    
    CancelShoppingCart = Button(frame_operating,text="Cancel Cart",font = ("Arial",14),command=cancelshoppingcart)
    CancelShoppingCart.place(x=855,y=300)
    
    #==========================================================================#    PRODUCT TABLE LAYOUT
    #==========================================================================#
    
    ProD_Label = Label(frame_operating,text="PRODUCT TABLE",font = ("Times New Roman Bold",30),bd=0,fg = "#000000",bg="#F2BED1",width=60)
    ProD_Label.place(x=0,y=365)
    
    
    command = "use userlogin"
    cur.execute(command)
    col = ("id","ProductID","PRODUCT","TYPE","PRICE","AMOUNT","STATUS","BRAND")

    ProductTable = Scrollbar(frame_operating,orient=VERTICAL)
    ListProduct = ttk.Treeview(frame_operating,columns = col,yscrollcommand=ProductTable.set,show="headings")
    ProductTable.config(command = ListProduct.yview)

    ListProduct.column("id",width=50)
    ListProduct.column("ProductID",width=150)
    ListProduct.column("PRODUCT",width=350)
    ListProduct.column("TYPE",width=200)
    ListProduct.column("PRICE",width=200)
    ListProduct.column("AMOUNT",width=150)
    ListProduct.column("STATUS",width=150)
    ListProduct.column("BRAND",width=200)


    ListProduct.heading("id",text="ID",anchor="center")
    ListProduct.heading("ProductID",text="PRODUCT ID",anchor="center")
    ListProduct.heading("PRODUCT",text="PRODUCT NAME",anchor="center")
    ListProduct.heading("TYPE",text="TYPE",anchor="center")
    ListProduct.heading("PRICE",text="PRICE",anchor="center")
    ListProduct.heading("AMOUNT",text="AMOUNT",anchor="center")
    ListProduct.heading("STATUS",text="STATUS",anchor="center")
    ListProduct.heading("BRAND",text="BRAND",anchor="center")
    
    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")    

    command = 'select * from product'
    cur.execute(command)
    
    myresult = cur.fetchall()
    for i in range (len(myresult)):
        myresult[i] = list(myresult[i])
        myresult[i].pop(0)
        myresult[i].insert(0,i+1)
        
    for i in range(len(myresult)):
        ListProduct.insert("",END,value = myresult[i],tags= "font")
    style.configure("Heading",font = ("Arial Bold",12))
    ListProduct.tag_configure("font",font = ("Arial",12))
    ListProduct.place(x = 0, y = 408,height=522)
    myconn.close()
    
    
    ListProduct.bind("<<TreeviewSelect>>",mouse_enter)

def shopping():
    global NameDetailEntry, IDDetailEntry, TypeDetailEntry, AmountDetailEntry, PriceDetailEntry, VoucherDetailEntry, SumDetailEntry
    
    #==========================================================================#    STORE NAME LAYOUT
    #==========================================================================#
    StoreName = Label(frame_operating,text="SAYU STORE",font = ("Times New Roman Bold",45),bd=0,fg = "#000000",bg="#F2BED1",width=40)
    StoreName.place(x = 0,y = 0)
    
    #==========================================================================#    AVATAR LAYOUT
    #==========================================================================#
    AvatarInfo = Label(frame_operating,font = ("Arial Bold",16),fg="#000000",bg="#FFFFFF",height=17,width=22)
    AvatarInfo.place(x = 1200, y = 70)
    
    try:
        #Connect to mysql
        myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
        cur = myconn.cursor()
        #print("Connected to Database!!")
    except:
        messagebox.showerror("Connection","Database connection not stablish!!")
        return
    
    command = "use userlogin"
    cur.execute(command)
    
    command = "select * from employee_info where status ='online'"
    cur.execute(command)
    
    myresult = cur.fetchone()
    #print(myresult)

    command = "Select fullname from employee_info where status ='online'"
    cur.execute(command)
    name_result = cur.fetchone()
    name_result = ''.join(name_result)

    command = "Select position from employee_info where status ='online'"
    cur.execute(command)
    position_result = cur.fetchone()
    position_result = ''.join(position_result)

    Name_employ_label = Label(frame_operating,text="STAFF ON DUTY",font = ("Arial Bold",15),fg="#000000",bg="#FFFFFF")
    Name_employ_label.place(x=1210,y=80)
    
    Name_employee = Label(frame_operating,text="Name",font = ("Arial Bold",12),fg="#000000",bg="#FFFFFF")
    Name_employee.place(x = 1220,y = 150)
    
    Position_employee = Label(frame_operating,text="Position",font = ("Arial Bold",12),fg="#000000",bg="#FFFFFF")
    Position_employee.place(x = 1220,y = 225)
    
    
    DataName_Label = Label(frame_operating,text = name_result ,font = ("Arial",12),fg="#000000",bg="#FFFFFF")
    DataName_Label.place(x = 1220,y=175)
    
    
    DataPosition_Label = Label(frame_operating,text = position_result ,font = ("Arial",12),fg="#000000",bg="#FFFFFF")
    DataPosition_Label.place(x = 1220,y=250)

    #==========================================================================#    PRODUCT DETAIL LAYOUT
    #==========================================================================#
    ShoppingCartlLabel = Label(frame_operating,anchor="nw",text="SHOPPING LIST",font = ("Arial Bold",16),width=60,height = 15,fg="#000000",bg="#E5BEEC")
    ShoppingCartlLabel.place(x=0,y=70)
    
    BillLabel = Label(frame_operating,anchor="nw",text="BILL",font = ("Arial Bold",16),width=37,height = 15,fg="#000000",bg="#FFAAC9")
    BillLabel.place(x=720,y=70)
    
    ProductDetailLabel = Label(frame_operating,anchor="nw",text="DETAIL",font = ("Arial Bold",16),width=60,height = 22,fg="#000000",bg="#D8C4B6")
    ProductDetailLabel.place(x=0,y=435)
    
    CustomerInfo = Label(frame_operating,anchor="nw",text = "CUSTOMER INFORMATION",font = ("Arial Bold",16),width=60,height = 22,fg="#000000",bg="#FFCDA8")
    CustomerInfo.place(x=720,y=435)
    
    
    #==========================================================================#    ENTRIES LAYOUT
    #==========================================================================#
    
    #1=============================================== NAME
    NameDetailLabel = Label(frame_operating,text="PRODUCT",font = ("Arial",14),fg="#000000",bg="#D8C4B6")
    NameDetailLabel.place(x=10,y=500)
    
    NameDetailEntry = Entry(frame_operating,font = ("Arial",14),fg="#000000",bg="#D8C4B6",width=28)
    NameDetailEntry.place(x=10,y=530)
    #1
    
    #2=============================================== ID
    IDDetailLabel = Label(frame_operating,text="ID",font = ("Arial",14),fg="#000000",bg="#D8C4B6")
    IDDetailLabel.place(x=10,y=580)
    
    IDDetailEntry = Entry(frame_operating,font = ("Arial",14),fg="#000000",bg="#D8C4B6",width=28)
    IDDetailEntry.place(x=10,y=610)
    #2
    
    #3================================================ TYPE
    TypeDetailLabel = Label(frame_operating,text="TYPE",font = ("Arial",14),fg="#000000",bg="#D8C4B6")
    TypeDetailLabel.place(x=10,y=660)
    
    TypeDetailEntry = Entry(frame_operating,font = ("Arial",14),fg="#000000",bg="#D8C4B6",width=28)
    TypeDetailEntry.place(x=10,y=690)
    #3
    
    #4================================================ BRAND
    StafflLabel = Label(frame_operating,text="STAFF",font = ("Arial",14),fg="#000000",bg="#D8C4B6")
    StafflLabel.place(x=10,y=740)
    
    StaffDetailEntry = Entry(frame_operating,font = ("Arial",14),fg="#000000",bg="#D8C4B6",width=28)
    StaffDetailEntry.place(x=10,y=770)
    #4
    
    #5================================================ PRICE
    PriceDetailLabel = Label(frame_operating,text="PRICE",font = ("Arial",14),fg="#000000",bg="#D8C4B6")
    PriceDetailLabel.place(x=380,y=500)
    
    PriceDetailEntry = Entry(frame_operating,font = ("Arial",14),fg="#000000",bg="#D8C4B6",width=28)
    PriceDetailEntry.place(x=380,y=530)
    #5
    
    #6================================================ AMOUNT
    AmountDetailLabel = Label(frame_operating,text="AMOUNT",font = ("Arial",14),fg="#000000",bg="#D8C4B6")
    AmountDetailLabel.place(x=380,y=580)
    
    AmountDetailEntry = Entry(frame_operating,font = ("Arial",14),fg="#000000",bg="#FFFFFF",width=28)
    AmountDetailEntry.place(x=380,y=610)
    #6
    
    #7================================================ VOUCHER
    VoucherDetailLabel = Label(frame_operating,text="VOUCHER",font = ("Arial",14),fg="#000000",bg="#D8C4B6")
    VoucherDetailLabel.place(x=380,y=660)
    
    VoucherDetailEntry = Entry(frame_operating,font = ("Arial",14),fg="#000000",bg="#FFFFFF",width=28)
    VoucherDetailEntry.place(x=380,y=690)
    #7
    
    
    #8================================================ SUM
    SumDetailLabel = Label(frame_operating,text="SUM",font = ("Arial",14),fg="#000000",bg="#D8C4B6")
    SumDetailLabel.place(x=380,y=740)
    
    SumDetailEntry = Entry(frame_operating,font = ("Arial",14),fg="#000000",bg="#D8C4B6",width=28)
    SumDetailEntry.place(x=380,y=770)
    #8
    
    
    #==========================================================================#    CUSTOMER INFO
    #==========================================================================#
    
    FullnameLabel = Label(frame_operating,text="Full Name",font = ("Arial",14),fg="#000000",bg="#FFCDA8")
    FullnameLabel.place(x=730,y=500)
    
    FullnameEntry = Entry(frame_operating,font = ("Arial",14),fg="#000000",bg="#FFCDA8",width=28)
    FullnameEntry.place(x=730,y=530)
    
    
    IDCustomerLabel = Label(frame_operating,text="Citizen Identification No",font = ("Arial",14),fg="#000000",bg="#FFCDA8")
    IDCustomerLabel.place(x=1090,y=500)
    
    IDCustomerEntry = Entry(frame_operating,font = ("Arial",14),fg="#000000",bg="#FFCDA8",width=28)
    IDCustomerEntry.place(x=1090,y=530)
    
    
    PhoneLabel = Label(frame_operating,text="Phone No",font = ("Arial",14),fg="#000000",bg="#FFCDA8")
    PhoneLabel.place(x=730,y=600)
    
    PhoneEntry = Entry(frame_operating,font = ("Arial",14),fg="#000000",bg="#FFCDA8",width=28)
    PhoneEntry.place(x=730,y=630)
    
    
    AddressLabel = Label(frame_operating,text="Address",font = ("Arial",14),fg="#000000",bg="#FFCDA8")
    AddressLabel.place(x=1090,y=600)
    
    AddressEntry = Entry(frame_operating,font = ("Arial",14),fg="#000000",bg="#FFCDA8",width=28)
    AddressEntry.place(x=1090,y=630)
    
    
    GenderLabel = Label(frame_operating,text="Gender",font = ("Arial",14),fg="#000000",bg="#FFCDA8")
    GenderLabel.place(x=730,y=700)
    
    GenderEntry = Entry(frame_operating,font = ("Arial",14),fg="#000000",bg="#FFCDA8",width=28)
    GenderEntry.place(x=730,y=730)
    
    
    CashLabel = Label(frame_operating,text="Cash (VND)",font = ("Arial",14),fg="#000000",bg="#FFCDA8")
    CashLabel.place(x=1090,y=700)
    
    CashEntry = Entry(frame_operating,font = ("Arial",14),fg="#000000",bg="#FFFFFF",width=28)
    CashEntry.place(x=1090,y=730)
    
    
    
    #==========================================================================#    BUTTONS FUNC
    #==========================================================================#
        
    
    
    def display():
        voucher = [VoucherDetailEntry.get()]
        try:
            #Connect to mysql
            myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
            cur = myconn.cursor()
            #print("Connected to Database!!")
        except:
            messagebox.showerror("Connection","Database connection not stablish!!")
            return

        
        
        
        
        NameDetailEntry.delete(0,END)
        IDDetailEntry.delete(0,END)
        TypeDetailEntry.delete(0,END)
        AmountDetailEntry.delete(0,END)            
        PriceDetailEntry.delete(0,END)
        
        #BillCode = random.randint(100000,999999)
        BillDate = date.today()
        BillText.delete(1.0,END)
            
        command = "select IDProduct, AmountBuy, Price from shopping_cart"
        cur.execute(command)
        result = cur.fetchall()
        
        BillText.insert(END,f"Bill code: {BillCode}\t\t\t\t          Date: {BillDate}\n\n")
        BillText.insert(END,"*****************************************************************************\n")
        BillText.insert(END,"PRODUCT ID\t\t\tAMOUNT\t\t         PRICE\n\n")
        for i in range(len(result)):
            BillText.insert(END, f"{result[i][0]}\t\t\t         {result[i][1]}\t\t      {result[i][2]}\n\n")
        BillText.insert(END,"*****************************************************************************\n")
                    
        
        giam = ""
        if VoucherDetailEntry.get() !="":
            sum = SumDetailEntry.get()
            gia = float(sum)/0.95
            giam = gia*0.05
                
            BillText.insert(END,f"VOUCHER\t\t\t\t\t     -{giam}\n")
            BillText.insert(END,"*****************************************************************************\n")
            
        else:
            BillText.insert(END,f"VOUCHER\t\t\t\t\t{giam}\n")
            BillText.insert(END,"*****************************************************************************\n")
        
        
        command = "select fullname from employee_info where status ='online'"
        cur.execute(command)
        mystaff = cur.fetchone()
        mystaff = ''.join(mystaff)
        
        BillText.insert(END,"STORE\t\tSTAFF\t\t\t           SUM\n\n")
        BillText.insert(END,f"SAYU\t\t{mystaff}\t\t\t     {SumDetailEntry.get()}\n\n")
        BillText.insert(END,"*****************************************************************************\n")
        BillText.insert(END,"Thank you so much!!")
        
        col = ("id","IDProduct","NameProduct","Price","AmountBuy")
        ShoppingTable = Scrollbar(frame_operating,orient=VERTICAL)
        #ShoppingTable.place(x=0,y=70)
            
            
        ListShopping = ttk.Treeview(frame_operating, columns=col,yscrollcommand=ShoppingTable.set,show="headings")
        ShoppingTable.config(command=ListShopping.yview)
            
        ListShopping.column("id",width=50)
        ListShopping.column("IDProduct",width=150)
        ListShopping.column("NameProduct",width=150)
        ListShopping.column("Price",width=100)
        ListShopping.column("AmountBuy",width=50)
            
            
        ListShopping.heading("id",text="id")
        ListShopping.heading("IDProduct",text="Product ID")
        ListShopping.heading("NameProduct",text="Product Name")
        ListShopping.heading("Price",text="Price")
        ListShopping.heading("AmountBuy",text="Amount")
            
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")    
            
        command = 'select id, IDProduct, NameProduct, Price, AmountBuy from shopping_cart'
        cur.execute(command)
            
        myresult = cur.fetchall()
        for i in range (len(myresult)):
            myresult[i] = list(myresult[i])
            myresult[i].pop(0)
            myresult[i].insert(0,i+1)
                
        for i in range(len(myresult)):
            ListShopping.insert("",END,value = myresult[i],tags= "font")
        style.configure("Heading",font = ("Arial Bold",12))
        ListShopping.tag_configure("font",font = ("Arial",12))
        ListShopping.place(x = 0, y = 100,height=335,width=720)
        
        sum=0
        command = "select AmountBuy, Price from shopping_cart"
        cur.execute(command)
        result = cur.fetchall()
        print(result)
        for r in range(len(result)):
                sum1 = result[r][0]*result[r][1]
                sum = sum1+sum
        
        try:
            command = "select date from voucher where voucher=%s"
            cur.execute(command,(voucher))
            result_check = cur.fetchone()
            #print(result_check)
            
            for i in result_check:
                voucherdate = i        
            today = date.today()
            if voucherdate>=today:
                sum = 0.95*sum
                SumDetailEntry.delete(0,END)
                SumDetailEntry.insert(0,sum)
        except:
                sum = sum
                SumDetailEntry.delete(0,END)
                SumDetailEntry.insert(0,sum)
        
        
        def mouse_enter(e):
            for sel in ListShopping.selection():
                item = ListShopping.item(sel)
                ID = [item['values'][1]]

            try:
                myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
                cur = myconn.cursor()
                #print("Connected to Database!!")
            except:
                messagebox.showerror("Connection","Database connection not stablish!!")
                return
                
            command = "use userlogin"
            cur.execute(command)
                
            command = "select NameProduct from shopping_cart where IDProduct =%s"
            cur.execute(command,(ID))
            myname_product = cur.fetchone()
            myname_product = ''.join(myname_product)
                
                
            command = "select IDProduct from shopping_cart where IDProduct =%s"
            cur.execute(command,(ID))
            myID_product = cur.fetchone()
            myID_product = ''.join(myID_product)
                
                
            command = "select Type from shopping_cart where IDProduct =%s"
            cur.execute(command,(ID))
            myType_product = cur.fetchone()
            myType_product = ''.join(myType_product)
                
                
            command = "select Price from shopping_cart where IDProduct =%s"
            cur.execute(command,(ID))
            myPrice_product = cur.fetchone()
            #myPrice_product = ''.join(myPrice_product)
                
                
            command = "select AmountBuy from shopping_cart where IDProduct =%s"
            cur.execute(command,(ID))
            myAmount_product = cur.fetchone()
            #myAmount_product = ''.join(myAmount_product)
                
            
            NameDetailEntry.delete(0,END)
            IDDetailEntry.delete(0,END)
            TypeDetailEntry.delete(0,END)
            PriceDetailEntry.delete(0,END)
            AmountDetailEntry.delete(0,END)
            

            NameDetailEntry.insert(0,myname_product)
            IDDetailEntry.insert(0,myID_product)
            TypeDetailEntry.insert(0,myType_product)
            PriceDetailEntry.insert(0,myPrice_product)
            AmountDetailEntry.insert(0,myAmount_product)
            
 
            
        ListShopping.bind("<<TreeviewSelect>>",mouse_enter)
       
    
    def checkvoucher():
        voucher = VoucherDetailEntry.get()
        try:
            #Connect to mysql
            myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
            cur = myconn.cursor()
            #print("Connected to Database!!")
        except:
            messagebox.showerror("Connection","Database connection not stablish!!")
            return
        
        command = "use userlogin"
        cur.execute(command)
        if voucher != "":
            try:
                command = "select date from voucher where voucher=%s"
                cur.execute(command,(voucher,))
                result = cur.fetchone()
                for i in result:
                    voucherdate = i
                today = date.today()
                if voucherdate >= today:
                    messagebox.showinfo("Notification","Your voucher is still valid!")
                    sum = 0
                    command = "select AmountBuy, Price from shopping_cart"
                    cur.execute(command)
                    result = cur.fetchall()
                    for r in range(len(result)):
                        sum1 = result[r][0]*result[r][1]
                        sum = sum1+sum
                    sum = 0.95*sum
                    SumDetailEntry.delete(0,END)
                    SumDetailEntry.insert(0,sum)
                    
                elif voucherdate < today:
                    messagebox.showinfo("Notification","Your voucher has expired! Please Choose another one!")
                    VoucherDetailEntry.delete(0,END)
                    
                    sum = 0
                    command = "select AmountBuy, Price from shopping_cart"
                    cur.execute(command)
                    result = cur.fetchall()
                    for r in range(len(result)):
                        sum1 = result[r][0]*result[r][1]
                        sum = sum1+sum
                    
                    SumDetailEntry.delete(0,END)
                    SumDetailEntry.insert(0,sum)
            except:
                messagebox.showerror("Error","Your voucher is incorrect or does not exist! Please check back!")
                VoucherDetailEntry.delete(0,END)
                
                sum = 0
                command = "select AmountBuy, Price from shopping_cart"
                cur.execute(command)
                result = cur.fetchall()
                for r in range(len(result)):
                    sum1 = result[r][0]*result[r][1]
                    sum = sum1+sum
                
                SumDetailEntry.delete(0,END)
                SumDetailEntry.insert(0,sum)
        else:
            sum = 0
            command = "select AmountBuy, Price from shopping_cart"
            cur.execute(command)
            result = cur.fetchall()
            for r in range(len(result)):
                sum1 = result[r][0]*result[r][1]
                sum = sum1+sum
                
            SumDetailEntry.delete(0,END)
            SumDetailEntry.insert(0,sum)
        
    
    def confirm():
        amount = AmountDetailEntry.get()
        amount_update = AmountDetailEntry.get()
        ID = IDDetailEntry.get()
        voucher = VoucherDetailEntry.get()
        global OK_mode
        OK_mode = 0
        try:
            #Connect to mysql
            myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
            cur = myconn.cursor()
            #print("Connected to Database!!")
        except:
            messagebox.showerror("Connection","Database connection not stablish!!")
            return
        
        try:
            command = "create table bill(id int not null auto_increment key, billcode int null, billdate date null, CustomerName varchar(45) null, CustomerID varchar(25) null, gender varchar(10) null, PhoneNo varchar(15) null, address varchar(100) null, Cash int null, staffname varchar(45) null, staffID varchar(10) null)"
            cur.execute(command)
        except:
            pass
        
        command = "select AmountStore from shopping_cart where IDProduct =%s"
        cur.execute(command,(ID,))
        myAmount_store = cur.fetchone()
        for i in myAmount_store:
            b = i
        
        left = b - int(amount_update)
        
        
        command = "select StatusOLD from shopping_cart where IDProduct =%s"
        cur.execute(command,(ID,))
        myAmount_store = cur.fetchone()
        for i in myAmount_store:
            c = i
                
        
        
        if left<0:
            messagebox.showwarning("Warning","Not enough product in store!!")
        elif left==0:
            if int(amount) >= 1: 
                    command = "update shopping_cart set AmountBuy = %s, AmountLeft = %s where IDProduct=%s"
                    cur.execute(command,(amount_update,left,ID))
                    myconn.commit()
                            
                            
                    command = "update product set AMOUNT = %s, STATUS ='Hết' where ProductID=%s"
                    cur.execute(command,(left,ID))
                    myconn.commit()
                    messagebox.showinfo("Notification","Your shopping cart has been updated!") 
            else:
                messagebox.showerror("Error","Can not update your shopping cart! Please check back!")
        else:
            if amount=="" and ID !="":
                messagebox.showerror("Error","Please enter the Product Amount!!")
            
            elif amount != "" and ID !="":
                command = "use userlogin"
                cur.execute(command)
                
                command = "select AmountBuy=%s from shopping_cart where IDProduct=%s"
                cur.execute(command,(amount,ID))
                result = cur.fetchone()
                if int(amount) >= 1:
                    try:
                        if result !=None :
                            command = "update shopping_cart set AmountBuy = %s, AmountLeft = %s where IDProduct=%s"
                            cur.execute(command,(amount_update,left,ID))
                            myconn.commit()
                            
                            
                            command = "update product set AMOUNT = %s, STATUS =%s where ProductID=%s"
                            cur.execute(command,(left,c,ID))
                            myconn.commit()
                            messagebox.showinfo("Notification","Your shopping cart has been updated!")
                        else:
                            messagebox.showerror("Error","Can not update your shopping cart! Please check back!")
                    except:
                        messagebox.showerror("Error","Can not update your shopping cart! Please check back!")
                elif int(amount)==0:
                    command = "update product set AMOUNT = %s, STATUS =%s where ProductID=%s"
                    cur.execute(command,(b,c,ID))
                    
                    command = "delete from shopping_cart where IDProduct =%s"
                    cur.execute(command,(ID,))
                    myconn.commit()
                    messagebox.showinfo("Notification","The product has been removed from your cart!")
                else:
                    messagebox.showerror("Error","Can not update your shopping cart! Please check back!")
                    
                if voucher != "":
                    try:
                        command = "select date from voucher where voucher=%s"
                        cur.execute(command,(voucher,))
                        result = cur.fetchone()
                        for i in result:
                            voucherdate = i
                        today = date.today()
                        if voucherdate >= today:
                            sum = 0
                            command = "select AmountBuy, Price from shopping_cart"
                            cur.execute(command)
                            result = cur.fetchall()
                            for r in range(len(result)):
                                sum1 = result[r][0]*result[r][1]
                                sum = sum1+sum
                            sum = 0.95*sum
                            SumDetailEntry.delete(0,END)
                            SumDetailEntry.insert(0,sum)
                            
                        elif voucherdate < today:
                            VoucherDetailEntry.delete(0,END)
                            
                            sum = 0
                            command = "select AmountBuy, Price from shopping_cart"
                            cur.execute(command)
                            result = cur.fetchall()
                            for r in range(len(result)):
                                sum1 = result[r][0]*result[r][1]
                                sum = sum1+sum
                            
                            SumDetailEntry.delete(0,END)
                            SumDetailEntry.insert(0,sum)
                    except:
                        messagebox.showerror("Error","Your voucher is incorrect or does not exist! Please check back!")
                        VoucherDetailEntry.delete(0,END)
                        sum = 0
                        command = "select AmountBuy, Price from shopping_cart"
                        cur.execute(command)
                        result = cur.fetchall()
                        for r in range(len(result)):
                            sum1 = result[r][0]*result[r][1]
                            sum = sum1+sum
                        
                        SumDetailEntry.delete(0,END)
                        SumDetailEntry.insert(0,sum)
                else:
                    sum = 0
                    command = "select AmountBuy, Price from shopping_cart"
                    cur.execute(command)
                    result = cur.fetchall()
                    for r in range(len(result)):
                        sum1 = result[r][0]*result[r][1]
                        sum = sum1+sum
                        
                    SumDetailEntry.delete(0,END)
                    SumDetailEntry.insert(0,sum)
            else:
                pass
            
            
    def printbill():
        bill=BillText.get(1.0,END)
        #print(bill)
        file_dir = open(f"{BillCode}.txt","w",encoding="utf-8")
        file_dir.write(bill)
        file_dir.close()
        messagebox.showinfo("Notification","Your bill is printed!")
        
        
    def pay():
        cash = CashEntry.get()
        pay = SumDetailEntry.get()
        
        name = FullnameEntry.get()
        ID = IDCustomerEntry.get()
        phone = PhoneEntry.get()
        address = AddressEntry.get()
        gender = GenderEntry.get()
        try:
            myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
            cur = myconn.cursor()
            #print("Connected to Database!!")
        except:
            messagebox.showerror("Connection","Database connection not stablish!!")
            return
        
        command ="use userlogin"
        cur.execute(command)
        
        if (name == "" or ID == "" or phone=="" or address=="" or gender=="" or OK_mode == 0):
            messagebox.showerror("Error","Please update all information!!!")
            
        else:
            if float(cash) == float(pay):
                    command = "update bill set Cash = %s where billcode =%s"
                    cur.execute(command,(pay,BillCode))
                    result = cur.fetchone()
                    myconn.commit()
                    messagebox.showinfo("Notification","Your bill is pay!! Thank you very much!")
                    
                    
                    change_cash = float(cash) - float(pay)
                    BillText.delete(1.0,END)
                        
                    command = "select IDProduct, AmountBuy, Price from shopping_cart"
                    cur.execute(command)
                    result = cur.fetchall()
                    
                    BillText.insert(END,f"Bill code: {BillCode}\t\t\t\t          Date: {BillDate}\n\n")
                    BillText.insert(END,"*****************************************************************************\n")
                    BillText.insert(END,"PRODUCT ID\t\t\tAMOUNT\t\t         PRICE\n\n")
                    for i in range(len(result)):
                        BillText.insert(END, f"{result[i][0]}\t\t\t         {result[i][1]}\t\t      {result[i][2]}\n\n")
                    BillText.insert(END,"*****************************************************************************\n")
                                
                    
                    giam = ""
                    if VoucherDetailEntry.get() !="":
                        sum = SumDetailEntry.get()
                        gia = float(sum)/0.95
                        giam = gia*0.05
                            
                        BillText.insert(END,f"VOUCHER\t\t\t\t\t     -{giam}\n")
                        BillText.insert(END,"*****************************************************************************\n")
                        
                    else:
                        BillText.insert(END,f"VOUCHER\t\t\t\t\t{giam}\n")
                        BillText.insert(END,"*****************************************************************************\n")
                    
                    BillText.insert(END,f"SUM\t\t\t\t\t      {SumDetailEntry.get()}\n\n")
                    
                    BillText.insert(END,f"CASH\t\t\t\t\t      {cash}\n\n")
                    BillText.insert(END,"*****************************************************************************\n")
                    BillText.insert(END,f"CHANGE\t\t\t\t\t      {change_cash}\n\n")
                    BillText.insert(END,"*****************************************************************************\n")
                    
                    command = "select fullname from employee_info where status ='online'"
                    cur.execute(command)
                    mystaff = cur.fetchone()
                    mystaff = ''.join(mystaff)
                    
                    BillText.insert(END,"STORE\t\tSTAFF\t\t\t\n\n")
                    BillText.insert(END,f"SAYU\t\t{mystaff}\n\n")
                    BillText.insert(END,"*****************************************************************************\n")
                    
                    BillText.insert(END,"Thank you so much!!")
                    
                    
                    
                    
                    command = "drop table shopping_cart"
                    cur.execute(command)
                    
                    
            elif float(cash) > float(pay):
                try:
                    command = "update bill set Cash = %s where billcode =%s"
                    cur.execute(command,(pay,BillCode))
                    myconn.commit()
                    messagebox.showinfo("Notification","Your bill is pay!! Thank you very much!")
                    
                    change_cash = float(cash)-float(pay)
                    
                    print(change_cash)
                    BillText.delete(1.0,END)
                        
                    command = "select IDProduct, AmountBuy, Price from shopping_cart"
                    cur.execute(command)
                    result = cur.fetchall()
                    
                    BillText.insert(END,f"Bill code: {BillCode}\t\t\t\t          Date: {BillDate}\n\n")
                    BillText.insert(END,"*****************************************************************************\n")
                    BillText.insert(END,"PRODUCT ID\t\t\tAMOUNT\t\t         PRICE\n\n")
                    for i in range(len(result)):
                        BillText.insert(END, f"{result[i][0]}\t\t\t         {result[i][1]}\t\t      {result[i][2]}\n\n")
                    BillText.insert(END,"*****************************************************************************\n")
                                
                    
                    giam = ""
                    if VoucherDetailEntry.get() !="":
                        sum = SumDetailEntry.get()
                        gia = float(sum)/0.95
                        giam = gia*0.05
                            
                        BillText.insert(END,f"VOUCHER\t\t\t\t\t     -{giam}\n")
                        BillText.insert(END,"*****************************************************************************\n")
                        
                    else:
                        BillText.insert(END,f"VOUCHER\t\t\t\t\t{giam}\n")
                        BillText.insert(END,"*****************************************************************************\n")
                    
                    BillText.insert(END,f"SUM\t\t\t\t\t      {SumDetailEntry.get()}\n\n")
                    
                    BillText.insert(END,f"CASH\t\t\t\t\t      {cash}\n\n")
                    BillText.insert(END,"*****************************************************************************\n")
                    BillText.insert(END,f"CHANGE\t\t\t\t\t      {change_cash}\n\n")
                    BillText.insert(END,"*****************************************************************************\n")
                    
                    command = "select fullname from employee_info where status ='online'"
                    cur.execute(command)
                    mystaff = cur.fetchone()
                    mystaff = ''.join(mystaff)
                    
                    BillText.insert(END,"STORE\t\tSTAFF\t\t\t\n\n")
                    BillText.insert(END,f"SAYU\t\t{mystaff}\n\n")
                    BillText.insert(END,"*****************************************************************************\n")
                    
                    BillText.insert(END,"Thank you so much!!")
                    
                    command = "drop table shopping_cart"
                    cur.execute(command)
                    
                except:
                    messagebox.showerror("Error","Can pay the bill, Please enter customer information first!!")
                    
            elif cash == "":
                messagebox.showerror("Error","Please enter your cash!!")
            elif float(cash) < float(pay):
                messagebox.showerror("Error","Your cash is not enough, Please check back!!")

    
    def ok():
        name = FullnameEntry.get()
        ID = IDCustomerEntry.get()
        phone = PhoneEntry.get()
        address = AddressEntry.get()
        gender = GenderEntry.get()
        
        global OK_mode
        OK_mode = 0
        if (name == "" or ID == "" or phone=="" or address=="" or gender==""):
            messagebox.showerror("Error","Please complete all information!!!")
            
        else:
            try:
                myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
                cur = myconn.cursor()
                #print("Connected to Database!!")
            except:
                messagebox.showerror("Connection","Database connection not stablish!!")
                return

            OK_mode = 1
            command = "use userlogin"
            cur.execute(command)
            
            command = "select fullname from employee_info where status ='online'"
            cur.execute(command)
            staff = cur.fetchone()
            staff = ''.join(staff)
            
            command = "select employee_ID from employee_info where status ='online'"
            cur.execute(command)
            staffID = cur.fetchone()
            staffID = ''.join(staffID)
    
    
            command = "select Billcode from bill where Billcode =%s"
            cur.execute(command,(BillCode,))
            check = cur.fetchone()
            if check == None:
                try:
                    command = "create table bill(id int not null auto_increment key, billcode int null, billdate date null, CustomerName varchar(45) null, CustomerID varchar(25) null, gender varchar(10) null, PhoneNo varchar(15) null, address varchar(100) null, Cash int null, staffname varchar(45) null, staffID varchar(10) null)"
                    cur.execute(command)
                    
                    command = "insert into bill(billcode,billdate,CustomerName,CustomerID,gender,PhoneNo,address,staffname,staffID) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cur.execute(command,(BillCode,BillDate,name,ID,gender,phone,address,staff,staffID))
                    myconn.commit()
                    messagebox.showinfo("Notification","Customer information is update!")
                    
                    
                except:
                    command = "insert into bill(billcode,billdate,CustomerName,CustomerID,gender,PhoneNo,address,staffname,staffID) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cur.execute(command,(BillCode,BillDate,name,ID,gender,phone,address,staff,staffID))
                    myconn.commit()
                    messagebox.showinfo("Notification","Customer information is update!")
            else:
                messagebox.showwarning("Warning","The Bill is already exist!!")
                            
    
    def mouse_enter(e):
        for sel in ListShopping.selection():
                item = ListShopping.item(sel)
                ID = [item['values'][1]]

        try:
            myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
            cur = myconn.cursor()
            #print("Connected to Database!!")
        except:
            messagebox.showerror("Connection","Database connection not stablish!!")
            return
            
        command = "use userlogin"
        cur.execute(command)
            
        command = "select NameProduct from shopping_cart where IDProduct =%s"
        cur.execute(command,(ID))
        myname_product = cur.fetchone()
        myname_product = ''.join(myname_product)
            
            
        command = "select IDProduct from shopping_cart where IDProduct =%s"
        cur.execute(command,(ID))
        myID_product = cur.fetchone()
        myID_product = ''.join(myID_product)
            
            
        command = "select Type from shopping_cart where IDProduct =%s"
        cur.execute(command,(ID))
        myType_product = cur.fetchone()
        myType_product = ''.join(myType_product)
            
            
        command = "select Price from shopping_cart where IDProduct =%s"
        cur.execute(command,(ID))
        myPrice_product = cur.fetchone()
        #myPrice_product = ''.join(myPrice_product)
            
            
        command = "select AmountBuy from shopping_cart where IDProduct =%s"
        cur.execute(command,(ID))
        myAmount_product = cur.fetchone()
        #myAmount_product = ''.join(myAmount_product)
            
        
        NameDetailEntry.delete(0,END)
        IDDetailEntry.delete(0,END)
        TypeDetailEntry.delete(0,END)
        PriceDetailEntry.delete(0,END)
        AmountDetailEntry.delete(0,END)
            

        NameDetailEntry.insert(0,myname_product)
        IDDetailEntry.insert(0,myID_product)
        TypeDetailEntry.insert(0,myType_product)
        PriceDetailEntry.insert(0,myPrice_product)
        AmountDetailEntry.insert(0,myAmount_product)
    
    #==========================================================================#    BUTTONS LAYOUT
    #==========================================================================#
    
    
    DisplayButton = Button(frame_operating,text="DISPLAY",font = ("Arial Bold",14),width=12,height=3,command=display)
    DisplayButton.place(x=70,y=830)
    
    CheckVoucherButton = Button(frame_operating,text="CHECK\n\nVOUCHER",font = ("Arial Bold",14),width=12,height=3,command=checkvoucher)
    CheckVoucherButton.place(x=270,y=830)

    ConfirmButton = Button(frame_operating,text="CONFIRM",font = ("Arial Bold",14),width=12,height=3,command=confirm)
    ConfirmButton.place(x=470,y=830)

    
    OKButton = Button(frame_operating,text="OK",font = ("Arial Bold",14),width=12,heigh=3,command=ok)
    OKButton.place(x=800,y=830)
    
    
    PayButton = Button(frame_operating,text="PAY",font = ("Arial Bold",14),width=12,heigh=3,command=pay)
    PayButton.place(x = 1000, y = 830)


    PrintBillButton = Button(frame_operating,text="PRINT\n\nBILL",font = ("Arial Bold",14),width=12,height=3,command=printbill)
    PrintBillButton.place(x = 1200, y = 830)    
    
    #==========================================================================#    BILL LAYPOUT
    #==========================================================================#
    try:
        command = "select fullname from employee_info where status ='online'"
        cur.execute(command)
        mystaff = cur.fetchone()
        mystaff = ''.join(mystaff)
        
        StaffDetailEntry.delete(0,END)
        StaffDetailEntry.insert(0,mystaff)
        
        
        
        sum = 0
        command = "select AmountBuy, Price from shopping_cart"
        cur.execute(command)
        result = cur.fetchall()
        for r in range(len(result)):
            sum1 = result[r][0]*result[r][1]
            sum = sum1+sum
            
        SumDetailEntry.delete(0,END)
        SumDetailEntry.insert(0,sum)
        
        
        BillText = ScrolledText(frame_operating,font=("Arial Bold",12))
        BillText.place(x=720,y=100,width=487,height=335)
            
        BillCode = random.randint(100000,999999)
        BillDate = date.today()
        BillText.delete(1.0,END)
            
        command = "select IDProduct, AmountBuy, Price from shopping_cart"
        cur.execute(command)
        result = cur.fetchall()
        
        BillText.insert(END,f"Bill code: {BillCode}\t\t\t\t          Date: {BillDate}\n\n")
        BillText.insert(END,"*****************************************************************************\n")
        BillText.insert(END,"PRODUCT ID\t\t\tAMOUNT\t\t         PRICE\n\n")
        for i in range(len(result)):
            BillText.insert(END, f"{result[i][0]}\t\t\t         {result[i][1]}\t\t      {result[i][2]}\n\n")
        BillText.insert(END,"*****************************************************************************\n")
                    
        
        giam = ""
        if VoucherDetailEntry.get() !="":
            sum = SumDetailEntry.get()
            gia = float(sum)/0.95
            giam = gia*0.05
                
            BillText.insert(END,f"VOUCHER\t\t\t\t\t-{giam}\n")
            BillText.insert(END,"*****************************************************************************\n")
            
        else:
            BillText.insert(END,f"VOUCHER\t\t\t\t\t{giam}\n")
            BillText.insert(END,"*****************************************************************************\n")
        
        
        command = "select fullname from employee_info where status ='online'"
        cur.execute(command)
        mystaff = cur.fetchone()
        mystaff = ''.join(mystaff)
        
        BillText.insert(END,"STORE\t\tSTAFF\t\t\t           SUM\n\n")
        BillText.insert(END,f"SAYU\t\t{mystaff}\t\t\t     {SumDetailEntry.get()}\n\n")
        BillText.insert(END,"*****************************************************************************\n")
        BillText.insert(END,"Thank you so much!!")
        
    
    #==========================================================================#    SHOPPING CART LAYOUT
    #==========================================================================#
    
        col = ("id","IDProduct","NameProduct","Price","AmountBuy")
        ShoppingTable = Scrollbar(frame_operating,orient=VERTICAL)
        #ShoppingTable.place(x=0,y=70)
            
        ListShopping = ttk.Treeview(frame_operating, columns=col,yscrollcommand=ShoppingTable.set,show="headings")
        ShoppingTable.config(command=ListShopping.yview)
            
        ListShopping.column("id",width=50)
        ListShopping.column("IDProduct",width=150)
        ListShopping.column("NameProduct",width=150)
        ListShopping.column("Price",width=100)
        ListShopping.column("AmountBuy",width=50)
            
            
        ListShopping.heading("id",text="id")
        ListShopping.heading("IDProduct",text="Product ID")
        ListShopping.heading("NameProduct",text="Product Name")
        ListShopping.heading("Price",text="Price")
        ListShopping.heading("AmountBuy",text="Amount")
            
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")    
            
        command = 'select id, IDProduct, NameProduct, Price, AmountBuy from shopping_cart'
        cur.execute(command)
            
        myresult = cur.fetchall()
        for i in range (len(myresult)):
            myresult[i] = list(myresult[i])
            myresult[i].pop(0)
            myresult[i].insert(0,i+1)
                
        for i in range(len(myresult)):
            ListShopping.insert("",END,value = myresult[i],tags= "font")
        style.configure("Heading",font = ("Arial Bold",12))
        ListShopping.tag_configure("font",font = ("Arial",12))
        ListShopping.place(x = 0, y = 100,height=335,width=720)
        myconn.close()
        
        
        
        
        
        
        ListShopping.bind("<<TreeviewSelect>>",mouse_enter)
    except:
        messagebox.showwarning("Warning","Your don't have any Shopping Cart!! Please create one!!")

def employee():
    #==========================================================================#    STORE NAME LAYOUT
    #==========================================================================#
    StoreName = Label(frame_operating,text="SAYU STORE",font = ("Times New Roman Bold",45),bd=0,fg = "#000000",bg="#F2BED1",width=40)
    StoreName.place(x = 0,y = 0)
    
    #==========================================================================#    AVATAR LAYOUT
    #==========================================================================#
    AvatarInfo = Label(frame_operating,font = ("Arial Bold",16),fg="#000000",bg="#FFFFFF",height=17,width=22)
    AvatarInfo.place(x = 1200, y = 70)
    
    try:
        #Connect to mysql
        myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
        cur = myconn.cursor()
        #print("Connected to Database!!")
    except:
        messagebox.showerror("Connection","Database connection not stablish!!")
        return
    
    command = "use userlogin"
    cur.execute(command)
    
    command = "select * from employee_info where status ='online'"
    cur.execute(command)
    
    myresult = cur.fetchone()
    #print(myresult)

    command = "Select fullname from employee_info where status ='online'"
    cur.execute(command)
    name_result = cur.fetchone()
    name_result = ''.join(name_result)

    command = "Select position from employee_info where status ='online'"
    cur.execute(command)
    position_result = cur.fetchone()
    position_result = ''.join(position_result)

    Name_employ_label = Label(frame_operating,text="STAFF ON DUTY",font = ("Arial Bold",15),fg="#000000",bg="#FFFFFF")
    Name_employ_label.place(x=1210,y=80)
    
    Name_employee = Label(frame_operating,text="Name",font = ("Arial Bold",12),fg="#000000",bg="#FFFFFF")
    Name_employee.place(x = 1220,y = 150)
    
    Position_employee = Label(frame_operating,text="Position",font = ("Arial Bold",12),fg="#000000",bg="#FFFFFF")
    Position_employee.place(x = 1220,y = 225)
    
    
    DataName_Label = Label(frame_operating,text = name_result ,font = ("Arial",12),fg="#000000",bg="#FFFFFF")
    DataName_Label.place(x = 1220,y=175)
    
    
    DataPosition_Label = Label(frame_operating,text = position_result ,font = ("Arial",12),fg="#000000",bg="#FFFFFF")
    DataPosition_Label.place(x = 1220,y=250)
    
    
    #=============================================================================================#     FIND STAFF LAYOUT
    #=============================================================================================#
    StaffInfoLabel = Label(frame_operating,anchor="n",text = "STAFF TABLE",font=("Times new roman Bold",18),width=86,heigh=16,fg="#000000",bg="#FFAAC9")
    StaffInfoLabel.place(x=0,y=70)
    
    

    EditLabel = Label(frame_operating,font=("Arial Bold",18),width=100,heigh=16,fg="#000000",bg="#FFE7CE")
    EditLabel.place(x=0,y=508)
    
    
    
    #=============================================================================================#     EDIT LAYOUT
    #=============================================================================================#
    NameEditLabel = Label(frame_operating,text="FULL NAME",font=("Arial Bold",16),fg="#000000",bg="#FFE7CE")
    NameEditLabel.place(x=20,y=550)
    
    NameEditEntry = Entry(frame_operating,font=("Arial",16),fg="#000000",bg="#FFFFFF",width=30)
    NameEditEntry.place(x=20,y=580)
    
    
    CTIDEditLabel = Label(frame_operating,text="CITIZEN ID (*)",font=("Arial Bold",16),fg="#000000",bg="#FFE7CE")
    CTIDEditLabel.place(x=20,y=650)
    
    CTIDEditEntry = Entry(frame_operating,font=("Arial",16),fg="#000000",bg="#FFFFFF",width=30)
    CTIDEditEntry.place(x=20,y=680)
    
    
    GenderEditLabel = Label(frame_operating,text="GENDER",font=("Arial Bold",16),fg="#000000",bg="#FFE7CE")
    GenderEditLabel.place(x=20,y=750)
    
    GenderEditEntry = Entry(frame_operating,font=("Arial",16),fg="#000000",bg="#FFFFFF",width=30)
    GenderEditEntry.place(x=20,y=780)
    
    
    PositionEditLabel = Label(frame_operating,text="POSITION",font=("Arial Bold",16),fg="#000000",bg="#FFE7CE")
    PositionEditLabel.place(x=490,y=550)
    
    PositionEditEntry = Entry(frame_operating,font=("Arial",16),fg="#000000",bg="#FFFFFF",width=30)
    PositionEditEntry.place(x=490,y=580)
    
    
    PhoneEditLabel = Label(frame_operating,text="PHONE NO (*)",font=("Arial Bold",16),fg="#000000",bg="#FFE7CE")
    PhoneEditLabel.place(x=490,y=650)
    
    PhoneEditEntry = Entry(frame_operating,font=("Arial",16),fg="#000000",bg="#FFFFFF",width=30)
    PhoneEditEntry.place(x=490,y=680)
    
    
    AddressEditLabel = Label(frame_operating,text="ADDRESS (*)",font=("Arial Bold",16),fg="#000000",bg="#FFE7CE")
    AddressEditLabel.place(x=490,y=750)
    
    AddressEditEntry = Entry(frame_operating,font=("Arial",16),fg="#000000",bg="#FFFFFF",width=30)
    AddressEditEntry.place(x=490,y=780)
    
    
    StaffIDEditLabel = Label(frame_operating,text="STAFF ID (*)",font=("Arial Bold",16),fg="#000000",bg="#FFE7CE")
    StaffIDEditLabel.place(x=960,y=550)
    
    StaffIDEditEntry = Entry(frame_operating,font=("Arial",16),fg="#000000",bg="#FFFFFF",width=30)
    StaffIDEditEntry.place(x=960,y=580)
    
    
    WorkEditLabel = Label(frame_operating,text="WORK SINCE",font=("Arial Bold",16),fg="#000000",bg="#FFE7CE")
    WorkEditLabel.place(x=960,y=650)
    
    WorkEditEntry = Entry(frame_operating,font=("Arial",16),fg="#000000",bg="#FFFFFF",width=30)
    WorkEditEntry.place(x=960,y=680)
    
    
    UserEditLabel = Label(frame_operating,text="ACCOUNT",font=("Arial Bold",16),fg="#000000",bg="#FFE7CE")
    UserEditLabel.place(x=960,y=750)
    
    UserEditEntry = Entry(frame_operating,font=("Arial",16),fg="#000000",bg="#FFFFFF",width=14)
    UserEditEntry.place(x=960,y=780)
    
    
    PassEditLabel = Label(frame_operating,text="PASSWORD",font=("Arial Bold",16),fg="#000000",bg="#FFE7CE")
    PassEditLabel.place(x=1150,y=750)
    
    PassEditEntry = Entry(frame_operating,font=("Arial",16),fg="#000000",bg="#FFFFFF",width=14)
    PassEditEntry.place(x=1150,y=780)
    
    
    
    #=============================================================================================#     FUNCS LAYOUT
    #=============================================================================================#
    
    
    def display():
        try:
            #Connect to mysql
            myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
            cur = myconn.cursor()
            #print("Connected to Database!!")
        except:
            messagebox.showerror("Connection","Database connection not stablish!!")
            return
        
        command = "use userlogin"
        cur.execute(command)
        col = ("id","employee_ID","fullname","gender","position","phone_number","citizen_id","address","worker_since")

        EmployeeTable = Scrollbar(frame_operating,orient=VERTICAL)
        Listemployee = ttk.Treeview(frame_operating,columns = col,yscrollcommand=EmployeeTable.set, show="headings")
        EmployeeTable.config(command = Listemployee.yview)
        
        Listemployee.column("id",width=20)
        Listemployee.column("employee_ID",width=100)
        Listemployee.column("fullname",width=200)
        Listemployee.column("gender",width=100)
        Listemployee.column("position",width=150)
        Listemployee.column("phone_number",width=105)
        Listemployee.column("citizen_id",width=120)
        Listemployee.column("address",width=300)
        Listemployee.column("worker_since",width=100)


        Listemployee.heading("id",text="ID",anchor="center")
        Listemployee.heading("employee_ID",text="STAFF ID",anchor="center")
        Listemployee.heading("fullname",text="FULL NAME",anchor="center")
        Listemployee.heading("gender",text="GENDER",anchor="center")
        Listemployee.heading("position",text="POSITION",anchor="center")
        Listemployee.heading("phone_number",text="PHONE",anchor="center")
        Listemployee.heading("citizen_id",text="CITIZEN ID",anchor="center")
        Listemployee.heading("address",text="ADDRESS",anchor="center")
        Listemployee.heading("worker_since",text="WORK SINCE",anchor="center")

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")    

        command = 'select * from employee_info'
        cur.execute(command)
        
        myresult = cur.fetchall()
        for i in range (len(myresult)):
            myresult[i] = list(myresult[i])
            myresult[i].pop(0)
            myresult[i].insert(0,i+1)
            
        for i in range(len(myresult)):
            Listemployee.insert("",END,value = myresult[i],tags= "font")
        style.configure("Heading",font = ("Arial Bold",11))
        Listemployee.tag_configure("font",font = ("Arial",11))
        Listemployee.place(x = 0, y = 100,height=366,width=1208)
        
        
        NameEditEntry.delete(0,END)
        StaffIDEditEntry.delete(0,END)
        CTIDEditEntry.delete(0,END)
        GenderEditEntry.delete(0,END)
        PositionEditEntry.delete(0,END)
        PhoneEditEntry.delete(0,END)
        AddressEditEntry.delete(0,END)
        WorkEditEntry.delete(0,END)
        UserEditEntry.delete(0,END)
        PassEditEntry.delete(0,END)
        
        
        def mouse_enter(e):
            for sel in Listemployee.selection():
                    item = Listemployee.item(sel)
                    ID = [item['values'][1]]

            try:
                    myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
                    cur = myconn.cursor()
                    #print("Connected to Database!!")
            except:
                    messagebox.showerror("Connection","Database connection not stablish!!")
                    return
                    
            command = "use userlogin"
            cur.execute(command)
                    
            command = "select employee_ID from employee_info where employee_ID =%s"
            cur.execute(command,(ID))
            mystaffID = cur.fetchone()
            mystaffID = ''.join(mystaffID)
                    
                    
            command = "select fullname from employee_info where employee_ID =%s"
            cur.execute(command,(ID))
            mystaffname = cur.fetchone()
            mystaffname = ''.join(mystaffname)
                    
                    
            command = "select gender from employee_info where employee_ID =%s"
            cur.execute(command,(ID))
            mystaffgender = cur.fetchone()
            mystaffgender = ''.join(mystaffgender)
                    
                    
            command = "select position from employee_info where employee_ID =%s"
            cur.execute(command,(ID))
            mystaffposition = cur.fetchone()
            mystaffposition = ''.join(mystaffposition)
                    
                    
            command = "select phone_number from employee_info where employee_ID =%s"
            cur.execute(command,(ID))
            mystaffphone = cur.fetchone()
            mystaffphone = ''.join(mystaffphone)
            
                    
            command = "select citizen_id from employee_info where employee_ID =%s"
            cur.execute(command,(ID))
            mystaffCTID = cur.fetchone()
            mystaffCTID = ''.join(mystaffCTID)
            
            
            
            command = "select address from employee_info where employee_ID =%s"
            cur.execute(command,(ID))
            mystaffaddress = cur.fetchone()
            mystaffaddress = ''.join(mystaffaddress)
            

            
            command = "select worker_since from employee_info where employee_ID =%s"
            cur.execute(command,(ID))
            mystaffwork = cur.fetchone()
            #mystaffwork = ''.join(mystaffwork)
            
            

            NameEditEntry.delete(0,END)
            StaffIDEditEntry.delete(0,END)
            CTIDEditEntry.delete(0,END)
            GenderEditEntry.delete(0,END)
            PositionEditEntry.delete(0,END)
            PhoneEditEntry.delete(0,END)
            AddressEditEntry.delete(0,END)
            WorkEditEntry.delete(0,END)



            NameEditEntry.insert(0,mystaffname)
            StaffIDEditEntry.insert(0,mystaffID)
            CTIDEditEntry.insert(0,mystaffCTID)
            GenderEditEntry.insert(0,mystaffgender)
            PositionEditEntry.insert(0,mystaffposition)
            PhoneEditEntry.insert(0,mystaffphone)
            AddressEditEntry.insert(0,mystaffaddress)
            WorkEditEntry.insert(0,mystaffwork)
            
        
    
        Listemployee.bind("<<TreeviewSelect>>",mouse_enter)
        
        
    def search():
        name = NameEditEntry.get()
        ID = StaffIDEditEntry.get()
        CTID = CTIDEditEntry.get()
        gender = GenderEditEntry.get()
        position = PositionEditEntry.get()
        phone = PhoneEditEntry.get()
        address = AddressEditEntry.get()
        worksince = WorkEditEntry.get()
        
        
        try:
            #Connect to mysql
            myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
            cur = myconn.cursor()
            #print("Connected to Database!!")
        except:
            messagebox.showerror("Connection","Database connection not stablish!!")
            return

        command="use userlogin"
        cur.execute(command)
        
        
        if (ID==""and CTID=="" and phone=="" and address==""):
            messagebox.showwarning("Warning","Please enter ID, Citizen ID, phone number or address to get correct information!!")
        elif ID!="":
            try:
                command = "select employee_ID from employee_info where employee_ID =%s"
                cur.execute(command,(ID,))
                mystaffID = cur.fetchone()
                mystaffID = ''.join(mystaffID)
                        
                        
                command = "select fullname from employee_info where employee_ID =%s"
                cur.execute(command,(ID,))
                mystaffname = cur.fetchone()
                mystaffname = ''.join(mystaffname)
                        
                        
                command = "select gender from employee_info where employee_ID =%s"
                cur.execute(command,(ID,))
                mystaffgender = cur.fetchone()
                mystaffgender = ''.join(mystaffgender)
                        
                        
                command = "select position from employee_info where employee_ID =%s"
                cur.execute(command,(ID,))
                mystaffposition = cur.fetchone()
                mystaffposition = ''.join(mystaffposition)
                        
                        
                command = "select phone_number from employee_info where employee_ID =%s"
                cur.execute(command,(ID,))
                mystaffphone = cur.fetchone()
                mystaffphone = ''.join(mystaffphone)
                
                        
                command = "select citizen_id from employee_info where employee_ID =%s"
                cur.execute(command,(ID,))
                mystaffCTID = cur.fetchone()
                mystaffCTID = ''.join(mystaffCTID)
                
                
                
                command = "select address from employee_info where employee_ID =%s"
                cur.execute(command,(ID,))
                mystaffaddress = cur.fetchone()
                mystaffaddress = ''.join(mystaffaddress)
            
            
                
            
                command = "select worker_since from employee_info where employee_ID =%s"
                cur.execute(command,(ID,))
                mystaffwork = cur.fetchone()
                #mystaffwork = ''.join(mystaffwork)
            
            except:
                messagebox.showwarning("Warning","Don't have this stass information")
                
            NameEditEntry.delete(0,END)
            StaffIDEditEntry.delete(0,END)
            CTIDEditEntry.delete(0,END)
            GenderEditEntry.delete(0,END)
            PositionEditEntry.delete(0,END)
            PhoneEditEntry.delete(0,END)
            AddressEditEntry.delete(0,END)
            WorkEditEntry.delete(0,END)


            NameEditEntry.insert(0,mystaffname)
            StaffIDEditEntry.insert(0,mystaffID)
            CTIDEditEntry.insert(0,mystaffCTID)
            GenderEditEntry.insert(0,mystaffgender)
            PositionEditEntry.insert(0,mystaffposition)
            PhoneEditEntry.insert(0,mystaffphone)
            AddressEditEntry.insert(0,mystaffaddress)
            WorkEditEntry.insert(0,mystaffwork)
            
        elif CTID!="":
            try:
                command = "select employee_ID from employee_info where citizen_id =%s"
                cur.execute(command,(CTID,))
                mystaffID = cur.fetchone()
                mystaffID = ''.join(mystaffID)
                        
                        
                command = "select fullname from employee_info where citizen_id =%s"
                cur.execute(command,(CTID,))
                mystaffname = cur.fetchone()
                mystaffname = ''.join(mystaffname)
                        
                        
                command = "select gender from employee_info where citizen_id =%s"
                cur.execute(command,(CTID,))
                mystaffgender = cur.fetchone()
                mystaffgender = ''.join(mystaffgender)
                        
                        
                command = "select position from employee_info where citizen_id =%s"
                cur.execute(command,(CTID,))
                mystaffposition = cur.fetchone()
                mystaffposition = ''.join(mystaffposition)
                        
                        
                command = "select phone_number from employee_info where citizen_id =%s"
                cur.execute(command,(CTID,))
                mystaffphone = cur.fetchone()
                mystaffphone = ''.join(mystaffphone)
                
                        
                command = "select citizen_id from employee_info where citizen_id =%s"
                cur.execute(command,(CTID,))
                mystaffCTID = cur.fetchone()
                mystaffCTID = ''.join(mystaffCTID)
                
                
                
                command = "select address from employee_info where citizen_id =%s"
                cur.execute(command,(CTID,))
                mystaffaddress = cur.fetchone()
                mystaffaddress = ''.join(mystaffaddress)
                

                
                command = "select worker_since from employee_info where citizen_id =%s"
                cur.execute(command,(CTID,))
                mystaffwork = cur.fetchone()
                #mystaffwork = ''.join(mystaffwork)
            except:
                messagebox.showwarning("Warning","Don't have this stass information")
            
            
            
            NameEditEntry.delete(0,END)
            StaffIDEditEntry.delete(0,END)
            CTIDEditEntry.delete(0,END)
            GenderEditEntry.delete(0,END)
            PositionEditEntry.delete(0,END)
            PhoneEditEntry.delete(0,END)
            AddressEditEntry.delete(0,END)
            WorkEditEntry.delete(0,END)



            NameEditEntry.insert(0,mystaffname)
            StaffIDEditEntry.insert(0,mystaffID)
            CTIDEditEntry.insert(0,mystaffCTID)
            GenderEditEntry.insert(0,mystaffgender)
            PositionEditEntry.insert(0,mystaffposition)
            PhoneEditEntry.insert(0,mystaffphone)
            AddressEditEntry.insert(0,mystaffaddress)
            WorkEditEntry.insert(0,mystaffwork)
            
        elif phone!="":
            try:
                command = "select employee_ID from employee_info where phone_number =%s"
                cur.execute(command,(phone,))
                mystaffID = cur.fetchone()
                mystaffID = ''.join(mystaffID)
                        
                        
                command = "select fullname from employee_info where phone_number =%s"
                cur.execute(command,(phone,))
                mystaffname = cur.fetchone()
                mystaffname = ''.join(mystaffname)
                        
                        
                command = "select gender from employee_info where phone_number =%s"
                cur.execute(command,(phone,))
                mystaffgender = cur.fetchone()
                mystaffgender = ''.join(mystaffgender)
                        
                        
                command = "select position from employee_info where phone_number =%s"
                cur.execute(command,(phone,))
                mystaffposition = cur.fetchone()
                mystaffposition = ''.join(mystaffposition)
                        
                        
                command = "select phone_number from employee_info where phone_number =%s"
                cur.execute(command,(phone,))
                mystaffphone = cur.fetchone()
                mystaffphone = ''.join(mystaffphone)
                
                        
                command = "select citizen_id from employee_info where phone_number =%s"
                cur.execute(command,(phone,))
                mystaffCTID = cur.fetchone()
                mystaffCTID = ''.join(mystaffCTID)
                
                
                
                command = "select address from employee_info where phone_number =%s"
                cur.execute(command,(phone,))
                mystaffaddress = cur.fetchone()
                mystaffaddress = ''.join(mystaffaddress)
                

                
                command = "select worker_since from employee_info where phone_number =%s"
                cur.execute(command,(phone,))
                mystaffwork = cur.fetchone()
                #mystaffwork = ''.join(mystaffwork)
            except:
                messagebox.showwarning("Warning","Don't have this stass information")
            
            NameEditEntry.delete(0,END)
            StaffIDEditEntry.delete(0,END)
            CTIDEditEntry.delete(0,END)
            GenderEditEntry.delete(0,END)
            PositionEditEntry.delete(0,END)
            PhoneEditEntry.delete(0,END)
            AddressEditEntry.delete(0,END)
            WorkEditEntry.delete(0,END)



            NameEditEntry.insert(0,mystaffname)
            StaffIDEditEntry.insert(0,mystaffID)
            CTIDEditEntry.insert(0,mystaffCTID)
            GenderEditEntry.insert(0,mystaffgender)
            PositionEditEntry.insert(0,mystaffposition)
            PhoneEditEntry.insert(0,mystaffphone)
            AddressEditEntry.insert(0,mystaffaddress)
            WorkEditEntry.insert(0,mystaffwork)
            
        elif address!="":
            try:  
                command = "select employee_ID from employee_info where address =%s"
                cur.execute(command,(address,))
                mystaffID = cur.fetchone()
                mystaffID = ''.join(mystaffID)
                        
                        
                command = "select fullname from employee_info where address =%s"
                cur.execute(command,(address,))
                mystaffname = cur.fetchone()
                mystaffname = ''.join(mystaffname)
                        
                        
                command = "select gender from employee_info where address =%s"
                cur.execute(command,(address,))
                mystaffgender = cur.fetchone()
                mystaffgender = ''.join(mystaffgender)
                        
                        
                command = "select position from employee_info where address =%s"
                cur.execute(command,(address,))
                mystaffposition = cur.fetchone()
                mystaffposition = ''.join(mystaffposition)
                        
                        
                command = "select phone_number from employee_info where address =%s"
                cur.execute(command,(address,))
                mystaffphone = cur.fetchone()
                mystaffphone = ''.join(mystaffphone)
                
                        
                command = "select citizen_id from employee_info where address =%s"
                cur.execute(command,(address,))
                mystaffCTID = cur.fetchone()
                mystaffCTID = ''.join(mystaffCTID)
                
                
                
                command = "select address from employee_info where address =%s"
                cur.execute(command,(address,))
                mystaffaddress = cur.fetchone()
                mystaffaddress = ''.join(mystaffaddress)
                

                
                command = "select worker_since from employee_info where address =%s"
                cur.execute(command,(address,))
                mystaffwork = cur.fetchone()
                #mystaffwork = ''.join(mystaffwork)
            except:
                messagebox.showwarning("Warning","Don't have this stass information")
            
            NameEditEntry.delete(0,END)
            StaffIDEditEntry.delete(0,END)
            CTIDEditEntry.delete(0,END)
            GenderEditEntry.delete(0,END)
            PositionEditEntry.delete(0,END)
            PhoneEditEntry.delete(0,END)
            AddressEditEntry.delete(0,END)
            WorkEditEntry.delete(0,END)



            NameEditEntry.insert(0,mystaffname)
            StaffIDEditEntry.insert(0,mystaffID)
            CTIDEditEntry.insert(0,mystaffCTID)
            GenderEditEntry.insert(0,mystaffgender)
            PositionEditEntry.insert(0,mystaffposition)
            PhoneEditEntry.insert(0,mystaffphone)
            AddressEditEntry.insert(0,mystaffaddress)
            WorkEditEntry.insert(0,mystaffwork)
            
        elif (name!=""or position !="" or worksince=="" or gender!=""):
            messagebox.showwarning("Warning","Please enter ID, Citizen ID, phone number or address to get correct information!!")
        else:
            messagebox.showwarning("Warning","Don't have this stass information")
    
    def update():
        name = NameEditEntry.get()
        ID = StaffIDEditEntry.get()
        CTID = CTIDEditEntry.get()
        gender = GenderEditEntry.get()
        position = PositionEditEntry.get()
        phone = PhoneEditEntry.get()
        address = AddressEditEntry.get()
        worksince = WorkEditEntry.get()
        
        
        try:
            #Connect to mysql
            myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
            cur = myconn.cursor()
            #print("Connected to Database!!")
        except:
            messagebox.showerror("Connection","Database connection not stablish!!")
            return

        command="use userlogin"
        cur.execute(command)
        
        
        command = "Select position from employee_info where status ='online'"
        cur.execute(command)
        position_result = cur.fetchone()
        position_result = ''.join(position_result)
            
        if (position_result=="Cửa hàng trưởng"):
        
        
            command = "update employee_info set fullname = %s, gender = %s,position=%s,phone_number=%s,citizen_id=%s,address=%s,worker_since=%s where employee_ID=%s"
            cur.execute(command,(name,gender,position,phone,CTID,address,worksince,ID))
            myconn.commit()
            messagebox.showinfo("Notification","Your employee information has been updated!")
            NameEditEntry.delete(0,END)
            CTIDEditEntry.delete(0,END)
            GenderEditEntry.delete(0,END)
            PositionEditEntry.delete(0,END)
            PhoneEditEntry.delete(0,END)
            AddressEditEntry.delete(0,END)
            StaffIDEditEntry.delete(0,END)
            WorkEditEntry.delete(0,END)
            UserEditEntry.delete(0,END)
            PassEditEntry.delete(0,END)
            
        else:
            messagebox.showerror("Error","You are not enough permissions!!")
    
    def add():
        name = NameEditEntry.get()
        ID = StaffIDEditEntry.get()
        CTID = CTIDEditEntry.get()
        gender = GenderEditEntry.get()
        position = PositionEditEntry.get()
        phone = PhoneEditEntry.get()
        address = AddressEditEntry.get()
        worksince = WorkEditEntry.get()
        acc = UserEditEntry.get()
        pasw = PassEditEntry.get()
        
        try:
            #Connect to mysql
            myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
            cur = myconn.cursor()
            #print("Connected to Database!!")
        except:
            messagebox.showerror("Connection","Database connection not stablish!!")
            return

        command="use userlogin"
        cur.execute(command)
        
        
        command = "Select position from employee_info where status ='online'"
        cur.execute(command)
        position_result = cur.fetchone()
        position_result = ''.join(position_result)
            
        if (position_result=="Cửa hàng trưởng"):
            if( acc=="" or pasw==""):
                messagebox.showerror("Error","Please enter the Account and Password!!")
            else:
                if (name == "" or ID=="" or gender =="" or position =="" or phone=="" or CTID=="" or address=="" or worksince==""):
                    messagebox.showerror("Error","Please enter full information!!")
                else:    
                    command = "select * from employee_info where Username=%s"
                    cur.execute(command,(acc,))
                    myresult = cur.fetchone()
                    #print(myresult)
                    if myresult != None:
                            messagebox.showerror("Error","User Name already exists!!")
                    else:
                        
                        command="insert into employee_info(employee_ID,fullname,gender,position,phone_number,citizen_id,address,worker_since,Username,Password,status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'offline')"
                        cur.execute(command,(ID,name,gender,position,phone,CTID,address,worksince,acc,pasw))
                        myconn.commit()
                        messagebox.showinfo("Notification","Successfully add employees")
                        
                        NameEditEntry.delete(0,END)
                        CTIDEditEntry.delete(0,END)
                        GenderEditEntry.delete(0,END)
                        PositionEditEntry.delete(0,END)
                        PhoneEditEntry.delete(0,END)
                        AddressEditEntry.delete(0,END)
                        StaffIDEditEntry.delete(0,END)
                        WorkEditEntry.delete(0,END)
                        UserEditEntry.delete(0,END)
                        PassEditEntry.delete(0,END)
                        
        else:
            messagebox.showerror("Error","You are not enough permissions!!")
    
    def remove():
        ID = StaffIDEditEntry.get()
        try:
            #Connect to mysql
            myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
            cur = myconn.cursor()
            #print("Connected to Database!!")
        except:
            messagebox.showerror("Connection","Database connection not stablish!!")
            return

        command="use userlogin"
        cur.execute(command)
        
        
        command = "Select position from employee_info where status ='online'"
        cur.execute(command)
        position_result = cur.fetchone()
        position_result = ''.join(position_result)
            
        if (position_result=="Cửa hàng trưởng"):
            command = "delete from employee_info where employee_ID =%s"
            cur.execute(command,(ID,))
            myconn.commit()
            messagebox.showinfo("Notification","Employee has been removed from the store!!")
            
            NameEditEntry.delete(0,END)
            CTIDEditEntry.delete(0,END)
            GenderEditEntry.delete(0,END)
            PositionEditEntry.delete(0,END)
            PhoneEditEntry.delete(0,END)
            AddressEditEntry.delete(0,END)
            StaffIDEditEntry.delete(0,END)
            WorkEditEntry.delete(0,END)
            UserEditEntry.delete(0,END)
            PassEditEntry.delete(0,END)
        else:
            messagebox.showerror("Error","You are not enough permissions!!")
    
    def clear():
        NameEditEntry.delete(0,END)
        CTIDEditEntry.delete(0,END)
        GenderEditEntry.delete(0,END)
        PositionEditEntry.delete(0,END)
        PhoneEditEntry.delete(0,END)
        AddressEditEntry.delete(0,END)
        StaffIDEditEntry.delete(0,END)
        WorkEditEntry.delete(0,END)
        UserEditEntry.delete(0,END)
        PassEditEntry.delete(0,END)
    
    def mouse_enter(e):
        for sel in Listemployee.selection():
                    item = Listemployee.item(sel)
                    ID = [item['values'][1]]

        try:
                myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
                cur = myconn.cursor()
                #print("Connected to Database!!")
        except:
                messagebox.showerror("Connection","Database connection not stablish!!")
                return
                
        command = "use userlogin"
        cur.execute(command)
                
        command = "select employee_ID from employee_info where employee_ID =%s"
        cur.execute(command,(ID))
        mystaffID = cur.fetchone()
        mystaffID = ''.join(mystaffID)
                
                
        command = "select fullname from employee_info where employee_ID =%s"
        cur.execute(command,(ID))
        mystaffname = cur.fetchone()
        mystaffname = ''.join(mystaffname)
                
                
        command = "select gender from employee_info where employee_ID =%s"
        cur.execute(command,(ID))
        mystaffgender = cur.fetchone()
        mystaffgender = ''.join(mystaffgender)
                
                
        command = "select position from employee_info where employee_ID =%s"
        cur.execute(command,(ID))
        mystaffposition = cur.fetchone()
        mystaffposition = ''.join(mystaffposition)
                
                
        command = "select phone_number from employee_info where employee_ID =%s"
        cur.execute(command,(ID))
        mystaffphone = cur.fetchone()
        mystaffphone = ''.join(mystaffphone)
        
                
        command = "select citizen_id from employee_info where employee_ID =%s"
        cur.execute(command,(ID))
        mystaffCTID = cur.fetchone()
        mystaffCTID = ''.join(mystaffCTID)
        
        
        
        command = "select address from employee_info where employee_ID =%s"
        cur.execute(command,(ID))
        mystaffaddress = cur.fetchone()
        mystaffaddress = ''.join(mystaffaddress)
        

        
        command = "select worker_since from employee_info where employee_ID =%s"
        cur.execute(command,(ID))
        mystaffwork = cur.fetchone()
        #mystaffwork = ''.join(mystaffwork)
        
        

        NameEditEntry.delete(0,END)
        StaffIDEditEntry.delete(0,END)
        CTIDEditEntry.delete(0,END)
        GenderEditEntry.delete(0,END)
        PositionEditEntry.delete(0,END)
        PhoneEditEntry.delete(0,END)
        AddressEditEntry.delete(0,END)
        WorkEditEntry.delete(0,END)



        NameEditEntry.insert(0,mystaffname)
        StaffIDEditEntry.insert(0,mystaffID)
        CTIDEditEntry.insert(0,mystaffCTID)
        GenderEditEntry.insert(0,mystaffgender)
        PositionEditEntry.insert(0,mystaffposition)
        PhoneEditEntry.insert(0,mystaffphone)
        AddressEditEntry.insert(0,mystaffaddress)
        WorkEditEntry.insert(0,mystaffwork)
        
    #=============================================================================================#     BUTTONS LAYOUT
    #=============================================================================================#
    
    DisplayButton = Button(frame_operating,text="DISPLAY",font=("Arial",16),fg="#000000",bg="#FFFFFF",height=3,width=10,command=display)
    DisplayButton.place(x=40,y=830)
    
    SearchStaffButton = Button(frame_operating,text="SEARCH",font=("Arial",16),fg="#000000",bg="#FFFFFF",height=3,width=10,command=search)
    SearchStaffButton.place(x=240,y=830)
    
    
    UpdateStaffButton = Button(frame_operating,text="UPDATE",font=("Arial",16),fg="#000000",bg="#F6FA70",height=3,width=10,command=update)
    UpdateStaffButton.place(x=500,y=830)
    
    
    AddStaffButton = Button(frame_operating,text="ADD",font=("Arial",16),fg="#000000",bg="#00DFA2",height=3,width=10,command=add)
    AddStaffButton.place(x=700,y=830)
    
    
    RemoveStaffButton = Button(frame_operating,text="REMOVE",font=("Arial",16),fg="#000000",bg="#FF0060",height=3,width=10,command=remove)
    RemoveStaffButton.place(x=980,y=830)
    
    
    ClearStaffButton = Button(frame_operating,text="CLEAR",font=("Arial",16),fg="#000000",bg="#FFFFFF",height=3,width=10,command=clear)
    ClearStaffButton.place(x=1180,y=830)
    
    #=============================================================================================#
    #=============================================================================================#
    
    Staff_Label = Label(frame_operating,text="STAFF INFORMATION",font = ("Times New Roman Bold",30),bd=0,fg = "#000000",bg="#F2BED1",width=60)
    Staff_Label.place(x=0,y=465)
    
    
    command = "use userlogin"
    cur.execute(command)
    col = ("id","employee_ID","fullname","gender","position","phone_number","citizen_id","address","worker_since")

    EmployeeTable = Scrollbar(frame_operating,orient=VERTICAL)
    Listemployee = ttk.Treeview(frame_operating,columns = col,yscrollcommand=EmployeeTable.set, show="headings")
    EmployeeTable.config(command = Listemployee.yview)
    
    Listemployee.column("id",width=20)
    Listemployee.column("employee_ID",width=100)
    Listemployee.column("fullname",width=200)
    Listemployee.column("gender",width=100)
    Listemployee.column("position",width=150)
    Listemployee.column("phone_number",width=105)
    Listemployee.column("citizen_id",width=120)
    Listemployee.column("address",width=300)
    Listemployee.column("worker_since",width=100)


    Listemployee.heading("id",text="ID",anchor="center")
    Listemployee.heading("employee_ID",text="STAFF ID",anchor="center")
    Listemployee.heading("fullname",text="FULL NAME",anchor="center")
    Listemployee.heading("gender",text="GENDER",anchor="center")
    Listemployee.heading("position",text="POSITION",anchor="center")
    Listemployee.heading("phone_number",text="PHONE",anchor="center")
    Listemployee.heading("citizen_id",text="CITIZEN ID",anchor="center")
    Listemployee.heading("address",text="ADDRESS",anchor="center")
    Listemployee.heading("worker_since",text="WORK SINCE",anchor="center")

    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")    

    command = 'select * from employee_info'
    cur.execute(command)
    
    myresult = cur.fetchall()
    for i in range (len(myresult)):
        myresult[i] = list(myresult[i])
        myresult[i].pop(0)
        myresult[i].insert(0,i+1)
        
    for i in range(len(myresult)):
        Listemployee.insert("",END,value = myresult[i],tags= "font")
    style.configure("Heading",font = ("Arial Bold",11))
    Listemployee.tag_configure("font",font = ("Arial",11))
    Listemployee.place(x = 0, y = 100,height=366,width=1208)
    myconn.close()
    


    
    
    
    Listemployee.bind("<<TreeviewSelect>>",mouse_enter)
    
def warehouse():
    #==========================================================================#    STORE NAME LAYOUT
    #==========================================================================#
    StoreName = Label(frame_operating,text="SAYU STORE",font = ("Times New Roman Bold",45),bd=0,fg = "#000000",bg="#F2BED1",width=40)
    StoreName.place(x = 0,y = 0)
    
    Staff_Label = Label(frame_operating,text="WAREHOUSE",font = ("Times New Roman Bold",25),fg = "#000000",bg="#FFBDF7",width=60)
    Staff_Label.place(x=0,y=70)
    
    
    RECEIPT_Label = Label(frame_operating,anchor="nw",text="RECEIPT PRODUCTS",font = ("Arial Bold",15),fg = "#000000",bg="#FFBDF7",width=65,height=20)
    RECEIPT_Label.place(x=0,y=480)
    
    
    Bill_Label = Label(frame_operating,anchor="nw",text="BILL",font = ("Arial Bold",15),fg = "#000000",bg="#FFECEC",width=65,height=20)
    Bill_Label.place(x=750,y=480)
    
    
    #==========================================================================#    AVATAR LAYOUT
    #==========================================================================#
    AvatarInfo = Label(frame_operating,font = ("Arial Bold",16),fg="#000000",bg="#FFFFFF",height=17,width=22)
    AvatarInfo.place(x = 1200, y = 70)
    
    try:
        #Connect to mysql
        myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
        cur = myconn.cursor()
        #print("Connected to Database!!")
    except:
        messagebox.showerror("Connection","Database connection not stablish!!")
        return
    
    command = "use userlogin"
    cur.execute(command)
    
    command = "select * from employee_info where status ='online'"
    cur.execute(command)
    
    myresult = cur.fetchone()
    #print(myresult)

    command = "Select fullname from employee_info where status ='online'"
    cur.execute(command)
    name_result = cur.fetchone()
    name_result = ''.join(name_result)

    command = "Select position from employee_info where status ='online'"
    cur.execute(command)
    position_result = cur.fetchone()
    position_result = ''.join(position_result)

    Name_employ_label = Label(frame_operating,text="STAFF ON DUTY",font = ("Arial Bold",15),fg="#000000",bg="#FFFFFF")
    Name_employ_label.place(x=1210,y=80)
    
    Name_employee = Label(frame_operating,text="Name",font = ("Arial Bold",12),fg="#000000",bg="#FFFFFF")
    Name_employee.place(x = 1220,y = 150)
    
    Position_employee = Label(frame_operating,text="Position",font = ("Arial Bold",12),fg="#000000",bg="#FFFFFF")
    Position_employee.place(x = 1220,y = 225)
    
    
    DataName_Label = Label(frame_operating,text = name_result ,font = ("Arial",12),fg="#000000",bg="#FFFFFF")
    DataName_Label.place(x = 1220,y=175)
    
    
    DataPosition_Label = Label(frame_operating,text = position_result ,font = ("Arial",12),fg="#000000",bg="#FFFFFF")
    DataPosition_Label.place(x = 1220,y=250)
    
    
    
    try:
        #print("1")
        command = "create table receipt_shopping(id int not null auto_increment key, productID varchar(45) null, AmountBuy int null, Price int null, AmountOld int null, AmountNew int null , OldStatus varchar(20) null)"
        cur.execute(command)
        myconn.commit()
    except:
        try:
            command = "create table receipt_bill(id int not null auto_increment key,billcode int null, billdate date null,Cash int null, staffname varchar(45) null, staffID varchar(10) null)"
            cur.execute(command)
        except:
            pass
    
    
    #============================================================================================#      LABEL AND ENTRY
    #============================================================================================#
    IDProductLabel = Label(frame_operating,text = "PRODUCT ID",font=("Arial",14),bg="#FFBDF7")
    IDProductLabel.place(x=15,y=530)
    
    
    IDProductEntry = Entry(frame_operating,font=("Arial",14),width=28,bg="#FFBDF7")
    IDProductEntry.place(x=15,y=560)
    
    
    StatusProductLabel = Label(frame_operating,text = "STATUS",font=("Arial",14),bg="#FFBDF7")
    StatusProductLabel.place(x=15,y=600)
    
    StatusProductEntry = Entry(frame_operating,font=("Arial",14),width=28,bg="#FFBDF7")
    StatusProductEntry.place(x=15,y=630)
    
    
    
    
    TypeProductLabel = Label(frame_operating,text = "TYPE",font=("Arial",14),bg="#FFBDF7")
    TypeProductLabel.place(x=15,y=670)
    
    
    TypeProductEntry = Entry(frame_operating,font=("Arial",14),width=28,bg="#FFBDF7")
    TypeProductEntry.place(x=15,y=700)
    
    
    
    PriceProductLabel = Label(frame_operating,text = "PRICE",font=("Arial",14),bg="#FFBDF7")
    PriceProductLabel.place(x=400,y=530)
    
    PriceProductEntry = Entry(frame_operating,font=("Arial",14),width=28,bg="#FFBDF7")
    PriceProductEntry.place(x=400,y=560)
    
    
    
    AmountProductLabel = Label(frame_operating,text = "AMOUNT",font=("Arial",14),bg="#FFBDF7")
    AmountProductLabel.place(x=400,y=600)
    
    AmountProductEntry = Entry(frame_operating,font=("Arial",14),width=28)
    AmountProductEntry.place(x=400,y=630)
    
    
    
    
    BrandProductLabel = Label(frame_operating,text = "BRAND",font=("Arial",14),bg="#FFBDF7")
    BrandProductLabel.place(x=400,y=670)
    
    
    BrandProductEntry = Entry(frame_operating,font=("Arial",14),width=28,bg="#FFBDF7")
    BrandProductEntry.place(x=400,y=700)
    
    
    CashLabel = Label(frame_operating,text = "CASH",font=("Arial",14),bg="#FFBDF7")
    CashLabel.place(x=400,y=740)
    
    
    CashEntry = Entry(frame_operating,font=("Arial",14),width=28)
    CashEntry.place(x=400,y=770)
    
    
    
    SumLabel = Label(frame_operating,text = "SUM",font=("Arial",14),bg="#FFBDF7")
    SumLabel.place(x=15,y=740)
    
    
    SumEntry = Entry(frame_operating,font=("Arial",14),width=28)
    SumEntry.place(x=15,y=770)
    
    
    
    
    #============================================================================================#      FUNCS
    #============================================================================================#

    def display():
            try:
                myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
                cur = myconn.cursor()
                #print("Connected to Database!!")
            except:
                messagebox.showerror("Connection","Database connection not stablish!!")
                return
            
            
            command = "use userlogin"
            cur.execute(command)
            col = ("id","ProductID","PRODUCT","TYPE","PRICE","AMOUNT","STATUS","BRAND")

            ProductTable = Scrollbar(frame_operating,orient=VERTICAL)
            ListProduct = ttk.Treeview(frame_operating,columns = col,yscrollcommand=ProductTable.set,show="headings")
            ProductTable.config(command = ListProduct.yview)

            ListProduct.column("id",width=50)
            ListProduct.column("ProductID",width=150)
            ListProduct.column("PRODUCT",width=200)
            ListProduct.column("TYPE",width=100)
            ListProduct.column("PRICE",width=150)
            ListProduct.column("AMOUNT",width=60)
            ListProduct.column("STATUS",width=70)
            ListProduct.column("BRAND",width=100)


            ListProduct.heading("id",text="ID",anchor="center")
            ListProduct.heading("ProductID",text="PRODUCT ID",anchor="center")
            ListProduct.heading("PRODUCT",text="PRODUCT NAME",anchor="center")
            ListProduct.heading("TYPE",text="TYPE",anchor="center")
            ListProduct.heading("PRICE",text="PRICE",anchor="center")
            ListProduct.heading("AMOUNT",text="AMOUNT",anchor="center")
            ListProduct.heading("STATUS",text="STATUS",anchor="center")
            ListProduct.heading("BRAND",text="BRAND",anchor="center")

            style = ttk.Style()
            style.theme_use("default")
            style.map("Treeview")    

            command = 'select * from product'
            cur.execute(command)
            
            myresult = cur.fetchall()
            for i in range (len(myresult)):
                myresult[i] = list(myresult[i])
                myresult[i].pop(0)
                myresult[i].insert(0,i+1)
                
            for i in range(len(myresult)):
                ListProduct.insert("",END,value = myresult[i],tags= "font")
            style.configure("Heading",font = ("Arial Bold",11))
            ListProduct.tag_configure("font",font = ("Arial",11))
            ListProduct.place(x = 0, y = 110,height=375,width=1200)
            
            StatusProductEntry.delete(0,END)
            IDProductEntry.delete(0,END)
            TypeProductEntry.delete(0,END)
            PriceProductEntry.delete(0,END)
            AmountProductEntry.delete(0,END)
            BrandProductEntry.delete(0,END)
            
            
            
            
            sum = 0
            command = "select AmountBuy, Price from receipt_shopping"
            cur.execute(command)
            result = cur.fetchall()
            for r in range(len(result)):
                sum1 = result[r][0]*result[r][1]
                sum = sum1+sum
                    
            SumEntry.delete(0,END)
            SumEntry.insert(0,sum)
                

                    
            #BillCode = random.randint(100000,999999)
            BillDate = date.today()
            BillText.delete(1.0,END)
                    
            command = "select productID, AmountBuy, Price from receipt_shopping"
            cur.execute(command)
            result = cur.fetchall()
                
            BillText.insert(END,f"Receipt bill code: {BillCode}\t\t\t\t\t\t\t        Date: {BillDate}\n\n")
            BillText.insert(END,"***************************************************************************************************************\n")
            BillText.insert(END,"PRODUCT ID\t\t\t\tAMOUNT\t\t\t\t       PRICE\n\n")
            for i in range(len(result)):
                BillText.insert(END, f"{result[i][0]}\t\t\t\t         {result[i][1]}\t\t\t\t     {result[i][2]}\n\n")
            BillText.insert(END,"***************************************************************************************************************\n")
                            
                
                
            command = "select fullname from employee_info where status ='online'"
            cur.execute(command)
            mystaff = cur.fetchone()
            mystaff = ''.join(mystaff)
                
            BillText.insert(END,"STORE\t\t\t\tSTAFF\t\t\t\t         SUM\n\n")
            BillText.insert(END,f"SAYU\t\t\t\t{mystaff}\t\t\t\t     {SumEntry.get()}\n\n")
            
            
            
            def mouse_enter(e):
                try:
                    myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
                    cur = myconn.cursor()
                    #print("Connected to Database!!")
                except:
                    messagebox.showerror("Connection","Database connection not stablish!!")
                    return
                
                for sel in ListProduct.selection():
                    item = ListProduct.item(sel)
                    ID = [item['values'][1]]

                
                command = "use userlogin"
                cur.execute(command)
                
                command = "select STATUS from product where ProductID =%s"
                cur.execute(command,(ID))
                myname_product = cur.fetchone()
                myname_product = ''.join(myname_product)
                
                
                command = "select ProductID from product where ProductID =%s"
                cur.execute(command,(ID))
                myID_product = cur.fetchone()
                myID_product = ''.join(myID_product)
                
                
                command = "select TYPE from product where ProductID =%s"
                cur.execute(command,(ID))
                myType_product = cur.fetchone()
                myType_product = ''.join(myType_product)
                
                
                command = "select PRICE from product where ProductID =%s"
                cur.execute(command,(ID))
                myPrice_product = cur.fetchone()
                #myPrice_product = ''.join(myPrice_product)
                
                
                command = "select AMOUNT from product where ProductID =%s"
                cur.execute(command,(ID))
                myAmount_product = cur.fetchone()
                #myAmount_product = ''.join(myAmount_product)
                
                
                command = "select BRAND from product where ProductID =%s"
                cur.execute(command,(ID))
                myBrand_product = cur.fetchone()
                myBrand_product = ''.join(myBrand_product)
                            
                
                StatusProductEntry.delete(0,END)
                IDProductEntry.delete(0,END)
                TypeProductEntry.delete(0,END)
                PriceProductEntry.delete(0,END)
                AmountProductEntry.delete(0,END)
                BrandProductEntry.delete(0,END)
                
                
                
                StatusProductEntry.insert(0,myname_product)
                IDProductEntry.insert(0,myID_product)
                TypeProductEntry.insert(0,myType_product)
                PriceProductEntry.insert(0,myPrice_product)
                AmountProductEntry.insert(0,myAmount_product)
                BrandProductEntry.insert(0,myBrand_product)

            
            ListProduct.bind("<<TreeviewSelect>>",mouse_enter)
    
    
    def add():
        ID = IDProductEntry.get()
        amount = AmountProductEntry.get()
        price = PriceProductEntry.get()
        try:
            myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
            cur = myconn.cursor()
            #print("Connected to Database!!")
        except:
            messagebox.showerror("Connection","Database connection not stablish!!")
            return
        
        command="use userlogin"
        cur.execute(command)
        
        
        
        command = "select AMOUNT from product where ProductID = %s"
        cur.execute(command,(ID,))
        number = cur.fetchone()
        for i in number:
            c = i
        b = int(c) + 1
        
        
        command = "select STATUS from product where productID=%s"
        cur.execute(command,(ID,))
        result1 = cur.fetchone()
        for i in result1:
            status = i
        
        
        try:
            command = "create table receipt_shopping(id int not null auto_increment key, productID varchar(45) null, AmountBuy int null, Price int null, AmountOld int null, OldStatus varchar(20) null)"
            cur.execute(command)
            myconn.commit()
            
            
            
            command = "select productID from receipt_shopping where productID=%s"
            cur.execute(command,(ID,))
            result = cur.fetchone()
            if  result==None:
                command="insert into receipt_shopping(productID,Price,AmountBuy,AmountOld,OldStatus) values(%s,%s,%s,%s,%s)"
                cur.execute(command,(ID,price,c,amount,status))
                myconn.commit()
                
                
                
                
                command="update product set AMOUNT=%s where ProductID=%s"
                cur.execute(command,(b,ID))
                myconn.commit()
                messagebox.showinfo("Notification","The product is added in your cart!!")
            else:
                messagebox.showwarning("Warning","The product is already in the cart!!")
            
            
        except:
            command = "select productID from receipt_shopping where productID=%s"
            cur.execute(command,(ID,))
            result = cur.fetchone()
            if  result==None:
                command="insert into receipt_shopping(productID,Price,AmountBuy,AmountOld,OldStatus,AmountNew) values(%s,%s,%s,%s,%s,%s)"
                cur.execute(command,(ID,price,c,amount,status,b))
                myconn.commit()
                
                
                command="update product set AMOUNT=%s, STATUS='Còn' where ProductID=%s"
                cur.execute(command,(b,ID))
                myconn.commit()
                messagebox.showinfo("Notification","The product is added in your cart!!")
            else:
                messagebox.showwarning("Warning","The product is already in the cart!!")
        
    
    
    def confirm():
        ID = IDProductEntry.get()
        amount = AmountProductEntry.get()
        try:
            #Connect to mysql
            myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
            cur = myconn.cursor()
            #print("Connected to Database!!")
        except:
            messagebox.showerror("Connection","Database connection not stablish!!")
            return
    
        if amount=="" and ID !="":
                messagebox.showerror("Error","Please enter the Product Amount!!")
            
        elif amount != "" and ID !="":
            command = "use userlogin"
            cur.execute(command)
                
            command = "select AmountBuy from receipt_shopping where ProductID = %s"
            cur.execute(command,(ID,))
            number = cur.fetchone()
            for i in number:
                c = i
            b = int(c) + int(amount)
            
            command = "select AmountOld from receipt_shopping where ProductID = %s"
            cur.execute(command,(ID,))
            number = cur.fetchone()
            for i in number:
                old = i
            
            
            command = "select OldStatus from receipt_shopping where ProductID = %s"
            cur.execute(command,(ID,))
            number = cur.fetchone()
            for i in number:
                status = i
            
            
            
            command = "select productID from receipt_shopping where productID=%s"
            cur.execute(command,(ID,))
            result = cur.fetchone()         
            if result!=None: 
                if int(amount) >= 1:
                    command = "update receipt_shopping set AmountBuy = %s where productID=%s"
                    cur.execute(command,(amount,ID))
                    myconn.commit()
                    messagebox.showinfo("Notification","Your receipt cart has been updated!")
                    
                    command = "update receipt_shopping set AmountNew = %s where ProductID = %s"
                    cur.execute(command,(b,ID))
                    myconn.commit()
                    
                    command = "update product set AMOUNT = %s, STATUS = 'Còn' where ProductID = %s"
                    cur.execute(command,(b,ID))
                    myconn.commit()
                    
                    
                elif int(amount) == 0:
                    command = "update product set AMOUNT = %s, STATUS = %s where ProductID = %s"
                    cur.execute(command,(old,status,ID))
                    myconn.commit()
                    
                    
                    command = "delete from receipt_shopping where productID =%s"
                    cur.execute(command,(ID,))
                    myconn.commit()
                    messagebox.showinfo("Notification","The product has been removed from your cart!")
                    
                else:
                    messagebox.showerror("Error","Can not update your cart!!")
                
    
    def pay():
        sum = SumEntry.get()
        pay = CashEntry.get()
        try:
            myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
            cur = myconn.cursor()
            #print("Connected to Database!!")
        except:
            messagebox.showerror("Connection","Database connection not stablish!!")
        
        command="use userlogin"
        cur.execute(command)
        
        BillText.delete(1.0,END)
        
        if pay=="":
            messagebox.showerror("Error","You need to enter the cash!!")   
        elif pay!="":
            if pay<sum:
                messagebox.showerror("Error","You need to enter enough money!!")
            elif pay == sum:
                
                change=0
                command = "select productID, AmountBuy, Price from receipt_shopping"
                cur.execute(command)
                result = cur.fetchall()
                #print(result)
                
                BillText.insert(END,f"Receipt bill code: {BillCode}\t\t\t\t\t\t\t        Date: {BillDate}\n\n")
                BillText.insert(END,"***************************************************************************************************************\n")
                BillText.insert(END,"PRODUCT ID\t\t\t\tAMOUNT\t\t\t\t       PRICE\n\n")
                for i in range(len(result)):
                    BillText.insert(END, f"{result[i][0]}\t\t\t\t         {result[i][1]}\t\t\t\t     {result[i][2]}\n\n")
                BillText.insert(END,"***************************************************************************************************************\n")
                

                BillText.insert(END,f"SUM\t\t\t\t\t\t\t\t{sum}\n\n")
                BillText.insert(END,f"CASH\t\t\t\t\t\t\t\t{pay}\n\n")
                BillText.insert(END,f"CHANGE\t\t\t\t\t\t\t\t{change}\n\n")
                BillText.insert(END,"***************************************************************************************************************\n")
                
                
                command = "select fullname from employee_info where status ='online'"
                cur.execute(command)
                mystaff = cur.fetchone()
                mystaff = ''.join(mystaff)
                    
                BillText.insert(END,"STORE\t\t\t\tSTAFF\t\t\t\t\n\n")
                BillText.insert(END,f"SAYU\t\t\t\t{mystaff}\t\t\t\t\n\n")
                
                messagebox.showinfo("Notification","Goods import successfully")
                
                command = "Select fullname from employee_info where status ='online'"
                cur.execute(command)
                name_result = cur.fetchone()
                name_result = ''.join(name_result)

                command = "Select employee_ID from employee_info where status ='online'"
                cur.execute(command)
                ID_result = cur.fetchone()
                ID_result = ''.join(ID_result)
                
                command = "insert into receipt_bill(billcode,billdate,Cash,staffname,staffID) values(%s,%s,%s,%s,%s)"
                cur.execute(command,(BillCode,BillDate,sum,name_result,ID_result))
                
                command = "drop table receipt_shopping"
                cur.execute(command)

            
            elif pay>sum:
                command = "select productID, AmountBuy, Price from receipt_shopping"
                cur.execute(command)
                result = cur.fetchall()
                #print(result)
                
                change=int(pay)-int(sum)
                BillText.insert(END,f"Receipt bill code: {BillCode}\t\t\t\t\t\t\t        Date: {BillDate}\n\n")
                BillText.insert(END,"***************************************************************************************************************\n")
                BillText.insert(END,"PRODUCT ID\t\t\t\tAMOUNT\t\t\t\t       PRICE\n\n")
                for i in range(len(result)):
                    BillText.insert(END, f"{result[i][0]}\t\t\t\t         {result[i][1]}\t\t\t\t     {result[i][2]}\n\n")
                BillText.insert(END,"***************************************************************************************************************\n")
                

                BillText.insert(END,f"SUM\t\t\t\t\t\t\t\t{sum}\n\n")
                BillText.insert(END,f"CASH\t\t\t\t\t\t\t\t{pay}\n\n")
                BillText.insert(END,f"CHANGE\t\t\t\t\t\t\t\t{change}\n\n")
                BillText.insert(END,"***************************************************************************************************************\n")  

                
                command = "select fullname from employee_info where status ='online'"
                cur.execute(command)
                mystaff = cur.fetchone()
                mystaff = ''.join(mystaff)
                    
                BillText.insert(END,"STORE\t\t\t\tSTAFF\t\t\t\t\n\n")
                BillText.insert(END,f"SAYU\t\t\t\t{mystaff}\t\t\t\t\n\n")
                
                messagebox.showinfo("Notification","Goods import successfully")
                
                
                command = "Select fullname from employee_info where status ='online'"
                cur.execute(command)
                name_result = cur.fetchone()
                name_result = ''.join(name_result)

                command = "Select employee_ID from employee_info where status ='online'"
                cur.execute(command)
                ID_result = cur.fetchone()
                ID_result = ''.join(ID_result)
                
                command = "insert into receipt_bill(billcode,billdate,Cash,staffname,staffID) values(%s,%s,%s,%s,%s)"
                cur.execute(command,(BillCode,BillDate,sum,name_result,ID_result))
                
                
                
                
                
                command = "drop table receipt_shopping"
                cur.execute(command) 
        else:
            print('1')
    
    def printbill():
        bill=BillText.get(1.0,END)
        print(bill)
        file_dir = open(f"{BillCode}.txt","w",encoding="utf-8")
        file_dir.write(bill)
        file_dir.close()
        messagebox.showinfo("Notification","Your bill is printed!")
    
    def mouse_enter(e):
            for sel in ListProduct.selection():
                item = ListProduct.item(sel)
                ID = [item['values'][1]]

            try:
                myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
                cur = myconn.cursor()
                #print("Connected to Database!!")
            except:
                messagebox.showerror("Connection","Database connection not stablish!!")
                return
            
            command = "use userlogin"
            cur.execute(command)
            
            command = "select STATUS from product where ProductID =%s"
            cur.execute(command,(ID))
            myname_product = cur.fetchone()
            myname_product = ''.join(myname_product)
            
            
            command = "select ProductID from product where ProductID =%s"
            cur.execute(command,(ID))
            myID_product = cur.fetchone()
            myID_product = ''.join(myID_product)
            
            
            command = "select TYPE from product where ProductID =%s"
            cur.execute(command,(ID))
            myType_product = cur.fetchone()
            myType_product = ''.join(myType_product)
            
            
            command = "select PRICE from product where ProductID =%s"
            cur.execute(command,(ID))
            myPrice_product = cur.fetchone()
            #myPrice_product = ''.join(myPrice_product)
            
            
            command = "select AMOUNT from product where ProductID =%s"
            cur.execute(command,(ID))
            myAmount_product = cur.fetchone()
            #myAmount_product = ''.join(myAmount_product)
            
            
            command = "select BRAND from product where ProductID =%s"
            cur.execute(command,(ID))
            myBrand_product = cur.fetchone()
            myBrand_product = ''.join(myBrand_product)
                        
            
            StatusProductEntry.delete(0,END)
            IDProductEntry.delete(0,END)
            TypeProductEntry.delete(0,END)
            PriceProductEntry.delete(0,END)
            AmountProductEntry.delete(0,END)
            BrandProductEntry.delete(0,END)
            
            
            
            StatusProductEntry.insert(0,myname_product)
            IDProductEntry.insert(0,myID_product)
            TypeProductEntry.insert(0,myType_product)
            PriceProductEntry.insert(0,myPrice_product)
            AmountProductEntry.insert(0,myAmount_product)
            BrandProductEntry.insert(0,myBrand_product)

    
    #============================================================================================#      BUTTONS
    #============================================================================================#
    
    DiplayButton = Button(frame_operating,text="DISPLAY",font=("Arial",12),width=10,height=3,command=display)
    DiplayButton.place(x=50,y=850)
    
    
    AddButton = Button(frame_operating,text="ADD",font=("Arial",12),width=10,height=3,command=add)
    AddButton.place(x=190,y=850)
    
    
    CofirmButton = Button(frame_operating,text="CONFIRM",font=("Arial",12),width=10,height=3,command=confirm)
    CofirmButton.place(x=330,y=850)
    
    
    PayButton = Button(frame_operating,text="PAY",font=("Arial",12),width=10,height=3,command=pay)
    PayButton.place(x=470,y=850)
    
    
    PrintBillButton = Button(frame_operating,text="PRINT\nBILL",font=("Arial",12),width=10,height=3,command=printbill)
    PrintBillButton.place(x=610,y=850)
    
    
    #============================================================================================#
    #============================================================================================#
    
    command = "use userlogin"
    cur.execute(command)
    col = ("id","ProductID","PRODUCT","TYPE","PRICE","AMOUNT","STATUS","BRAND")

    ProductTable = Scrollbar(frame_operating,orient=VERTICAL)
    ListProduct = ttk.Treeview(frame_operating,columns = col,yscrollcommand=ProductTable.set,show="headings")
    ProductTable.config(command = ListProduct.yview)

    ListProduct.column("id",width=50)
    ListProduct.column("ProductID",width=150)
    ListProduct.column("PRODUCT",width=200)
    ListProduct.column("TYPE",width=100)
    ListProduct.column("PRICE",width=150)
    ListProduct.column("AMOUNT",width=60)
    ListProduct.column("STATUS",width=70)
    ListProduct.column("BRAND",width=100)


    ListProduct.heading("id",text="ID",anchor="center")
    ListProduct.heading("ProductID",text="PRODUCT ID",anchor="center")
    ListProduct.heading("PRODUCT",text="PRODUCT NAME",anchor="center")
    ListProduct.heading("TYPE",text="TYPE",anchor="center")
    ListProduct.heading("PRICE",text="PRICE",anchor="center")
    ListProduct.heading("AMOUNT",text="AMOUNT",anchor="center")
    ListProduct.heading("STATUS",text="STATUS",anchor="center")
    ListProduct.heading("BRAND",text="BRAND",anchor="center")

    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")    

    command = 'select * from product'
    cur.execute(command)
    
    myresult = cur.fetchall()
    for i in range (len(myresult)):
        myresult[i] = list(myresult[i])
        myresult[i].pop(0)
        myresult[i].insert(0,i+1)
        
    for i in range(len(myresult)):
        ListProduct.insert("",END,value = myresult[i],tags= "font")
    style.configure("Heading",font = ("Arial Bold",11))
    ListProduct.tag_configure("font",font = ("Arial",11))
    ListProduct.place(x = 0, y = 110,height=375,width=1200)
   

        
    sum = 0
    command = "select AmountBuy, Price from receipt_shopping"
    cur.execute(command)
    result = cur.fetchall()
    for r in range(len(result)):
        sum1 = result[r][0]*result[r][1]
        sum = sum1+sum
            
    SumEntry.delete(0,END)
    SumEntry.insert(0,sum)
        
        
    BillText = ScrolledText(frame_operating,font=("Arial Bold",12))
    BillText.place(x=750,y=510,width=695,height=420)
            
    BillCode = random.randint(100000,999999)
    BillDate = date.today()
    BillText.delete(1.0,END)
            
    command = "select productID, AmountBuy, Price from receipt_shopping"
    cur.execute(command)
    result = cur.fetchall()
        
    BillText.insert(END,f"Receipt bill code: {BillCode}\t\t\t\t\t\t\t        Date: {BillDate}\n\n")
    BillText.insert(END,"***************************************************************************************************************\n")
    BillText.insert(END,"PRODUCT ID\t\t\t\tAMOUNT\t\t\t\t       PRICE\n\n")
    for i in range(len(result)):
        BillText.insert(END, f"{result[i][0]}\t\t\t\t         {result[i][1]}\t\t\t\t     {result[i][2]}\n\n")
    BillText.insert(END,"***************************************************************************************************************\n")
                    
        
        
    command = "select fullname from employee_info where status ='online'"
    cur.execute(command)
    mystaff = cur.fetchone()
    mystaff = ''.join(mystaff)
        
    BillText.insert(END,"STORE\t\t\t\tSTAFF\t\t\t\t         SUM\n\n")
    BillText.insert(END,f"SAYU\t\t\t\t{mystaff}\t\t\t\t     {SumEntry.get()}\n\n")
    myconn.close()
    
    
    
    ListProduct.bind("<<TreeviewSelect>>",mouse_enter)

def revenue():
    #==========================================================================#    STORE NAME LAYOUT
    #==========================================================================#
    StoreName = Label(frame_operating,text="SAYU STORE",font = ("Times New Roman Bold",45),bd=0,fg = "#000000",bg="#F2BED1",width=40)
    StoreName.place(x = 0,y = 0)
    
    #==========================================================================#    AVATAR LAYOUT
    #==========================================================================#
    AvatarInfo = Label(frame_operating,font = ("Arial Bold",16),fg="#000000",bg="#FFFFFF",height=17,width=22)
    AvatarInfo.place(x = 1200, y = 70)
    
    try:
        #Connect to mysql
        myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
        cur = myconn.cursor()
        #print("Connected to Database!!")
    except:
        messagebox.showerror("Connection","Database connection not stablish!!")
        return
    
    command = "use userlogin"
    cur.execute(command)
    
    command = "select * from employee_info where status ='online'"
    cur.execute(command)
    
    myresult = cur.fetchone()
    #print(myresult)

    command = "Select fullname from employee_info where status ='online'"
    cur.execute(command)
    name_result = cur.fetchone()
    name_result = ''.join(name_result)

    command = "Select position from employee_info where status ='online'"
    cur.execute(command)
    position_result = cur.fetchone()
    position_result = ''.join(position_result)

    Name_employ_label = Label(frame_operating,text="STAFF ON DUTY",font = ("Arial Bold",15),fg="#000000",bg="#FFFFFF")
    Name_employ_label.place(x=1210,y=80)
    
    Name_employee = Label(frame_operating,text="Name",font = ("Arial Bold",12),fg="#000000",bg="#FFFFFF")
    Name_employee.place(x = 1220,y = 150)
    
    Position_employee = Label(frame_operating,text="Position",font = ("Arial Bold",12),fg="#000000",bg="#FFFFFF")
    Position_employee.place(x = 1220,y = 225)
    
    
    DataName_Label = Label(frame_operating,text = name_result ,font = ("Arial",12),fg="#000000",bg="#FFFFFF")
    DataName_Label.place(x = 1220,y=175)
    
    
    DataPosition_Label = Label(frame_operating,text = position_result ,font = ("Arial",12),fg="#000000",bg="#FFFFFF")
    DataPosition_Label.place(x = 1220,y=250)
    
    #====================================================================================#
    #====================================================================================#
    RevenueInfo = Label(frame_operating,anchor="nw",text="REVENUE",font = ("Times new roman Bold",25),fg="#000000",bg="#FFCDA8",height=12,width=60)
    RevenueInfo.place(x = 0, y = 70)
    
    RevenueTable = Label(frame_operating,anchor="n",text="REVENUE TABLE",font = ("Times new roman Bold",25),fg="#000000",bg="#F2BED1",height=12,width=75)
    RevenueTable.place(x=0,y=450)
    
    
    ImportInfo = Label(frame_operating,anchor="nw",text="IMPORT TABLE",font = ("Times new roman Bold",25),fg="#000000",bg="#FFCDA8",height=1,width=20)
    ImportInfo.place(x = 680, y = 70)
    
    
    #====================================================================================#
    #====================================================================================#
    
    command = "use userlogin"
    cur.execute(command)
    col = ("id","billcode","billdate","CustomerName","CustomerID","gender","PhoneNo","address","Cash","staffname","staffID")

    BillTable = Scrollbar(frame_operating,orient=VERTICAL)
    ListBill = ttk.Treeview(frame_operating,columns = col,yscrollcommand=BillTable.set,show="headings")
    BillTable.config(command = ListBill.yview)

    ListBill.column("id",width=50)
    ListBill.column("billcode",width=120)
    ListBill.column("billdate",width=120)
    ListBill.column("CustomerName",width=180)
    ListBill.column("CustomerID",width=150)
    ListBill.column("gender",width=80)
    ListBill.column("PhoneNo",width=100)
    ListBill.column("address",width=250)
    ListBill.column("Cash",width=80)
    ListBill.column("staffname",width=120)
    ListBill.column("staffID",width=100)


    ListBill.heading("id",text="ID",anchor="center")
    ListBill.heading("billcode",text="BILL CODE",anchor="center")
    ListBill.heading("billdate",text="BILL DATE",anchor="center")
    ListBill.heading("CustomerName",text="CUSTOMER NAME",anchor="center")
    ListBill.heading("CustomerID",text="CUSTOMER ID",anchor="center")
    ListBill.heading("gender",text="GENDER",anchor="center")
    ListBill.heading("PhoneNo",text="PHONE NO",anchor="center")
    ListBill.heading("address",text="ADDRESS",anchor="center")
    ListBill.heading("Cash",text="CASH",anchor="center")
    ListBill.heading("staffname",text="STAFF NAME",anchor="center")
    ListBill.heading("staffID",text="STAFF ID",anchor="center")

    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")    

    command = 'select * from bill'
    cur.execute(command)
    
    myresult = cur.fetchall()
    for i in range (len(myresult)):
        myresult[i] = list(myresult[i])
        myresult[i].pop(0)
        myresult[i].insert(0,i+1)
        
    for i in range(len(myresult)):
        ListBill.insert("",END,value = myresult[i],tags= "font")
    style.configure("Heading",font = ("Arial Bold",12))
    ListBill.tag_configure("font",font = ("Arial",12))
    ListBill.place(x = 0, y = 500,height=450,width=1450)
    
    
    
    command = "use userlogin"
    cur.execute(command)
    col = ("id","billcode","billdate","Cash","staffname","staffID")

    BillTable1 = Scrollbar(frame_operating,orient=VERTICAL)
    ListBill1 = ttk.Treeview(frame_operating,columns = col,yscrollcommand=BillTable1.set,show="headings")
    BillTable1.config(command = ListBill.yview)

    ListBill1.column("id",width=50)
    ListBill1.column("billcode",width=100)
    ListBill1.column("billdate",width=100)
    ListBill1.column("Cash",width=70)
    ListBill1.column("staffname",width=100)
    ListBill1.column("staffID",width=80)
    


    ListBill1.heading("id",text="ID",anchor="center")
    ListBill1.heading("billcode",text="BILL CODE",anchor="center")
    ListBill1.heading("billdate",text="BILL DATE",anchor="center")
    ListBill1.heading("Cash",text="CASH",anchor="center")
    ListBill1.heading("staffname",text="STAFF NAME",anchor="center")
    ListBill1.heading("staffID",text="STAFF ID",anchor="center")
    

    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")    

    command = 'select * from receipt_bill'
    cur.execute(command)
    
    myresult = cur.fetchall()
    for i in range (len(myresult)):
        myresult[i] = list(myresult[i])
        myresult[i].pop(0)
        myresult[i].insert(0,i+1)
        
    for i in range(len(myresult)):
        ListBill1.insert("",END,value = myresult[i],tags= "font")
    style.configure("Heading",font = ("Arial Bold",12))
    ListBill1.tag_configure("font",font = ("Arial",12))
    ListBill1.place(x = 455, y = 110,height=340,width=750)
    
    
    
    
    
    
    
    #======================================================================================================#
    #======================================================================================================#
    
    try:
        #Connect to mysql
        myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
        cur = myconn.cursor()
        #print("Connected to Database!!")
    except:
        messagebox.showerror("Connection","Database connection not stablish!!")
        return
    
    
    command="use userlogin"
    cur.execute(command)

    sum = 0
    command = "Select Cash from bill"
    cur.execute(command)
    revenue_result = cur.fetchall()
    #print(revenue_result)
    for r in range(len(revenue_result)):
        sum1 = revenue_result[r][0]*1
        sum=sum + sum1

    sum_nhap = 0
    command = "Select Cash from receipt_bill"
    cur.execute(command)
    revenue_result = cur.fetchall()
    #print(revenue_result)
    for r in range(len(revenue_result)):
        sum2 = revenue_result[r][0]*1
        sum_nhap=sum_nhap + sum2
    
    
    
    

    StoreRevenue = Label(frame_operating,text="STORE REVENUE",font = ("Times New Roman Bold",16),fg = "#000000",bg="#FFCDA8")
    StoreRevenue.place(x=20,y=150)

    EntryRevenue = Entry(frame_operating,font = ("Times New Roman Bold",16),fg = "#000000",bg="#00DFA2")
    EntryRevenue.place(x=20,y=180)
        
    
    ImporProduct = Label(frame_operating,text="IMPORT PRODUCT",font = ("Times New Roman Bold",16),fg = "#000000",bg="#FFCDA8")
    ImporProduct.place(x=20,y=230)
    
    
    EntryImport = Entry(frame_operating,font = ("Times New Roman Bold",16),fg = "#000000",bg="#FF0060")
    EntryImport.place(x=20,y=260)
    
        
    EntryImport.delete(0,END)
    EntryImport.insert(0,sum_nhap)
        
        
    EntryRevenue.delete(0,END)
    EntryRevenue.insert(0,sum)
    
def info():
    #==========================================================================#    STORE NAME LAYOUT
    #==========================================================================#
    StoreName = Label(frame_operating,text="SAYU STORE",font = ("Times New Roman Bold",45),bd=0,fg = "#000000",bg="#F2BED1",width=40)
    StoreName.place(x = 0,y = 0)
    
    #==========================================================================#    AVATAR LAYOUT
    #==========================================================================#
    AvatarInfo = Label(frame_operating,font = ("Arial Bold",16),fg="#000000",bg="#FFFFFF",height=17,width=22)
    AvatarInfo.place(x = 1200, y = 70)
    
    try:
        #Connect to mysql
        myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
        cur = myconn.cursor()
        #print("Connected to Database!!")
    except:
        messagebox.showerror("Connection","Database connection not stablish!!")
        return
    
    command = "use userlogin"
    cur.execute(command)
    
    command = "select * from employee_info where status ='online'"
    cur.execute(command)
    
    myresult = cur.fetchone()
    #print(myresult)

    command = "Select fullname from employee_info where status ='online'"
    cur.execute(command)
    name_result = cur.fetchone()
    name_result = ''.join(name_result)

    command = "Select position from employee_info where status ='online'"
    cur.execute(command)
    position_result = cur.fetchone()
    position_result = ''.join(position_result)

    Name_employ_label = Label(frame_operating,text="STAFF ON DUTY",font = ("Arial Bold",15),fg="#000000",bg="#FFFFFF")
    Name_employ_label.place(x=1210,y=80)
    
    Name_employee = Label(frame_operating,text="Name",font = ("Arial Bold",12),fg="#000000",bg="#FFFFFF")
    Name_employee.place(x = 1220,y = 150)
    
    Position_employee = Label(frame_operating,text="Position",font = ("Arial Bold",12),fg="#000000",bg="#FFFFFF")
    Position_employee.place(x = 1220,y = 225)
    
    
    DataName_Label = Label(frame_operating,text = name_result ,font = ("Arial",12),fg="#000000",bg="#FFFFFF")
    DataName_Label.place(x = 1220,y=175)
    
    
    DataPosition_Label = Label(frame_operating,text = position_result ,font = ("Arial",12),fg="#000000",bg="#FFFFFF")
    DataPosition_Label.place(x = 1220,y=250)
    
    
    #==========================================================================#    INFORMATION
    #==========================================================================#
    INFOMATION = Label(frame_operating,font = ("Times New Roman Bold",16),bd=0,fg = "#000000",bg="#FFCDA8",width=100,height=40)
    INFOMATION.place(x = 0,y = 70)
    
    
    LAP = Label(frame_operating,font = ("Times New Roman Bold",16),bd=0,fg = "#000000",bg="#FFCDA8",width=30,height=40)
    LAP.place(x = 1100,y = 400)
    
    #==========================================================================#    INFORMATION
    #==========================================================================#
    try:    
        command = "Select employee_ID from employee_info where status ='online'"
        cur.execute(command)
        ID = cur.fetchone()
        ID = ''.join(ID)

        command = "Select fullname from employee_info where status ='online'"
        cur.execute(command)
        name = cur.fetchone()
        name = ''.join(name)
        
        command = "Select gender from employee_info where status ='online'"
        cur.execute(command)
        gender = cur.fetchone()
        gender = ''.join(gender)
        
        
        command = "Select position from employee_info where status ='online'"
        cur.execute(command)
        position_result = cur.fetchone()
        position_result = ''.join(position_result)
        
        
        command = "Select phone_number from employee_info where status ='online'"
        cur.execute(command)
        phone = cur.fetchone()
        phone = ''.join(phone)
        
        
        command = "Select citizen_id from employee_info where status ='online'"
        cur.execute(command)
        CTID = cur.fetchone()
        CTID = ''.join(CTID)
        
        
        command = "Select address from employee_info where status ='online'"
        cur.execute(command)
        address = cur.fetchone()
        address = ''.join(address)
        
        
        command = "Select worker_since from employee_info where status ='online'"
        cur.execute(command)
        work = cur.fetchone()
        
        
        command = "Select Username from employee_info where status ='online'"
        cur.execute(command)
        user = cur.fetchone()
        user = ''.join(user)
    
    
        """command = "Select Password from employee_info where status ='online'"
        cur.execute(command)
        pasw = cur.fetchone()
        pasw = ''.join(pasw)"""
    except:
        command = "Select employee_ID from employee_info where status ='online'"
        cur.execute(command)
        ID = cur.fetchone()
        ID = ''.join(ID)
        
        command = "Select fullname from employee_info where status ='online'"
        cur.execute(command)
        name = cur.fetchone()
        name = ''.join(name)

        command = "Select gender from employee_info where status ='online'"
        cur.execute(command)
        gender = cur.fetchone()
        if gender == None:
            gender = "None"
        
        command = "Select position from employee_info where status ='online'"
        cur.execute(command)
        position_result = cur.fetchone()
        position_result = ''.join(position_result)
        
        command = "Select phone_number from employee_info where status ='online'"
        cur.execute(command)
        phone = cur.fetchone()
        if phone == None:
            phone = "None"
        
        command = "Select citizen_id from employee_info where status ='online'"
        cur.execute(command)
        CTID = cur.fetchone()
        if CTID == None:
            CTID = "None"
        
    
        command = "Select address from employee_info where status ='online'"
        cur.execute(command)
        address = cur.fetchone()
        if address == None:
            address = "None"
        
    
        command = "Select worker_since from employee_info where status ='online'"
        cur.execute(command)
        work = cur.fetchone()
        
        
        command = "Select Username from employee_info where status ='online'"
        cur.execute(command)
        user = cur.fetchone()
        user = ''.join(user)
    
    
    Info = Label(frame_operating,text="INFORMATION",font=("Times new roman",25),width=66,fg="#000000",bg="#FCE9F1")
    Info.place(x=4,y=70)
    
    
    
    
    NameLabel = Label(frame_operating,text = "FULL NAME",font=("Arial Bold",20),fg="#000000",bg="#FFCDA8")
    NameLabel.place(x=20,y=160)
    
    NameEntry =  Entry(frame_operating,font=("Arial",20),fg="#000000",bg="#FFCDA8")
    NameEntry.place(x=20,y=200) 
    
    NameEntry.delete(0,END)
    NameEntry.insert(0,name)


    IDLabel = Label(frame_operating,text = "STAFF ID",font=("Arial Bold",20),fg="#000000",bg="#FFCDA8")
    IDLabel.place(x=420,y=160)
    
    IDEntry =  Entry(frame_operating,font=("Arial",20),fg="#000000",bg="#FFCDA8")
    IDEntry.place(x=420,y=200) 
    
    IDEntry.delete(0,END)
    IDEntry.insert(0,ID)


    PositionLabel = Label(frame_operating,text = "POSITION",font=("Arial Bold",20),fg="#000000",bg="#FFCDA8")
    PositionLabel.place(x=820,y=160)
    
    PositionEntry =  Entry(frame_operating,font=("Arial",20),fg="#000000",bg="#FFCDA8")
    PositionEntry.place(x=820,y=200) 
    
    PositionEntry.delete(0,END)
    PositionEntry.insert(0,position_result)
    
    
    
    
    
    
    GenLabel = Label(frame_operating,text = "GENDER",font=("Arial Bold",20),fg="#000000",bg="#FFCDA8")
    GenLabel.place(x=20,y=300)
    
    GenEntry =  Entry(frame_operating,font=("Arial",20),fg="#000000",bg="#FFCDA8")
    GenEntry.place(x=20,y=340) 
    
    GenEntry.delete(0,END)
    GenEntry.insert(0,gender)


    PhoneLabel = Label(frame_operating,text = "PHONE NO",font=("Arial Bold",20),fg="#000000",bg="#FFCDA8")
    PhoneLabel.place(x=420,y=300)
    
    PhoneEntry =  Entry(frame_operating,font=("Arial",20),fg="#000000",bg="#FFCDA8")
    PhoneEntry.place(x=420,y=340) 
    
    PhoneEntry.delete(0,END)
    PhoneEntry.insert(0,phone)


    CTIDLabel = Label(frame_operating,text = "CITIZEN ID",font=("Arial Bold",20),fg="#000000",bg="#FFCDA8")
    CTIDLabel.place(x=820,y=300)
    
    CTIDEntry =  Entry(frame_operating,font=("Arial",20),fg="#000000",bg="#FFCDA8")
    CTIDEntry.place(x=820,y=340) 
    
    CTIDEntry.delete(0,END)
    CTIDEntry.insert(0,CTID)
    
    
    
    
    AddressLabel = Label(frame_operating,text = "ADDRESS",font=("Arial Bold",20),fg="#000000",bg="#FFCDA8")
    AddressLabel.place(x=20,y=440)
    
    AddressEntry =  Entry(frame_operating,font=("Arial",20),fg="#000000",bg="#FFCDA8",width=47)
    AddressEntry.place(x=20,y=480) 
    
    AddressEntry.delete(0,END)
    AddressEntry.insert(0,address)


    WorkLabel = Label(frame_operating,text = "FIRST DAY OF WORK",font=("Arial Bold",20),fg="#000000",bg="#FFCDA8")
    WorkLabel.place(x=820,y=440)
    
    WorkEntry =  Entry(frame_operating,font=("Arial",20),fg="#000000",bg="#FFCDA8")
    WorkEntry.place(x=820,y=480) 
    
    WorkEntry.delete(0,END)
    WorkEntry.insert(0,work)
    
    
    Infouser = Label(frame_operating,text="ACCOUNT INFORMATION",font=("Times new roman",25),width=80,fg="#000000",bg="#FCE9F1")
    Infouser.place(x=0,y=575)
    

    AccLabel = Label(frame_operating,text = "USER",font=("Arial Bold",18),fg="#000000",bg="#FFCDA8")
    AccLabel.place(x=20,y=650)
    
    AccEntry =  Entry(frame_operating,font=("Arial",20),fg="#000000",bg="#FFCDA8")
    AccEntry.place(x=20,y=680) 
    
    AccEntry.delete(0,END)
    AccEntry.insert(0,user)


    PassLabel1 = Label(frame_operating,text = "PASSWORD",font=("Arial Bold",18),fg="#000000",bg="#FFCDA8")
    PassLabel1.place(x=420,y=650)
    
    PassEntry1 =  Entry(frame_operating,font=("Arial",20),fg="#000000",bg="#FFCDA8")
    PassEntry1.place(x=420,y=680) 
    
    PassEntry1.delete(0,END)
    #PassEntry.insert(0,pasw)


    PassLabel2 = Label(frame_operating,text = "PASSWORD CONFIRM",font=("Arial Bold",18),fg="#000000",bg="#FFCDA8")
    PassLabel2.place(x=820,y=650)
    
    PassEntry2 =  Entry(frame_operating,font=("Arial",20),fg="#000000",bg="#FFCDA8")
    PassEntry2.place(x=820,y=680) 
    
    PassEntry2.delete(0,END)
    #PassEntry.insert(0,pasw)

    #==========================================================================================#    FUNCS
    #==========================================================================================#


    def display():
        try:
            #Connect to mysql
            myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
            cur = myconn.cursor()
            #print("Connected to Database!!")
        except:
            messagebox.showerror("Connection","Database connection not stablish!!")
            return
        
        
        command = "use userlogin"
        cur.execute(command)
        
        
        command = "Select employee_ID from employee_info where status ='online'"
        cur.execute(command)
        ID = cur.fetchone()
        ID = ''.join(ID)

        command = "Select fullname from employee_info where status ='online'"
        cur.execute(command)
        name = cur.fetchone()
        name = ''.join(name)
        
        command = "Select gender from employee_info where status ='online'"
        cur.execute(command)
        gender = cur.fetchone()
        gender = ''.join(gender)
        
        
        command = "Select position from employee_info where status ='online'"
        cur.execute(command)
        position_result = cur.fetchone()
        position_result = ''.join(position_result)
        
        
        command = "Select phone_number from employee_info where status ='online'"
        cur.execute(command)
        phone = cur.fetchone()
        phone = ''.join(phone)
        
        
        command = "Select citizen_id from employee_info where status ='online'"
        cur.execute(command)
        CTID = cur.fetchone()
        CTID = ''.join(CTID)
        
        
        command = "Select address from employee_info where status ='online'"
        cur.execute(command)
        address = cur.fetchone()
        address = ''.join(address)
        
        
        command = "Select worker_since from employee_info where status ='online'"
        cur.execute(command)
        work = cur.fetchone()
        
        
        command = "Select Username from employee_info where status ='online'"
        cur.execute(command)
        user = cur.fetchone()
        user = ''.join(user)
    

        AccEntry.delete(0,END)
        WorkEntry.delete(0,END)
        AddressEntry.delete(0,END)
        CTIDEntry.delete(0,END)
        PhoneEntry.delete(0,END)
        GenEntry.delete(0,END)
        PositionEntry.delete(0,END)
        IDEntry.delete(0,END)
        NameEntry.delete(0,END)
    
    
    
        AccEntry.insert(0,user)
        WorkEntry.insert(0,work)
        AddressEntry.insert(0,address)
        CTIDEntry.insert(0,CTID)
        PhoneEntry.insert(0,phone)
        GenEntry.insert(0,gender)
        PositionEntry.insert(0,position_result)
        IDEntry.insert(0,ID)
        NameEntry.insert(0,name)





    def update():
        name = NameEntry.get()
        acc  = AccEntry.get()
        position = PositionEntry.get()
        gender = GenEntry.get()
        address = AddressEntry.get()
        pasw1 = PassEntry1.get()
        pasw2 = PassEntry2.get()
        phone = PhoneEntry.get()
        CTID = CTIDEntry.get()
        work = WorkEntry.get()
        
        try:
            #Connect to mysql
            myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", database = "userlogin",auth_plugin='mysql_native_password')
            cur = myconn.cursor()
            #print("Connected to Database!!")
        except:
            messagebox.showerror("Connection","Database connection not stablish!!")
            return
        
        
        command = "Select employee_ID from employee_info where status ='online'"
        cur.execute(command)
        ID = cur.fetchone()
        ID = ''.join(ID)
        
        
        
        command = "use userlogin"
        cur.execute(command)
        
        if (name == "" or gender=="" or address=="" or pasw1=="" or pasw2=="" or phone=="" or CTID=="" or position=="" or work=="" or acc==""):
            messagebox.showerror("Error","Please enter information you want to update")
        elif pasw1!=pasw2:
            messagebox.showerror("Error","Your password dosen't match!!")
        else:
            command = "select * from employee_info where Username=%s"
            cur.execute(command,(acc,))
            myresult = cur.fetchone()
            #print(myresult)
            if myresult == None:
                messagebox.showerror("Error","User Name doesn't exists!!")
            else:
                command = "Select position from employee_info where status ='online'"
                cur.execute(command)
                positioncheck = cur.fetchone()
                positioncheck = ''.join(positioncheck)
                
                if positioncheck=="Cửa hàng trưởng":
                    command = "update employee_info set fullname=%s, gender=%s,position=%s,phone_number=%s,citizen_id=%s,address=%s,worker_since=%s,Username=%s,Password=%s where status='online'"
                    cur.execute(command,(name,gender,position,phone,CTID,address,work,acc,pasw1))
                    myconn.commit()
                    
                    AccEntry.delete(0,END)
                    WorkEntry.delete(0,END)
                    AddressEntry.delete(0,END)
                    CTIDEntry.delete(0,END)
                    PhoneEntry.delete(0,END)
                    GenEntry.delete(0,END)
                    PositionEntry.delete(0,END)
                    IDEntry.delete(0,END)
                    NameEntry.delete(0,END)
                    PassEntry1.delete(0,END)
                    PassEntry2.delete(0,END)
                    
                    messagebox.showinfo("Notification","Your information is updated!!")
                else:
                    command = "update employee_info set fullname=%s, gender=%s,phone_number=%s,citizen_id=%s,address=%s,Password=%s where status ='online'"
                    cur.execute(command,(name,gender,phone,CTID,address,pasw1))
                    myconn.commit()
                    
                    AccEntry.delete(0,END)
                    WorkEntry.delete(0,END)
                    AddressEntry.delete(0,END)
                    CTIDEntry.delete(0,END)
                    PhoneEntry.delete(0,END)
                    GenEntry.delete(0,END)
                    PositionEntry.delete(0,END)
                    IDEntry.delete(0,END)
                    NameEntry.delete(0,END)
                    PassEntry1.delete(0,END)
                    PassEntry2.delete(0,END)
                    
                    
                    messagebox.showinfo("Notification","Your information is updated!!")
    #==========================================================================================#    BUTTONS
    #==========================================================================================#
    
    Display = Button(frame_operating,text="DISPLAY",font=("Arial Bold",16),width=16,height=3,command=display)
    Display.place(x=250,y=800)
    
    
    Update = Button(frame_operating,text="UPDATE",font=("Arial Bold",16),width=16,height=3,bg="#F6FA70",command=update)
    Update.place(x=670,y=800)
    
    
#==================================================================#    icon img of window

icon = 'C:\\Users\\Admin\\Documents\\Tai_lieu_mon_hoc\\HKII_2022_2023\\Applied Programming in Engineering\\Final\\Image\\store_icon5.ico'
window_main.iconbitmap(icon)

#==================================================================#    FRAME
######## FRAME WINDOW

frame_main = Frame(window_main,background="#FDCEDF")
frame_main.pack(padx=5,pady=5,fill="both",expand=True)


######## FRAME OPERATING
home_img = 'C:\\Users\\Admin\\Documents\\Tai_lieu_mon_hoc\\HKII_2022_2023\\Applied Programming in Engineering\\Final\\Image\\pet_home3.png'
background_home = PhotoImage(file=home_img)
frame_operating = Frame(frame_main,background="#FDCEDF",width=1440,height=928,bd=0)
frame_operating.place(x=300,y=0)
Label(frame_operating,image=background_home).pack()

######## FRAME BUTTONS
frame_buttons = Frame(frame_main,background="#FDCEDF",width=300,height=950)
frame_buttons.place(x=0,y=0)

#==================================================================#    BUTTONS
#Buttons and Img's Buttons
######## Load Img

img_path = os.path.dirname(os.path.realpath(__file__))
img_home = customtkinter.CTkImage(Image.open(img_path + "\\Image\\home.png"),size=(35,35))

HomeButton = customtkinter.CTkButton(master=frame_buttons,
                       text = "Home               ",
                       image=img_home,
                       border_color="#F3EC9A",
                       corner_radius=12,
                       border_spacing=5,
                       compound="right",
                       anchor="e",
                       font = ("Arial Bold",14),
                       fg_color="#FFAAC9",
                       hover_color="#FFFFFF",
                       text_color="#000000",
                       command=home)
HomeButton.place(x = 30,y = 120)


img_path0 = os.path.dirname(os.path.realpath(__file__))
img_product = customtkinter.CTkImage(Image.open(img_path0 + "\\Image\\product3.png"),size=(35,35))

ProductButton = customtkinter.CTkButton(master=frame_buttons,
                       text = "Product            ",
                       image=img_product,
                       border_color="#F3EC9A",
                       corner_radius=12,
                       border_spacing=5,
                       compound="right",
                       anchor="e",
                       font = ("Arial Bold",14),
                       fg_color="#FFAAC9",
                       hover_color="#FFFFFF",
                       text_color="#000000",
                       command=product)
ProductButton.place(x = 30,y = 190)



img_path1 = os.path.dirname(os.path.realpath(__file__))
img_shoppingcart = customtkinter.CTkImage(Image.open(img_path1 + "\\Image\\Icongiohang.png"),size=(35,35))

ShoppingButton = customtkinter.CTkButton(master=frame_buttons,
                       text = "Shopping Cart ",
                       image=img_shoppingcart,
                       border_color="#F3EC9A",
                       corner_radius=12,
                       border_spacing=5,
                       compound="right",
                       anchor="e",
                       font = ("Arial Bold",14),
                       fg_color="#FFAAC9",
                       hover_color="#FFFFFF",
                       text_color="#000000",
                       command=shopping)
ShoppingButton.place(x = 30,y = 260)



img_path2 = os.path.dirname(os.path.realpath(__file__))
img_employee = customtkinter.CTkImage(Image.open(img_path2 + "\\Image\\employee.png"),size=(35,35))

EmployeeButton = customtkinter.CTkButton(master=frame_buttons,
                       text = "Employees      ",
                       image=img_employee,
                       border_color="#F3EC9A",
                       corner_radius=12,
                       border_spacing=5,
                       compound="right",
                       anchor="e",
                       font = ("Arial Bold",14),
                       fg_color="#FFAAC9",
                       hover_color="#FFFFFF",
                       text_color="#000000",
                       command=employee)
EmployeeButton.place(x = 30,y = 330)



img_path3 = os.path.dirname(os.path.realpath(__file__))
img_employee = customtkinter.CTkImage(Image.open(img_path3 + "\\Image\\warehouse1.png"),size=(35,35))

WarehouseButton = customtkinter.CTkButton(master=frame_buttons,
                       text = "Warehouse      ",
                       image=img_employee,
                       border_color="#F3EC9A",
                       corner_radius=12,
                       border_spacing=5,
                       compound="right",
                       anchor="e",
                       font = ("Arial Bold",14),
                       fg_color="#FFAAC9",
                       hover_color="#FFFFFF",
                       text_color="#000000",
                       command=warehouse)
WarehouseButton.place(x = 30,y = 400)



img_path4 = os.path.dirname(os.path.realpath(__file__))
img_revenue = customtkinter.CTkImage(Image.open(img_path4 + "\\Image\\doanhthu.png"),size=(35,35))

RevenueButton = customtkinter.CTkButton(master=frame_buttons,
                       text = "Revenue          ",
                       image=img_revenue,
                       border_color="#F3EC9A",
                       corner_radius=12,
                       border_spacing=5,
                       compound="right",
                       anchor="e",
                       font = ("Arial Bold",14),
                       fg_color="#FFAAC9",
                       hover_color="#FFFFFF",
                       text_color="#000000",
                       command=revenue)
RevenueButton.place(x = 30,y = 470)



img_path5 = os.path.dirname(os.path.realpath(__file__))
img_info = customtkinter.CTkImage(Image.open(img_path5 + "\\Image\\info2.png"),size=(35,35))

InfoButton = customtkinter.CTkButton(master=frame_buttons,
                       text = "Information      ",
                       image=img_info,
                       border_color="#F3EC9A",
                       corner_radius=12,
                       border_spacing=5,
                       compound="right",
                       anchor="e",
                       font = ("Arial Bold",14),
                       fg_color="#FFAAC9",
                       hover_color="#FFFFFF",
                       text_color="#000000",
                       command=info)
InfoButton.place(x = 30,y = 540)



#LOGOUT LEFT
img_path6 = os.path.dirname(os.path.realpath(__file__))
img_logout = customtkinter.CTkImage(Image.open(img_path6 + "\\Image\\logout2.png"),size=(35,35))

LogoutButton = customtkinter.CTkButton(master=frame_buttons,
                       text = "Log out            ",
                       image=img_logout,
                       border_color="#F3EC9A",
                       corner_radius=12,
                       border_spacing=5,
                       compound="right",
                       anchor="e",
                       font = ("Arial Bold",14),
                       fg_color="#FF0060",
                       hover_color="#FFFFFF",
                       text_color="#000000",
                       command=login)
LogoutButton.place(x = 30,y = 610)

#========================================================================================#
##### Labels
StoreName = Label(frame_operating,text="SAYU STORE",font = ("Times New Roman Bold",40),bd=0,fg = "#000000",bg="#947257")
StoreName.place(x = 555,y = 130)

window_main.mainloop()