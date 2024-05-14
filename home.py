import customtkinter as ctk
import subprocess
from tkinter import messagebox
import threading

def view_my_plans():
    subprocess.run(['python', 'my_plans.py'], check=True)

def plans_screen():
    subprocess.run(['python', 'plan.py'], check=True)

# Create the Admin main page window
home_window = ctk.CTk()
home_window.title("Home Page")
home_window.geometry("800x600")
home_window.configure(bg="light blue")
home_window.grab_set()

# Create a button to open the admin timetable
plans_button = ctk.CTkButton(
    home_window, text="Plan an Event", command=threading.Thread(plans_screen).start, font=("Arial", 18)
)

plans_button.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

# Create a button to open the announcements page
my_plans_button = ctk.CTkButton(home_window, text="View My Plans", font=("Arial", 18), command=threading.Thread(view_my_plans).start)
my_plans_button.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

# Start the main event loop for the Admin main page
if __name__=='__main__':
    home_window.mainloop()
