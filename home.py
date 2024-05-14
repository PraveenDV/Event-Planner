import customtkinter as ctk
import subprocess
from tkinter import messagebox

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
    home_window, text="Plan an Event", command=plans_screen, font=("Arial", 18)
)

plans_button.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

# Create a button to open the announcements page
my_plans_button = ctk.CTkButton(home_window, text="View My Plans", font=("Arial", 18), command=view_my_plans)
my_plans_button.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

'''def open_announcement_options():
    announcement_options_window = ctk.CTkToplevel(master=home_window)
    announcement_options_window.title("Announcement Options")
    announcement_options_window.geometry("400x400")

    view_global_announcement_button = ctk.CTkButton(
        announcement_options_window,
        text="View Global Announcements",
        command=lambda: view_global_announcement(),
        font=("Arial", 16)
    )
    view_global_announcement_button.pack(pady=10)

    view_admin_announcement_button = ctk.CTkButton(
        announcement_options_window,
        text="View Admin Announcements",
        command=lambda: view_admin_announcement(),
        font=("Arial", 16)
    )
    view_admin_announcement_button.pack(pady=10)

    add_admin_announcement_button = ctk.CTkButton(
        announcement_options_window,
        text="Add Admin Announcement",
        command=lambda: add_admin_announcement(),
        font=("Arial", 16)
    )
    add_admin_announcement_button.pack(pady=10)

    add_global_announcement_button = ctk.CTkButton(
        announcement_options_window,
        text="Add Global Announcement",
        command=lambda: add_global_announcement(),
        font=("Arial", 16)
    )
    add_global_announcement_button.pack(pady=10)
'''

# Start the main event loop for the Admin main page
home_window.mainloop()
