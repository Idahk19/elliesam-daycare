import tkinter as tk
from datetime import date

from database import children_collection
from database import staff_collection
from database import attendance_collection
from database import activities_collection

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
        cursor="hand2",
        command=lambda: admin_dashboard(
            window,
            user,
            login_screen
        )
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
        command=lambda: children(
            main_area,
            window
        )
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
        command=lambda: staff(
            main_area,
            window
        )
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
        command=lambda: admin_attendance(
            main_area,
            window
        )
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
        command=lambda: admin_activities(
            main_area,
            window
        )
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
        pady=(40, 5)
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

    today = date.today().strftime("%Y-%m-%d")

    children_count = children_collection.count_documents({})

    staff_count = staff_collection.count_documents({})

    present_count = attendance_collection.count_documents({
        "date": today,
        "attendance": "Present"
    })

    absent_count = attendance_collection.count_documents({
        "date": today,
        "attendance": "Absent"
    })

    total_paid = 0

    records = attendance_collection.find({
        "date": today
    })

    for record in records:
        total_paid += record.get(
            "amount_paid",
            0
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

    # CHILDREN CARD

    children_card = tk.Frame(
        cards_frame,
        bg="#EAF7FC",
        width=220,
        height=120
    )

    children_card.grid(
        row=0,
        column=0,
        padx=8,
        pady=8
    )

    children_card.grid_propagate(False)

    tk.Label(
        children_card,
        text="CHILDREN REGISTERED",
        font=("Arial", 10, "bold"),
        bg="#EAF7FC",
        fg="#6F8A96"
    ).pack(
        anchor="w",
        padx=20,
        pady=(18, 5)
    )

    tk.Label(
        children_card,
        text=str(children_count),
        font=("Arial", 28, "bold"),
        bg="#EAF7FC",
        fg="#315A72"
    ).pack(
        anchor="w",
        padx=20
    )

    # STAFF CARD

    staff_card = tk.Frame(
        cards_frame,
        bg="#EAF7FC",
        width=220,
        height=120
    )

    staff_card.grid(
        row=0,
        column=1,
        padx=8,
        pady=8
    )

    staff_card.grid_propagate(False)

    tk.Label(
        staff_card,
        text="STAFF REGISTERED",
        font=("Arial", 10, "bold"),
        bg="#EAF7FC",
        fg="#6F8A96"
    ).pack(
        anchor="w",
        padx=20,
        pady=(18, 5)
    )

    tk.Label(
        staff_card,
        text=str(staff_count),
        font=("Arial", 28, "bold"),
        bg="#EAF7FC",
        fg="#315A72"
    ).pack(
        anchor="w",
        padx=20
    )

    # PRESENT TODAY CARD

    attendance_card = tk.Frame(
        cards_frame,
        bg="#EAF7FC",
        width=220,
        height=120
    )

    attendance_card.grid(
        row=0,
        column=2,
        padx=8,
        pady=8
    )

    attendance_card.grid_propagate(False)

    tk.Label(
        attendance_card,
        text="PRESENT TODAY",
        font=("Arial", 10, "bold"),
        bg="#EAF7FC",
        fg="#6F8A96"
    ).pack(
        anchor="w",
        padx=20,
        pady=(18, 5)
    )

    tk.Label(
        attendance_card,
        text=str(present_count),
        font=("Arial", 28, "bold"),
        bg="#EAF7FC",
        fg="#315A72"
    ).pack(
        anchor="w",
        padx=20
    )

    # TODAY'S ATTENDANCE

    todays_attendance = tk.Frame(
        cards_frame,
        bg="#B9E3F5",
        width=340,
        height=170
    )

    todays_attendance.grid(
        row=1,
        column=0,
        columnspan=2,
        padx=8,
        pady=15
    )

    todays_attendance.grid_propagate(False)

    tk.Label(
        todays_attendance,
        text="TODAY'S ATTENDANCE",
        font=("Arial", 11, "bold"),
        bg="#B9E3F5",
        fg="#315A72"
    ).pack(
        anchor="w",
        padx=25,
        pady=(22, 5)
    )

    tk.Label(
        todays_attendance,
        text=f"{present_count} Present  •  {absent_count} Absent",
        font=("Arial", 20, "bold"),
        bg="#B9E3F5",
        fg="#294A5A"
    ).pack(
        anchor="w",
        padx=25,
        pady=5
    )

    tk.Label(
        todays_attendance,
        text=f"Total registered: {children_count} children",
        font=("Arial", 10),
        bg="#B9E3F5",
        fg="#6F8A96"
    ).pack(
        anchor="w",
        padx=25
    )

    # TOTAL PAID TODAY

    todays_payment = tk.Frame(
        cards_frame,
        bg="#B9E3F5",
        width=340,
        height=170
    )

    todays_payment.grid(
        row=1,
        column=2,
        padx=8,
        pady=15
    )

    todays_payment.grid_propagate(False)

    tk.Label(
        todays_payment,
        text="TOTAL PAID TODAY",
        font=("Arial", 11, "bold"),
        bg="#B9E3F5",
        fg="#315A72"
    ).pack(
        anchor="w",
        padx=25,
        pady=(22, 5)
    )

    tk.Label(
        todays_payment,
        text=f"KSh {total_paid:,.0f}",
        font=("Arial", 25, "bold"),
        bg="#B9E3F5",
        fg="#294A5A"
    ).pack(
        anchor="w",
        padx=25,
        pady=5
    )

    tk.Label(
        todays_payment,
        text="Payments received today",
        font=("Arial", 10),
        bg="#B9E3F5",
        fg="#6F8A96"
    ).pack(
        anchor="w",
        padx=25
    )

    cards_frame.grid_columnconfigure(
        0,
        weight=1
    )

    cards_frame.grid_columnconfigure(
        1,
        weight=1
    )

    cards_frame.grid_columnconfigure(
        2,
        weight=1
    )