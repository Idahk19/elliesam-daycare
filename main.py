import tkinter as tk
from PIL import Image, ImageTk

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

image = Image.open("daycare.jpg")
image = image.resize((300, 200))
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(
    left_frame,
    image=photo,
    bg="#B9E3F5"
)

image_label.pack(pady=20)

logo = tk.Label(
    left_frame,
    text="ELLIESAM",
    font=("Arial", 30, "bold"),
    bg="#B9E3F5",
    fg="#315A72"
)

logo.pack(pady=(80, 10)) # vertical spacing above and below

daycare = tk.Label(
    left_frame,
    text="DAYCARE",
    font=("Arial", 14, "bold"),
    bg="#B9E3F5",
    fg="#315A72"
)
daycare.pack(pady=(0, 50))

welcome = tk.Label(
    left_frame,
    text="Where little hearts\nlearn, grow & shine",
    font=("Arial", 24, "bold"),
    bg="#B9E3F5",
    fg="#315A72",
    justify="center"
)
welcome.pack(pady=(0, 20))

description = tk.Label(
    left_frame,
    text="A simple and organized way to manage\n"
         "children, caregivers, attendance,\n"
         "activities and more.",
    font=("Arial", 11),
    bg="#B9E3F5",
    fg="#294A5A",
    justify="center"
)
description.pack(pady=(0, 30))

features = tk.Label(
    left_frame,
    text="Safe  |  Caring  |  Organized",
    font=("Arial", 11, "bold"),
    bg="#B9E3F5",
    fg="#315A72"
)

features.pack(pady=(0, 20))

# Keep the application running
window.mainloop()