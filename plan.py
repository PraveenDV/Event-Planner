import customtkinter as ctk
import tkinter as tk
from tkcalendar import Calendar, DateEntry
import csv
from tkinter import messagebox
import json

def addEntry():
    date=calendar.selection_get()
    event=event_entry.get()
    location=location_entry.get()
    if event and date and location:
        data_rec = {
            "Date": str(date),
            "Event": event,
            "Location of Event": location
        }
        with open('data_files\plans.txt', 'a', newline='') as write_file:        
            json.dump(data_rec, write_file)
            write_file.write('\n')
        messagebox.showinfo('',"Successfully added event!")

    else:
        messagebox.showwarning('Warning', 'Please input required details')

def clear_event():
    event_entry.delete(0, ctk.END)
    location_entry.delete(0, ctk.END)
    calendar.selection_clear()


planner_window = ctk.CTk()
planner_window.title("planner Page")
planner_window.geometry("800x600")
planner_window.configure(bg="light blue")
planner_window.grab_set()

calendar=Calendar(planner_window, selectmode='day', date_pattern='yyyy-mm-dd', cursor='hand2')
calendar.pack(pady=50)

event_entry=ctk.CTkEntry(planner_window, width=100, height=50, corner_radius=5, placeholder_text="Event Name")
event_entry.place(x=300, y=200)

location_entry=ctk.CTkEntry(planner_window, width=100, height=50, corner_radius=5, placeholder_text="Enter event location")
location_entry.place(x=400, y=200)

addEvent_btn=ctk.CTkButton(planner_window, width=20, height=20, corner_radius=5, text='Add Event', command=addEntry)
addEvent_btn.place(x=350, y=300)

cancel_btn=ctk.CTkButton(planner_window, width=20, height=20, corner_radius=5, text='Clear Selection', command=clear_event)
cancel_btn.place(x=450, y=300)

planner_window.mainloop()