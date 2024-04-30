#Importing all the required modules(pickle,tkinter,PIL)
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter.font as tkFont
import pickle 

#Creating the main window using Tk() method.
project=tk.Tk()
project.title("Introduction")
i=Image.open(r"C:\Users\11e27\Desktop\airplane.png")

#Creating a frame to display the contents of the windows.
fr=tk.Frame()
fr.pack(side=tk.LEFT,expand=1)

#Inputting all the text which needs to be displayed on the introduction window.
tk.Label(fr,text="ID1110",font=("Cooper Black",38),compound="center").pack()
tk.Label(fr,text="AIRPORT RESERVATION SYSTEM",font=("Cooper Black",38),compound="center").pack()
tk.Label(fr,text="Submitted by:",font=("Cooper Black",30),compound="center").pack()
tk.Label(fr,text="Anju Sasikumar (142301004)",font=("Cooper Black",20),compound="center").pack()
tk.Label(fr,text="Muhamed Rizwan Mehboob (142301026",font=("Cooper Black",20),compound="center").pack()
tk.Label(fr,text="Lokesh Gadhipaka (112301007)",font=("Cooper Black",20),compound="center").pack()

#Defining the function to book the reservation.
def book_rsv(): 
    b=tk.Toplevel()
    b.title('BOOKING PORTAL') 
    tk.Label(b,text="Enter your details below:",font=("Cooper Black",30),compound="center").grid(row=0,column=1)
    tk.Label(b,text="",font=("Cooper Black",18),compound="center").grid(row=1,column=1)
    tk.Label(b,text="Passenger name",font=("Cooper Black",18),compound="center").grid(row=2,column=1)
    tk.Label(b,text="",font=("Cooper Black",18),compound="center").grid(row=3,column=1)
    tk.Label(b,text="Age",font=("Cooper Black",18),compound="center").grid(row=4,column=1)
    tk.Label(b,text="",font=("Cooper Black",18),compound="center").grid(row=5,column=10)
    tk.Label(b,text="Contact no:",font=("Cooper Black",18),compound="center").grid(row=6,column=1)
    tk.Label(b,text="",font=("Cooper Black",18),compound="center").grid(row=7,column=10)
    tk.Label(b,text="Passport Number",font=("Cooper Black",18),compound="center").grid(row=8,column=1)
    tk.Label(b,text="",font=("Cooper Black",18),compound="center").grid(row=9,column=10)
    tk.Label(b,text="Credit card number:",font=("Cooper Black",18),compound="center").grid(row=10,column=1)
    tk.Label(b,text="",font=("Cooper Black",18),compound="center").grid(row=11,column=10)
    tk.Label(b,text="Bank name:",font=("Cooper Black",18),compound="center").grid(row=12,column=1)
    tk.Label(b,text="",font=("Cooper Black",18),compound="center").grid(row=13,column=10)
    tk.Label(b,text="Date of departure:",font=("Cooper Black",18),compound="center").grid(row=14,column=1)
    tk.Label(b,text="",font=("Cooper Black",18),compound="center").grid(row=15,column=10)
    tk.Label(b,text="Flight name",font=("Cooper Black",18),compound="center").grid(row=16,column=1)
    tk.Label(b,text="",font=("Cooper Black",18),compound="center").grid(row=17,column=10)
    tk.Label(b,text="Source(place)",font=("Cooper Black",18),compound="center").grid(row=18,column=1)
    tk.Label(b,text="",font=("Cooper Black",18),compound="center").grid(row=19,column=10)
    tk.Label(b,text="Destination",font=("Cooper Black",18),compound="center").grid(row=20,column=1)
    
    #Retrieving the user input and storing them.
    e1,e2,e3,e4,e5,e6,e7,e8,e9,e10=tk.Entry(b),tk.Entry(b),tk.Entry(b),tk.Entry(b),tk.Entry(b),tk.Entry(b),tk.Entry(b),tk.Entry(b),tk.Entry(b),tk.Entry(b)
    e1.grid(row=2,column=8)
    e2.grid(row=4,column=8)
    e3.grid(row=6,column=8)
    e4.grid(row=8,column=8)
    e5.grid(row=10,column=8)
    e6.grid(row=12,column=8)
    e7.grid(row=14,column=8)
    e8.grid(row=16,column=8)
    e9.grid(row=18,column=8)
    e10.grid(row=20,column=8)
    
    def getInput():
        #Retreiving the user inputted reservation details.
        name=e1.get()
        age=e2.get()
        contact=e3.get()
        pn=e4.get()
        ccn=e5.get()
        bankn=e6.get()
        date=e7.get()
        flightn=e8.get()
        source=e9.get()
        dest=e10.get()
        b.destroy()
        global rsv
        rsv={"Passenger_name":name,"Age":age,"Contact_no":contact,"Passport_number":pn,"Credit_card_number":ccn,"Bank_name":bankn,
             "Date_of_departure":date,"Flight_name":flightn,"Source(place)":source,"Destination":dest}
        
        #Saving the reservation details to the binary file using pickle.
        r=open("data.dat",'ab') 
        pickle.dump(rsv,r) 
        r.close() 
    
    #Displaying buttons to provide options to return to main menu or to submit the reservation details    
    tk.Button(b,text="Go to Main Portal",font=("Cooper Black",18),compound="center",command=b.destroy).grid(row=21,column=9)
    tk.Button(b,text ="Submit",font=("Cooper Black",18),compound="center",command=getInput).grid(row=21,column=7)
    b.attributes('-fullscreen',True)
    b.mainloop()

#Defining a function to enquire the reservation details using passport number as reference.
def enquire_rsv():
    e=tk.Toplevel()
    e.title('Enquiry Portal')
    tk.Label(e,text="Enter your passport no:",font=("Cooper Black",30),compound="center").grid(row=0,column=10)
    ep=tk.Entry(e)  #Entry field for passport number.
    ep.grid(row=1,column=10)
    def getInput():
        p=ep.get()
        global s
        s=p
        check(s) 
    tk.Button(e,text ="Submit",font=("Cooper Black",18),compound="center",command=getInput).grid(row=1,column=12)
    e.attributes('-fullscreen',True)
    
    def check(s): 
        #Checks the reservation using  the passport number and retrieves the data and attributes correspoding to that number.
        r=open("data.dat",'rb')
        flag=False
        while True:
            try:
                rsv=pickle.load(r)
                if rsv['Passport_number']==s:
                    tk.Button(e,text="Go to Main Portal",font=("Cooper Black",18),compound="center",command=e.destroy).grid(row=21,column=10)
                    tk.Label(e,text=("Passenger_name:",rsv["Passenger_name"]),font=("Cooper Black",18),compound="center").grid(row=2,column=10)
                    tk.Label(e,text="",font=("Cooper Black",18),compound="center").grid(row=3,column=10)
                    tk.Label(e,text=("Age:",rsv["Age"]),font=("Cooper Black",18),compound="center").grid(row=4,column=10)
                    tk.Label(e,text="",font=("Cooper Black",18),compound="center").grid(row=5,column=10)
                    tk.Label(e,text=("Contact_no:",rsv["Contact_no"]),font=("Cooper Black",18),compound="center").grid(row=6,column=10)
                    tk.Label(e,text="",font=("Cooper Black",18),compound="center").grid(row=7,column=10)
                    tk.Label(e,text=("Passport_Number:",rsv['Passport_number']),font=("Cooper Black",18),compound="center").grid(row=8,column=10)
                    tk.Label(e,text="",font=("Cooper Black",18),compound="center").grid(row=9,column=10)
                    tk.Label(e,text=("Credit_card_number:",rsv["Credit_card_number"]),font=("Cooper Black",18),compound="center").grid(row=10,column=10)
                    tk.Label(e,text="",font=("Cooper Black",18),compound="center").grid(row=11,column=10)
                    tk.Label(e,text=("Bank_name:",rsv["Bank_name"]), font=("Cooper Black",18),compound="center").grid(row=12,column=10)
                    tk.Label(e,text="",font=("Cooper Black",18),compound="center").grid(row=13,column=20)
                    tk.Label(e,text=("Date_of_departure:",rsv["Date_of_departure"]),font=("Cooper Black",18),compound="center").grid(row=14,column=10)
                    tk.Label(e,text="",font=("Cooper Black",18),compound="center").grid(row=15,column=10)
                    tk.Label(e,text=("Flight_name:",rsv["Flight_name"]),font=("Cooper Black",18),compound="center").grid(row=16,column=10)
                    tk.Label(e,text="",font=("Cooper Black",18),compound="center").grid(row=17,column=10)
                    tk.Label(e,text=("Source(place):",rsv["Source(place)"]),font=("Cooper Black",18),compound="center").grid(row=18,column=10)
                    tk.Label(e,text="",font=("Cooper Black",18),compound="center").grid(row=19,column=10)
                    tk.Label(e,text=("Destination:",rsv["Destination"]),font=("Cooper Black",18),compound="center").grid(row=20,column=10)
                    flag=True        
            except EOFError:
                break
        if flag==False: #If there isn't a reservation corresponding to the user inputted passport number, displays the appropriate statement
            tk.Label(e,text="No such reservation found",font=("Cooper Black",20),compound="center").grid(row=2,column=10)
            tk.Button(e,text="Go to Main Portal",font=("Cooper Black",18),compound="center",command=e.destroy).grid(row=3,column=10)
        r.close()  
    e.mainloop()   
    
'''Defining a function to edit the reservations corresponding to the user inputted passport number. 
It will edit a component or a single detail at a time for the corresponding reservation'''
def edit_rsv(): 
    m=tk.Toplevel()
    m.title('Edit Portal')
    tk.Label(m,text="Enter your passport no:",font=("Cooper Black",30),compound="center").grid(row=0,column=10)
    et=tk.Entry(m)
    et.grid(row=0,column=15) #Entry field for passport number.
    
    def getInput(): #Defining a function to retrieve user input and to select the field to modify.
        p=et.get()
        global s
        s=p
        tk.Label(m,text="Which field you want to modify?",font=("Cooper Black",28),compound="center").grid(row=1,column=10)
        
        def callback(selection):
            d=selection
            tk.Label(m,text="Enter new value:",font=("Cooper Black",20),compound="center").grid(row=3,column=10)
            ez=tk.Entry(m) #Entry field for the new value of the attribute required to change.
            ez.grid(row=3,column=12)
            
            def ggf():
                n=ez.get()
                global v
                v=n
                modify(d,v)
            tk.Button(m,text ="Submit",font=("Cooper Black",18),compound="center",command=ggf).grid(row=3,column=15)
        
        #Creating a menu to display and to select the attribute required to modify.
        f1=tkFont.Font(family='Cooper Black', size=28)
        options ='Passenger_name Age Contact_no Credit_card_number Bank_name Date_of_departure Flight_name Source(place) Destination'.split()
        selected= tk.StringVar(m,value="FIELDS")
        om=tk.OptionMenu(m,selected,*options,command=callback)
        om.config(font=f1)
        f2=tkFont.Font(family='Cooper Black', size=20)
        menu=m.nametowidget(om.menuname)
        menu.config(font=f2)
        om.grid(row=2,column=10,padx=100,pady=10)
        
        def modify(d,v):
            r=open("data.dat",'ab+')
            r.seek(0)
            flag=False
            while True:
                try:
                    rsv=pickle.load(r)
                    if rsv["Passport_number"]==s: #Storing the modified attribute to the binary file.
                        rsv[d]=v
                        pickle.dump(rsv,r)
                        flag=True                     
                except EOFError:
                    break
            r.close()
            tk.Button(m,text="Go to Main Portal",font=("Cooper Black",18),compound="center",command=m.destroy).grid(row=4,column=10)
            r.close()
    tk.Button(m,text ="Submit",font=("Cooper Black",18),compound="center",command=getInput).grid(row=0,column=20)
    m.attributes('-fullscreen',True)
    m.mainloop()

# Defining a function to cancel the reservation corresponding to the passport number.
def cancel_rsv():
    d=tk.Toplevel()
    d.title('Cancel Portal')
    
    # Entry field to input the passport number whose attributes we are required to modify.
    tk.Label(d,text="Enter your passport no:",font=("Cooper Black",30),compound="center").grid(row=0,column=10)
    el=tk.Entry(d)
    el.grid(row=1,column=10)
    
    # Defining the function that will help to delete the reservation corresponding to the provided passport number.
    def DEL(s): 
        r=open ("data.dat","rb")
        bh=[]
        while True:
            try:
                bs=pickle.load(r) # load() is used with try and except blocks to prevent EOF error.
                bh.append(bs)
            except EOFError: 
                break
        r.close()
        
        # Rewriting all the records except the one we are going to delete.
        r=open("data.dat","wb")
        for x in bh:
            if x["Passport_number"]==s: 
                continue
            pickle.dump(x,r)
        r.close()
    
    def getInput():
        p=el.get()
        global s
        s=p
        DEL(s)
    
    # Creating buttons to provide option to go back to submit the change or go back to main menu.
    tk.Button(d,text ="Submit",font=("Cooper Black",18),compound="center",command=getInput).grid(row=1,column=12)
    tk.Button(d,text="Go to Main Portal",font=("Cooper Black",18),compound="center",command=d.destroy).grid(row=2,column=10)
    d.attributes('-fullscreen',True)
    d.mainloop()

# Defining the function to create the main menu where we can choose the operation that the user require.
def airline():
    bp=tk.Toplevel()
    bp.title("Main portal")
    global i
    i=ImageTk.PhotoImage(i)
    il=tk.Label(bp,image=i) # Using PhotoImage function to display an image in the main menu.
    il.pack()
    tk.Label(bp,text="Welcome to Airport Reservation System",font=("Cooper Black",38),compound="center").pack()
    tk.Label(bp,text="Main menu",font=("Cooper Black",25),bg="lemon chiffon",compound="center").pack()
    tk.Button(bp,text="Book Reservation",font=("Cooper Black",20),compound="center",command=book_rsv).pack()
    tk.Button(bp,text="Enquire Reservation",font=("Cooper Black",20),compound="center",command=enquire_rsv).pack()
    tk.Button(bp,text="Modify Reservation",font=("Cooper Black",20),compound="center",command=edit_rsv).pack()
    tk.Button(bp,text="Cancel Reservation",font=("Cooper Black",20),compound="center",command=cancel_rsv).pack()
    tk.Button(bp,text="Exit Portal",font=("Cooper Black",20),compound="center",command=bp.destroy).pack()
    bp.attributes('-fullscreen',True)

# Displays options in the introduction page which can redirect to main menu or exit the interface.
bn=tk.Button(fr,text ="Proceed to Project",font=("Cooper Black",25),bg="lemon chiffon",compound="center",command=airline).pack()   
bc=tk.Button(fr,text ="Exit",font=("Cooper Black",25),bg="lemon chiffon",compound="center",command=project.destroy).pack()                                                                                                                                                                                                        
project.attributes('-fullscreen',True)
project.mainloop()































































































































































