import tkinter as tk
from children import children
from staff import staff
from admin_attendance import admin_attendance
from admin_activities import admin_activities

def admin_dashboard(window, user, login_screen):

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

    main_area = tk.Frame(
        window,
        bg="#FFFFFF"
    )

    main_area.pack(
        side="right",
        fill="both",
        expand=True
    )

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
    cursor="hand2",
    command=lambda: children(main_area, window)
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
        cursor="hand2",
        command=lambda: staff(main_area, window)
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
        cursor="hand2",
        command=lambda: admin_attendance(main_area, window)
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
        cursor="hand2",
        command=lambda: admin_activities(main_area, window)
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
        cursor="hand2",
        command=login_screen
    )

    logout_button.pack(
        side="bottom",
        fill="x",
        padx=15,
        pady=25
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
    cards_frame = tk.Frame(
        main_area,
        bg="#FFFFFF"
    )

    cards_frame.pack(
       fill="x",
       padx=45,
       pady=30
    )

    children_card = tk.Frame(
       cards_frame,
       bg="#B9E3F5",
       width=240,
       height=120
    )

    children_card.grid(
       row=0,
       column=0,
       padx=10,
       pady=10
    )

    children_card.grid_propagate(False)

    staff_card = tk.Frame(
       cards_frame,
       bg="#B9E3F5",
       width=240,
       height=120
    )

    staff_card.grid(
       row=0,
       column=1,
       padx=10,
       pady=10
    )

    staff_card.grid_propagate(False)


    todays_attendance = tk.Frame(
       cards_frame,
       bg="#B9E3F5",
       width=240,
       height=120
    )

    todays_attendance.grid(
       row=0,
       column=2,
       padx=10,
       pady=10
    )

    todays_attendance.grid_propagate(False)


    todays_activity = tk.Frame(
      cards_frame,
      bg="#B9E3F5",
      width=370,
      height=180
    )

    todays_activity.grid(
      row=1,
      column=0,
      columnspan=2,
      padx=10,
      pady=10
    )

    todays_activity.grid_propagate(False)


    recent_payment = tk.Frame(
      cards_frame,
      bg="#B9E3F5",
      width=240,
      height=180
    )

    recent_payment.grid(
      row=1,
      column=2,
      padx=10,
      pady=10
    )

    recent_payment.grid_propagate(False)