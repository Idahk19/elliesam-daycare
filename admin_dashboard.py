import tkinter as tk

def admin_dashboard(window):
    for item in window.winfo_children():
        item.destroy()

    window.title("Ellisam Daycare - Admin Dashboard")
    window.configure(bg="#FFFFFF")

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

    brand.pack(pady=(40, 0))

    daycare = tk.Label(
        sidebar,
        text="DAYCARE",
        font=("Arial", 11, "bold"),
        bg="#B9E3F5",
        fg="#315A72"
    )

    daycare.pack(pady=(0, 45))

    dashboard_button = tk.Button(
        sidebar,
        text="Dashboard",
        font=("Arial", 11, "bold"),
        bg="#FFFFFF",
        fg="#315A72",
        relief="flat",
        bd=0,
        anchor="w",
        padx=25,
        cursor="hand2"
    )

    dashboard_button.pack(
        fill="x",
        padx=15,
        pady=5
    )

    children_button = tk.Button(
        sidebar,
        text="Children",
        font=("Arial", 11),
        bg="#B9E3F5",
        fg="#294A5A",
        relief="flat",
        bd=0,
        anchor="w",
        padx=25,
        cursor="hand2"
    )

    children_button.pack(
        fill="x",
        padx=15,
        pady=5
    )

    staff_button = tk.Button(
        sidebar,
        text="Staff",
        font=("Arial", 11),
        bg="#B9E3F5",
        fg="#294A5A",
        relief="flat",
        bd=0,
        anchor="w",
        padx=25,
        cursor="hand2"
    )

    staff_button.pack(
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
        cursor="hand2"
    )

    attendance_button.pack(
        fill="x",
        padx=15,
        pady=5
    )

    payments_button = tk.Button(
        sidebar,
        text="Payments",
        font=("Arial", 11),
        bg="#B9E3F5",
        fg="#294A5A",
        relief="flat",
        bd=0,
        anchor="w",
        padx=25,
        cursor="hand2"
    )

    payments_button.pack(
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

    reports_button = tk.Button(
        sidebar,
        text="Reports",
        font=("Arial", 11),
        bg="#B9E3F5",
        fg="#294A5A",
        relief="flat",
        bd=0,
        anchor="w",
        padx=25,
        cursor="hand2"
    )

    reports_button.pack(
        fill="x",
        padx=15,
        pady=5
    )

    settings_button = tk.Button(
        sidebar,
        text="Settings",
        font=("Arial", 11),
        bg="#B9E3F5",
        fg="#294A5A",
        relief="flat",
        bd=0,
        anchor="w",
        padx=25,
        cursor="hand2"
    )

    settings_button.pack(
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

    main_area = tk.Frame(
        window,
        bg="#FFFFFF"
    )

    main_area.pack(
        side="right",
        fill="both",
        expand=True
    )

    welcome = tk.Label(
        main_area,
        text="Welcome to the Admin Dashboard",
        font=("Arial", 24, "bold"),
        bg="#FFFFFF",
        fg="#294A5A"
    )

    welcome.pack(
        anchor="w",
        padx=45,
        pady=(50, 10)
    )

    subtitle = tk.Label(
        main_area,
        text="Manage your daycare from one place.",
        font=("Arial", 11),
        bg="#FFFFFF",
        fg="#6F8A96"
    )

    subtitle.pack(
        anchor="w",
        padx=45
    )
 