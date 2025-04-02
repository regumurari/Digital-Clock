import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title('Digital Clock')
root.geometry('300x100')
root.resizable(False, False)

# Create and configure the label
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')

# Start the clock
update_time()

# Run the application
root.mainloop()