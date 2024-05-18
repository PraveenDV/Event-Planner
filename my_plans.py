import customtkinter as ctk
import tkinter as tk
from tkcalendar import Calendar, DateEntry
import csv
from tkinter import messagebox
import pickle
import json
import os

view_plans_window = ctk.CTk()
view_plans_window.title("view_plans Page")
view_plans_window.geometry("800x600")
view_plans_window.grab_set()

title=ctk.CTkLabel(view_plans_window, width=50, height=30, text='My Plans')


def display_info(event):
   event_detail_screen=ctk.CTkToplevel(view_plans_window)
   event_detail_screen.title('Event Details')
   event_detail_screen.grab_set()

   eventInfo=ctk.CTkLabel(event_detail_screen, text=f"Event:{event['Event']}", width=10, height=10)
   eventInfo.pack()

   dateInfo=ctk.CTkLabel(event_detail_screen, text=f"Date:{event['Date']}", width=10, height=10)
   dateInfo.pack()

   locationInfo=ctk.CTkLabel(event_detail_screen, text=f"Location of Event:{event['Location of Event']}", width=10, height=10)
   locationInfo.pack()
         


def create_event_buttons(plans):
    for plan in plans:
        event_btn = ctk.CTkButton(view_plans_window, text=plan['Event'], width=20, height=20, command=lambda: display_info(plan))
        event_btn.pack(pady=5)



def display_event_btn():
    plans=[]
    if os.path.exists('data_files/plans.txt'):
     with open('data_files\plans.txt', 'r') as f: 
        for line in f:
            plan=json.loads(line.strip())
            plans.append(plan)
        create_event_buttons(plans)
    else:
       messagebox.showwarning('Warning', 'No plans found!')        
display_event_btn()



view_plans_window.mainloop()
