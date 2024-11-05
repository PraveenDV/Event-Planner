import customtkinter as ctk
import subprocess
from tkinter import messagebox
import threading

def view_my_plans():
   try: 
    subprocess.run(['python', 'my_plans.py'], check=True)
   except subprocess.CalledProcessError as e:
      messagebox.showerror("Error",f"Failed to load{e}")

def plans_screen():
   try: 
    subprocess.run(['python', 'plan.py'], check=True)
   except subprocess.CalledProcessError as e:
      messagebox.showerror("Error",f"Failed to load{e}")    
    
# Create the home page window
home_window = ctk.CTk()
home_window.title("Home Page")
home_window.geometry("800x600")
home_window.configure(bg="light blue")
home_window.grab_set()

#def threadPlans():
   #     threading.Thread(target=view_my_plans).start()

#def threadPlanner():

# Create a button to open plans page
my_plans_button = ctk.CTkButton(home_window, text="View My Plans", font=("Arial", 18), command=lambda: threading.Thread(target=view_my_plans).start())
my_plans_button.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

# Create a button to open the planner
plans_button = ctk.CTkButton(
    home_window, text="Plan an Event", command=lambda: threading.Thread(target=plans_screen).start(), font=("Arial", 18)
)
plans_button.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)



# Start the main event loop for the home window
if __name__=='__main__':
    home_window.mainloop()
