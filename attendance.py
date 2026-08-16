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
        text="Attendance & Payments",
        font=("Arial", 24, "bold"),
        bg="#FFFFFF",
        fg="#294A5A"
    )
    title.pack(anchor="w", padx=45, pady=(40, 5))

    today = date.today().strftime("%d/%m/%Y")

    subtitle = tk.Label(
        main_area,
        text=f"Record today's attendance and payments.   {today}",
        font=("Arial", 11),
        bg="#FFFFFF",
        fg="#6F8A96"
    )
    subtitle.pack(anchor="w", padx=45, pady=(0, 25))

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
        "Expected Fee",
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

    children = list(children_collection.find())

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

        expected_fee = tk.Entry(
            attendance_frame,
            font=("Arial", 10),
            bg="#EAF7FC",
            fg="#294A5A",
            relief="flat",
            bd=0
        )

        expected_fee.insert(0, "500")

        expected_fee.grid(
            row=row,
            column=2,
            padx=10,
            pady=8,
            ipady=5
        )

        amount_paid = tk.Entry(
            attendance_frame,
            font=("Arial", 10),
            bg="#EAF7FC",
            fg="#294A5A",
            relief="flat",
            bd=0
        )

        amount_paid.insert(0, "0")

        amount_paid.grid(
            row=row,
            column=3,
            padx=10,
            pady=8,
            ipady=5
        )

        attendance_data.append({
            "child": child,
            "status": attendance_status,
            "expected_fee": expected_fee,
            "amount_paid": amount_paid
        })

    attendance_frame.grid_columnconfigure(0, weight=2)
    attendance_frame.grid_columnconfigure(1, weight=1)
    attendance_frame.grid_columnconfigure(2, weight=1)
    attendance_frame.grid_columnconfigure(3, weight=1)

    def save_attendance():

        today_date = date.today().strftime("%Y-%m-%d")

        for item in attendance_data:

            child = item["child"]

            status = item["status"].get()

            expected_fee = item["expected_fee"].get().strip()
            amount_paid = item["amount_paid"].get().strip()

            if not expected_fee:
                expected_fee = "0"

            if not amount_paid:
                amount_paid = "0"

            try:
                expected_fee = float(expected_fee)
                amount_paid = float(amount_paid)

                if expected_fee < 0 or amount_paid < 0:
                    messagebox.showwarning(
                        "Invalid Amount",
                        "Amounts cannot be negative."
                    )
                    return

            except ValueError:

                messagebox.showwarning(
                    "Invalid Amount",
                    "Please enter valid amounts."
                )
                return

            child_name = (
                f"{child.get('first_name', '')} "
                f"{child.get('last_name', '')}"
            ).strip()

            existing_record = attendance_collection.find_one({
                "child_id": child["_id"],
                "date": today_date
            })

            if existing_record:

                attendance_collection.update_one(
                    {
                        "_id": existing_record["_id"]
                    },
                    {
                        "$set": {
                            "attendance": status,
                            "expected_fee": expected_fee,
                            "amount_paid": amount_paid
                        }
                    }
                )

            else:

                attendance_collection.insert_one({
                    "child_id": child["_id"],
                    "child_name": child_name,
                    "date": today_date,
                    "attendance": status,
                    "expected_fee": expected_fee,
                    "amount_paid": amount_paid
                })

        messagebox.showinfo(
            "Success",
            "Attendance and payment information saved successfully!"
        )

        attendance(main_area, window)

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

    history_container = tk.Frame(
        main_area,
        bg="#FFFFFF"
    )

    history_container.pack(
        fill="both",
        expand=True,
        padx=45,
        pady=(0, 20)
    )

    canvas = tk.Canvas(
        history_container,
        bg="#FFFFFF",
        highlightthickness=0
    )

    scrollbar = tk.Scrollbar(
        history_container,
        orient="vertical",
        command=canvas.yview
    )

    history_frame = tk.Frame(
        canvas,
        bg="#FFFFFF"
    )

    history_frame.bind(
        "<Configure>",
        lambda event: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window(
        (0, 0),
        window=history_frame,
        anchor="nw"
    )

    canvas.configure(
        yscrollcommand=scrollbar.set
    )

    canvas.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    history_headers = [
        "Date",
        "Child",
        "Attendance",
        "Expected Fee",
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

    records = attendance_collection.find().sort(
        "date",
        -1
    )

    for row, record in enumerate(records, start=1):

        values = [
            record.get("date", ""),
            record.get("child_name", ""),
            record.get("attendance", ""),
            f"KSh {record.get('expected_fee', 0)}",
            f"KSh {record.get('amount_paid', 0)}"
        ]

        for column, value in enumerate(values):

            tk.Label(
                history_frame,
                text=value,
                font=("Arial", 9),
                bg="#EAF7FC",
                fg="#294A5A",
                padx=15,
                pady=8,
                anchor="w"
            ).grid(
                row=row,
                column=column,
                sticky="ew"
            )

    history_frame.grid_columnconfigure(0, weight=1)
    history_frame.grid_columnconfigure(1, weight=2)
    history_frame.grid_columnconfigure(2, weight=1)
    history_frame.grid_columnconfigure(3, weight=1)
    history_frame.grid_columnconfigure(4, weight=1)