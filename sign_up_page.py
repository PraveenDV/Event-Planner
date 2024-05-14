import tkinter as tk
from tkinter import *
from tkinter import messagebox
import subprocess
from PIL import ImageTk, Image
import ast
import customtkinter as ctk

import threading

sign_up_window = ctk.CTk()
sign_up_window.title("Sign Up")
sign_up_window.geometry("800x800")
sign_up_window.grab_set()
sign_up_window.configure(bg="light blue")

def open_login_page():
    subprocess.run(['python', 'login_page.py'],check=True)
    

#roles=['Admin', 'Teacher', 'Student']


def sign_up():
    user=username.get()
    password=password_entry.get()
    confirm_pass=cpassword_entry.get()
    #role=role_var.get()
       
    if user and password==confirm_pass:
       
         try:
            file=open(r'data_files\users.txt', 'r+')
            d=file.read()
            r=ast.literal_eval(d)
            dict1={user:password}
            r.update(dict1)
            file.truncate(0)
            file.close()

            file=open(r'data_files\users.txt', 'w')
            w=file.write(str(r))

            messagebox.showinfo('Signup', "Succesfully signed up!")
            subprocess.run(['python', 'home.py'],check=True)
            sign_up_window.destroy()

         except:
            file=open(r'data_files\users.txt', 'w')
            data=str({'Username':'password'})
            file.write(data)
            file.close()

         
         
    else: 
            messagebox.showerror(message='Please enter username and password')
    
    


frame=ctk.CTkFrame(sign_up_window, width=250, height=230).place(x=440, y=120)
heading=ctk.CTkLabel(frame, width=25, text="Sign Up", font=('Century Gothic', 25, 'bold'))
heading.place(x=500, y=50)

#Label(frame, text='Username:', font=('Arial', 11)).place(x=500, y=150)
username=ctk.CTkEntry(frame, font=("Arial", 11), placeholder_text='Username')
username.place(x=500, y=150)

#Label(frame, text='Password:', font=('Arial', 11)).place(x=500, y=220)
password_entry=ctk.CTkEntry(frame, placeholder_text='Password', font=("Arial", 11),show='*')
password_entry.place(x=500, y=220)

#Label(frame, text='Confirm password:', font=('Arial', 11)).place(x=500, y=320)
cpassword_entry=ctk.CTkEntry(frame, placeholder_text="Confirm password", font=("Arial", 11),show='*')
cpassword_entry.place(x=500, y=300)

'''ctk.CTkLabel(frame, text='Sign up as?', font=('Arial', 11)).place(x=500, y=400)
role_var=ctk.StringVar(sign_up_window)
role_var.set(roles[0])
dropdown=ctk.CTkOptionMenu(sign_up_window, variable=role_var, values=roles, hover=True)
dropdown.place(x=500, y=420)'''

sign_up_button=ctk.CTkButton(frame, text="Sign Up", font=("Arial", 11, "bold"), width=20, command=threading.Thread(target=sign_up).start)
sign_up_button.place(x=500, y=480)

ctk.CTkLabel(frame, text="Already have an account?",  font=("Arial", 11)).place(x=500, y=580)
signin=ctk.CTkButton(frame, width=6, text='Sign in', fg_color='#57a1f8', command=threading.Thread(target=open_login_page).start)
signin.place(x=670, y=580)

if __name__=='__main__':
    sign_up_window.mainloop()
