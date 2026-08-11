import tkinter as tk

# Create the main application window
window = tk.Tk()

# Window settings
window.title("Ellisam Daycare Management System")
window.geometry("1100x700") # width and height
window.configure(bg="#FFFFFF")
window.resizable(False, False) # stop it from resizing

left_frame = tk.Frame(
    window, # belongs inside the main window
    bg="#B9E3F5",
    width=520,
    height=700
)

left_frame.pack(side="left", fill="y") # put to the left and fill vertically
left_frame.pack_propagate(False) # keep it at the specified width and length

# Keep the application running
window.mainloop()