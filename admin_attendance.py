import tkinter as tk
from database import attendance_collection
from tkinter import messagebox


def admin_attendance(main_area, window):

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

    subtitle = tk.Label(
        main_area,
        text="View children's attendance and payment records.",
        font=("Arial", 11),
        bg="#FFFFFF",
        fg="#6F8A96"
    )
    subtitle.pack(anchor="w", padx=45, pady=(0, 25))

    history_frame = tk.Frame(main_area, bg="#FFFFFF")
    history_frame.pack(fill="both", expand=True, padx=45)

    headers = [
        "Date",
        "Child",
        "Attendance",
        "Expected Fee",
        "Amount Paid",
        "Arrears",
        "Actions"
    ]

    for column, header in enumerate(headers):

        tk.Label(
            history_frame,
            text=header,
            font=("Arial", 10, "bold"),
            bg="#B9E3F5",
            fg="#294A5A",
            padx=15,
            pady=10
        ).grid(row=0, column=column, sticky="ew")

    records = list(
        attendance_collection.find().sort("date", -1)
    )

    def delete_record(record):

        answer = messagebox.askyesno(
            "Delete Record",
            "Are you sure you want to delete this record?"
        )

        if answer:

            attendance_collection.delete_one({
                "_id": record["_id"]
            })

            messagebox.showinfo(
                "Deleted",
                "Attendance record deleted successfully."
            )

            admin_attendance(main_area, window)

    def edit_record(record):

        edit_window = tk.Toplevel(window)
        edit_window.title("Edit Attendance")
        edit_window.geometry("400x350")
        edit_window.configure(bg="#FFFFFF")

        tk.Label(
            edit_window,
            text="Edit Attendance",
            font=("Arial", 20, "bold"),
            bg="#FFFFFF",
            fg="#294A5A"
        ).pack(pady=20)

        tk.Label(
            edit_window,
            text=f"Child: {record.get('child_name', '')}",
            bg="#FFFFFF",
            fg="#294A5A"
        ).pack(pady=5)

        tk.Label(
            edit_window,
            text="Attendance",
            bg="#FFFFFF",
            fg="#294A5A"
        ).pack()

        attendance_box = tk.Entry(
            edit_window,
            bg="#EAF7FC",
            relief="flat"
        )
        attendance_box.insert(
            0,
            record.get("attendance", "")
        )
        attendance_box.pack(
            pady=5,
            ipady=5
        )

        tk.Label(
            edit_window,
            text="Expected Fee",
            bg="#FFFFFF",
            fg="#294A5A"
        ).pack()

        expected_entry = tk.Entry(
            edit_window,
            bg="#EAF7FC",
            relief="flat"
        )
        expected_entry.insert(
            0,
            record.get("expected_fee", 0)
        )
        expected_entry.pack(
            pady=5,
            ipady=5
        )

        tk.Label(
            edit_window,
            text="Amount Paid",
            bg="#FFFFFF",
            fg="#294A5A"
        ).pack()

        paid_entry = tk.Entry(
            edit_window,
            bg="#EAF7FC",
            relief="flat"
        )
        paid_entry.insert(
            0,
            record.get("amount_paid", 0)
        )
        paid_entry.pack(
            pady=5,
            ipady=5
        )

        def save_edit():

            try:
                expected_fee = float(
                    expected_entry.get()
                )

                amount_paid = float(
                    paid_entry.get()
                )

            except ValueError:

                messagebox.showwarning(
                    "Invalid Amount",
                    "Please enter valid amounts."
                )

                return

            attendance_collection.update_one(
                {"_id": record["_id"]},
                {
                    "$set": {
                        "attendance": attendance_box.get(),
                        "expected_fee": expected_fee,
                        "amount_paid": amount_paid
                    }
                }
            )

            messagebox.showinfo(
                "Updated",
                "Attendance record updated successfully."
            )

            edit_window.destroy()

            admin_attendance(
                main_area,
                window
            )

        tk.Button(
            edit_window,
            text="SAVE CHANGES",
            font=("Arial", 10, "bold"),
            bg="#6FB6D6",
            fg="white",
            relief="flat",
            bd=0,
            command=save_edit
        ).pack(
            pady=20,
            ipadx=20,
            ipady=8
        )

    for row, record in enumerate(records, start=1):

        expected_fee = record.get("expected_fee", 0)
        amount_paid = record.get("amount_paid", 0)
        arrears = expected_fee - amount_paid

        values = [
            record.get("date", ""),
            record.get("child_name", ""),
            record.get("attendance", ""),
            f"KSh {expected_fee}",
            f"KSh {amount_paid}",
            f"KSh {arrears}"
        ]

        for column, value in enumerate(values):

            tk.Label(
                history_frame,
                text=value,
                font=("Arial", 9),
                bg="#EAF7FC",
                fg="#294A5A",
                padx=15,
                pady=8
            ).grid(
                row=row,
                column=column,
                sticky="ew"
            )

        actions = tk.Frame(
            history_frame,
            bg="#EAF7FC"
        )

        actions.grid(
            row=row,
            column=6,
            padx=5,
            pady=5
        )

        tk.Button(
            actions,
            text="Edit",
            bg="#6FB6D6",
            fg="white",
            relief="flat",
            bd=0,
            command=lambda r=record: edit_record(r)
        ).pack(
            side="left",
            padx=3
        )

        tk.Button(
            actions,
            text="Delete",
            bg="#E57373",
            fg="white",
            relief="flat",
            bd=0,
            command=lambda r=record: delete_record(r)
        ).pack(
            side="left",
            padx=3
        )

    history_frame.grid_columnconfigure(0, weight=1)
    history_frame.grid_columnconfigure(1, weight=2)
    history_frame.grid_columnconfigure(2, weight=1)
    history_frame.grid_columnconfigure(3, weight=1)
    history_frame.grid_columnconfigure(4, weight=1)
    history_frame.grid_columnconfigure(5, weight=1)
    history_frame.grid_columnconfigure(6, weight=2)