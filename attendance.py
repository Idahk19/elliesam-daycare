import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import date

from database import children_collection
from database import attendance_collection


def attendance(main_area, window):

    for item in main_area.winfo_children():
        item.destroy()

    title = tk.Label(
        main_area,
        text="Attendance",
        font=("Arial", 24, "bold"),
        bg="#FFFFFF",
        fg="#294A5A"
    )

    title.pack(
        anchor="w",
        padx=45,
        pady=(40, 5)
    )

    today = date.today().strftime("%d/%m/%Y")

    subtitle = tk.Label(
        main_area,
        text=f"Record today's attendance and payments.   {today}",
        font=("Arial", 11),
        bg="#FFFFFF",
        fg="#6F8A96"
    )

    subtitle.pack(
        anchor="w",
        padx=45,
        pady=(0, 25)
    )

    attendance_frame = tk.Frame(
        main_area,
        bg="#FFFFFF"
    )

    attendance_frame.pack(
        fill="x",
        padx=45
    )

    headers = [
        "Child",
        "Attendance",
        "Amount Paid"
    ]

    for column, header in enumerate(headers):

        tk.Label(
            attendance_frame,
            text=header,
            font=("Arial", 11, "bold"),
            bg="#B9E3F5",
            fg="#294A5A",
            padx=20,
            pady=12
        ).grid(
            row=0,
            column=column,
            sticky="ew"
        )

    attendance_data = []

    children = children_collection.find()

    for row, child in enumerate(children, start=1):

        first_name = child.get("first_name", "")
        last_name = child.get("last_name", "")

        child_name = f"{first_name} {last_name}".strip()

        if not child_name:
            child_name = "Unknown Child"

        tk.Label(
            attendance_frame,
            text=child_name,
            font=("Arial", 10),
            bg="#EAF7FC",
            fg="#294A5A",
            padx=20,
            pady=10,
            anchor="w"
        ).grid(
            row=row,
            column=0,
            sticky="ew"
        )

        attendance_status = ttk.Combobox(
            attendance_frame,
            values=["Present", "Absent"],
            state="readonly",
            width=15
        )

        attendance_status.set("Present")

        attendance_status.grid(
            row=row,
            column=1,
            padx=10,
            pady=8
        )

        amount_entry = tk.Entry(
            attendance_frame,
            font=("Arial", 10),
            bg="#EAF7FC",
            fg="#294A5A",
            relief="flat",
            bd=0
        )

        amount_entry.insert(0, "0")

        amount_entry.grid(
            row=row,
            column=2,
            padx=10,
            pady=8,
            ipady=5
        )

        attendance_data.append(
            {
                "child": child,
                "status": attendance_status,
                "amount": amount_entry
            }
        )

    attendance_frame.grid_columnconfigure(
        0,
        weight=2
    )

    attendance_frame.grid_columnconfigure(
        1,
        weight=1
    )

    attendance_frame.grid_columnconfigure(
        2,
        weight=1
    )

    def save_attendance():

        today_date = date.today().strftime("%Y-%m-%d")

        for item in attendance_data:

            child = item["child"]

            status = item["status"].get()

            amount = item["amount"].get().strip()

            if not amount:
                amount = "0"

            try:
                amount = float(amount)

                if amount < 0:
                    messagebox.showwarning(
                        "Invalid Amount",
                        "Amount paid cannot be negative."
                    )
                    return

            except ValueError:

                messagebox.showwarning(
                    "Invalid Amount",
                    "Please enter a valid amount."
                )

                return

            existing_record = attendance_collection.find_one(
                {
                    "child_id": child["_id"],
                    "date": today_date
                }
            )

            if existing_record:

                attendance_collection.update_one(
                    {
                        "_id": existing_record["_id"]
                    },
                    {
                        "$set": {
                            "attendance": status,
                            "amount_paid": amount
                        }
                    }
                )

            else:

                attendance_collection.insert_one(
                    {
                        "child_id": child["_id"],
                        "child_name": (
                            f"{child.get('first_name', '')} "
                            f"{child.get('last_name', '')}"
                        ).strip(),
                        "date": today_date,
                        "attendance": status,
                        "amount_paid": amount
                    }
                )

        messagebox.showinfo(
            "Success",
            "Attendance saved successfully!"
        )

        attendance(
            main_area,
            window
        )

    save_button = tk.Button(
        main_area,
        text="SAVE ATTENDANCE",
        font=("Arial", 11, "bold"),
        bg="#6FB6D6",
        fg="white",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=save_attendance
    )

    save_button.pack(
        padx=45,
        pady=20,
        ipadx=20,
        ipady=8
    )

    history_title = tk.Label(
        main_area,
        text="Attendance History",
        font=("Arial", 18, "bold"),
        bg="#FFFFFF",
        fg="#294A5A"
    )

    history_title.pack(
        anchor="w",
        padx=45,
        pady=(15, 10)
    )

    history_frame = tk.Frame(
        main_area,
        bg="#FFFFFF"
    )

    history_frame.pack(
        fill="both",
        expand=True,
        padx=45
    )

    history_headers = [
        "Date",
        "Child",
        "Attendance",
        "Amount Paid"
    ]

    for column, header in enumerate(history_headers):

        tk.Label(
            history_frame,
            text=header,
            font=("Arial", 10, "bold"),
            bg="#B9E3F5",
            fg="#294A5A",
            padx=15,
            pady=10
        ).grid(
            row=0,
            column=column,
            sticky="ew"
        )

    for row, record in enumerate(
        attendance_collection.find().sort("date", -1),
        start=1
    ):

        tk.Label(
            history_frame,
            text=record.get("date", ""),
            bg="#EAF7FC",
            fg="#294A5A",
            padx=15,
            pady=8
        ).grid(
            row=row,
            column=0,
            sticky="ew"
        )

        tk.Label(
            history_frame,
            text=record.get("child_name", ""),
            bg="#EAF7FC",
            fg="#294A5A",
            padx=15,
            pady=8
        ).grid(
            row=row,
            column=1,
            sticky="ew"
        )

        tk.Label(
            history_frame,
            text=record.get("attendance", ""),
            bg="#EAF7FC",
            fg="#294A5A",
            padx=15,
            pady=8
        ).grid(
            row=row,
            column=2,
            sticky="ew"
        )

        tk.Label(
            history_frame,
            text=f"KSh {record.get('amount_paid', 0)}",
            bg="#EAF7FC",
            fg="#294A5A",
            padx=15,
            pady=8
        ).grid(
            row=row,
            column=3,
            sticky="ew"
        )

    history_frame.grid_columnconfigure(0, weight=1)
    history_frame.grid_columnconfigure(1, weight=2)
    history_frame.grid_columnconfigure(2, weight=1)
    history_frame.grid_columnconfigure(3, weight=1)