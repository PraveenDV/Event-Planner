import customtkinter as ctk
import tkinter as tk
from tkcalendar import Calendar, DateEntry
import csv
from tkinter import messagebox
import json
import pickle

'''def update(event):
    plans=[]
    date=calendar.selection_get()
    ev=event_entry.get()
    location=location_entry.get()
    tasks=Task_entry.get()
    with open('data_files/plans.dat', 'rb+') as f:
      while True: 
        try:
            lines=pickle.load(f)
            for line in lines:
                if line[1] == event['Event']:
                    plans.append(line)
        except EOFError:
                #print(f"Skipping invalid JSON: {line}")
                break
        for i in plans:
            if i['Event'] == event['Event']:
                i['Date']=date
                i['Location of Event']=location
                i['Tasks']=tasks

      f.seek(0)
      f.truncate()

      for i in plans:
          pickle.dump(i, f)
'''
def update(event):
    date = calendar.selection_get()
    ev = event_entry.get()
    location = location_entry.get()
    tasks = Task_entry.get()

    with open('data_files/plans.txt', 'r+') as f:
        data = []
        try:
            while True:
                lines = json.load(f)
                for i in lines:
                    data.append()
        except EOFError:
            pass


        for i in range(len(data)):
            if data[i]['Event'] == event['Event']:
                data[i]['Date'] = str(date)
                data[i]['Location of Event'] = location
                data[i]['Tasks'] = tasks

        f.seek(0)
        for item in data:
            json.dump(item, f)
        f.truncate()

def clear_event():
    event_entry.delete(0, ctk.END)
    location_entry.delete(0, ctk.END)
    Task_entry.delete(0, ctk.END)
    calendar.selection_clear()

def addEntry():
    date=calendar.selection_get()
    event=event_entry.get()
    location=location_entry.get()
    tasks=Task_entry.get()
    if event and date and location:
        data_rec = {
            "Date": str(date),
            "Event": event,
            "Location of Event": location,
            "Tasks": tasks
        }
        with open('data_files\plans.txt', 'a') as write_file:        
            json.dump(data_rec, write_file)
            write_file.write('\n')
        messagebox.showinfo('',"Successfully added event!")
        clear_event()

    else:
        messagebox.showwarning('Warning', 'Please input required details')

planner_window = ctk.CTk()
planner_window.title("planner Page")
planner_window.geometry("800x600")
planner_window.configure(bg="light blue")
planner_window.grab_set()

calendar=Calendar(planner_window, selectmode='day', date_pattern='yyyy-mm-dd', cursor='hand2')
calendar.pack(pady=40)

event_entry=ctk.CTkEntry(planner_window, width=100, height=100, corner_radius=15, placeholder_text="Event Name")
event_entry.place(x=300, y=300)

location_entry=ctk.CTkEntry(planner_window, width=100, height=100, corner_radius=15, placeholder_text="Enter location")
location_entry.place(x=400, y=300)

Task_entry=ctk.CTkEntry(planner_window, width=100, height=100, corner_radius=15, placeholder_text="Enter Tasks")
Task_entry.place(x=350, y=400)

addEvent_btn=ctk.CTkButton(planner_window, width=20, height=20, corner_radius=15, text='Add Event', command=addEntry)
addEvent_btn.place(x=300, y=500)

cancel_btn=ctk.CTkButton(planner_window, width=20, height=20, corner_radius=15, text='Clear Selection', command=clear_event)
cancel_btn.place(x=400, y=500)

planner_window.mainloop()