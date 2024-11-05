import customtkinter as ctk
import tkinter as tk
from tkcalendar import Calendar, DateEntry
import csv
from tkinter import messagebox
import pickle
import json
import os
import subprocess
#from plan import update

view_plans_window = ctk.CTk()
view_plans_window.title("view_plans Page")
view_plans_window.geometry("800x600")
view_plans_window.grab_set()

title=ctk.CTkLabel(view_plans_window, width=50, height=30, text='My Plans')

def delete(event):
    # Get the event button
    for widget in view_plans_window.winfo_children():
        if isinstance(widget, ctk.CTkButton) and widget.cget("text") == event['Event']:
            widget.destroy()
            break

    # Delete the event info from the file
    plans=[]
    try:
      with open('data_files/plans.txt', 'r+') as f:
        lines = f.readlines()
        u=f.tell()
        for line in lines:
            try:
                if json.loads(line)['Event'] != event['Event']:
                    plans.append(line)
                    f.seek(u)
            except json.JSONDecodeError:
                print(f"Skipping invalid JSON: {line}")   
        f.truncate()

      with open('data_files/plans.txt', 'w') as f:
          for line in plans:
              f.write(line)
              f.write('\n')
    except Exception as e:
        messagebox.showerror('Error', str(e))


def display_info(event):
  try:
   event_detail_screen=ctk.CTkToplevel(view_plans_window)
   event_detail_screen.title('Event Details')
   event_detail_screen.geometry("400x400")
   event_detail_screen.grab_set()

   eventInfo=ctk.CTkLabel(event_detail_screen, text=f"Event:{event['Event']}", width=20, height=20)
   eventInfo.pack()

   dateInfo=ctk.CTkLabel(event_detail_screen, text=f"Date:{event['Date']}", width=20, height=20)
   dateInfo.pack()

   locationInfo=ctk.CTkLabel(event_detail_screen, text=f"Location of Event:{event['Location of Event']}", width=20, height=20)
   locationInfo.pack()

   TaskInfo=ctk.CTkLabel(event_detail_screen, text=f"Things To Do:{event['Tasks']}", width=20, height=20)
   TaskInfo.pack()

   delete_btn = ctk.CTkButton(event_detail_screen,text="Delete", width=30, height=30, command=lambda e=event: delete(e))
   delete_btn.pack(pady=5)

  except Exception as e:
     messagebox.showerror('Error', str(e))
    
def create_event_buttons(plans):
    for plan in plans:
        event_btn = ctk.CTkButton(view_plans_window, text=plan['Event'], width=20, height=20, command=lambda p=plan: display_info(p))
        event_btn.pack(pady=5)

def display_event_btn():
    plans = []
    if os.path.exists('data_files/plans.txt'):
        with open('data_files/plans.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line:  # Check if the line is not empty
                    #while True:
                     try:
                        lines = json.loads(line)
                        plans.append(lines)
                     except json.JSONDecodeError as e:
                        print(f"Skipping invalid JSON line: {lines}")
        if plans:
            create_event_buttons(plans)
        else:
            messagebox.showwarning('Warning', 'No valid plans found!')
    else:
        messagebox.showwarning('Warning', 'No plans found!')

display_event_btn()

if __name__=='__main__':
    view_plans_window.mainloop()
