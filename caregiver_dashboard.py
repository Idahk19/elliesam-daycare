import tkinter as tk

def caregiver_dashboard(window):
    for item in window.winfo_children():
        item.destroy()

    window.title("Ellisam Daycare - Caregiver Dashboard")
    window.configure(bg="#FFFFFF")
    main_area = tk.Frame(
    window,
    bg="#FFFFFF"
)
     