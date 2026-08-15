import tkinter as tk
from PIL import Image, ImageTk
from database import staff_collection
import bcrypt
from tkinter import messagebox
from admin_dashboard import admin_dashboard
from caregiver_dashboard import caregiver_dashboard


# Create the main application window
window = tk.Tk()

# Window settings
window.title("Ellisam Daycare Management System")
window.geometry("1100x700")  # width and height
window.configure(bg="#FFFFFF")
window.resizable(False, False)  # stop it from resizing


left_frame = tk.Frame(
    window,  # belongs inside the main window
    bg="#B9E3F5",
    width=520,
    height=700
)

left_frame.pack(side="left", fill="y")
left_frame.pack_propagate(False)


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

logo.pack(pady=(80, 10))


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


right_frame = tk.Frame(
    window,
    bg="#FFFFFF",
    width=580,
    height=700
)

right_frame.pack(side="right", fill="both", expand=True)
right_frame.pack_propagate(False)


small_welcome = tk.Label(
    right_frame,
    text="WELCOME BACK",
    font=("Arial", 11, "bold"),
    bg="#FFFFFF",
    fg="#6FB6D6"
)

small_welcome.pack(
    anchor="w",
    padx=90,
    pady=(90, 8)
)


login_heading = tk.Label(
    right_frame,
    text="Sign in to your account",
    font=("Arial", 25, "bold"),
    bg="#FFFFFF",
    fg="#294A5A"
)

login_heading.pack(
    anchor="w",
    padx=90
)


subtitle = tk.Label(
    right_frame,
    text="Enter your details to access the daycare system.",
    font=("Arial", 10),
    bg="#FFFFFF",
    fg="#6F8A96"
)

subtitle.pack(
    anchor="w",
    padx=90,
    pady=(8, 35)
)


username_label = tk.Label(
    right_frame,
    text="Username",
    font=("Arial", 11, "bold"),
    bg="#FFFFFF",
    fg="#294A5A"
)

username_label.pack(
    anchor="w",
    padx=90
)


username_entry = tk.Entry(
    right_frame,
    font=("Arial", 12),
    bg="#EAF7FC",
    fg="#294A5A",
    relief="flat",
    bd=0
)

username_entry.pack(
    fill="x",
    padx=90,
    pady=(8, 20),
    ipady=12
)


password_label = tk.Label(
    right_frame,
    text="Password",
    font=("Arial", 11, "bold"),
    bg="#FFFFFF",
    fg="#294A5A"
)

password_label.pack(
    anchor="w",
    padx=90
)


password_entry = tk.Entry(
    right_frame,
    font=("Arial", 12),
    bg="#EAF7FC",
    fg="#294A5A",
    relief="flat",
    bd=0,
    show="*"
)

password_entry.pack(
    fill="x",
    padx=90,
    pady=(8, 10),
    ipady=12
)


forgot_password = tk.Label(
    right_frame,
    text="Forgot password?",
    font=("Arial", 9, "bold"),
    bg="#FFFFFF",
    fg="#6FB6D6",
    cursor="hand2"
)

forgot_password.pack(
    anchor="e",
    padx=90,
    pady=(0, 25)
)


def login():

    username = username_entry.get().strip()
    password = password_entry.get()

    if not username or not password:

        messagebox.showwarning(
            "Missing Information",
            "Please enter your username and password."
        )

        return


    user = staff_collection.find_one({
        "username": username
    })


    if user is None:

        messagebox.showerror(
            "Login Failed",
            "Invalid username or password."
        )

        return


    stored_password = user.get("password")


    if stored_password is None:

        messagebox.showerror(
            "Login Failed",
            "This account does not have a password."
        )

        return


    # MongoDB may return the bcrypt password as bytes
    # or as a string depending on how it was stored.

    if isinstance(stored_password, str):

        stored_password = stored_password.encode("utf-8")


    try:

        password_valid = bcrypt.checkpw(
            password.encode("utf-8"),
            stored_password
        )

    except (ValueError, TypeError):

        messagebox.showerror(
            "Login Failed",
            "The password stored for this account is invalid."
        )

        return


    if not password_valid:

        messagebox.showerror(
            "Login Failed",
            "Invalid username or password."
        )

        return


    role = user.get("role", "")


    # Caregiver
    if role == "Caregiver":

        caregiver_dashboard(window)


    # Admin
    elif role == "Admin":

        admin_dashboard(window)


    # Other roles
    else:

        messagebox.showerror(
            "Login Failed",
            "Your account does not have a valid role."
        )


login_button = tk.Button(
    right_frame,
    text="SIGN IN",
    font=("Arial", 12, "bold"),
    bg="#6FB6D6",
    fg="#FFFFFF",
    activebackground="#315A72",
    activeforeground="#FFFFFF",
    relief="flat",
    bd=0,
    cursor="hand2",
    command=login
)

login_button.pack(
    fill="x",
    padx=90,
    ipady=13
)


footer = tk.Label(
    right_frame,
    text="Elliesam Daycare Management System",
    font=("Arial", 9),
    bg="#FFFFFF",
    fg="#6F8A96"
)

footer.pack(
    side="bottom",
    pady=35
)


# Keep the application running
window.mainloop()