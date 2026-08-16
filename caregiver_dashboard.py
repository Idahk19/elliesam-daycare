import tkinter as tk
from children import children
from attendance import attendance


def caregiver_dashboard(window):

    for item in window.winfo_children():
        item.destroy()

    window.title("Ellisam Daycare - Caregiver Dashboard")
    window.configure(bg="#FFFFFF")

    main_area = tk.Frame(
        window,
        bg="#FFFFFF"
    )

    main_area.pack(
        side="right",
        fill="both",
        expand=True
    )

    sidebar = tk.Frame(
        window,
        bg="#B9E3F5",
        width=230
    )

    sidebar.pack(
        side="left",
        fill="y"
    )

    sidebar.pack_propagate(False)

    brand = tk.Label(
        sidebar,
        text="ELLIESAM",
        font=("Arial", 22, "bold"),
        bg="#B9E3F5",
        fg="#315A72"
    )

    brand.pack(
        pady=(40, 0)
    )

    daycare = tk.Label(
        sidebar,
        text="DAYCARE",
        font=("Arial", 11, "bold"),
        bg="#B9E3F5",
        fg="#315A72"
    )

    daycare.pack(
        pady=(0, 45)
    )

    children_button = tk.Button(
        sidebar,
        text="Children",
        font=("Arial", 11, "bold"),
        bg="#FFFFFF",
        fg="#315A72",
        relief="flat",
        bd=0,
        anchor="w",
        padx=25,
        cursor="hand2",
        command=lambda: children(main_area, window)
    )

    children_button.pack(
        fill="x",
        padx=15,
        pady=5
    )

    attendance_button = tk.Button(
        sidebar,
        text="Attendance",
        font=("Arial", 11),
        bg="#B9E3F5",
        fg="#294A5A",
        relief="flat",
        bd=0,
        anchor="w",
        padx=25,
        cursor="hand2",
        command=lambda: attendance(main_area, window)
    )

    attendance_button.pack(
        fill="x",
        padx=15,
        pady=5
    )

    activities_button = tk.Button(
        sidebar,
        text="Activities",
        font=("Arial", 11),
        bg="#B9E3F5",
        fg="#294A5A",
        relief="flat",
        bd=0,
        anchor="w",
        padx=25,
        cursor="hand2"
    )

    activities_button.pack(
        fill="x",
        padx=15,
        pady=5
    )

    logout_button = tk.Button(
        sidebar,
        text="Logout",
        font=("Arial", 11, "bold"),
        bg="#B9E3F5",
        fg="#315A72",
        relief="flat",
        bd=0,
        anchor="w",
        padx=25,
        cursor="hand2"
    )

    logout_button.pack(
        side="bottom",
        fill="x",
        padx=15,
        pady=25
    )

    children(
        main_area,
        window
    )