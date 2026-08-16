import tkinter as tk
from tkinter import messagebox
from database import activities_collection


def admin_activities(main_area, window):

    for item in main_area.winfo_children():
        item.destroy()

    title = tk.Label(
        main_area,
        text="Activities",
        font=("Arial", 24, "bold"),
        bg="#FFFFFF",
        fg="#294A5A"
    )
    title.pack(anchor="w", padx=45, pady=(40, 5))

    subtitle = tk.Label(
        main_area,
        text="View children's daily activities and routines.",
        font=("Arial", 11),
        bg="#FFFFFF",
        fg="#6F8A96"
    )
    subtitle.pack(anchor="w", padx=45, pady=(0, 25))

    history_frame = tk.Frame(
        main_area,
        bg="#FFFFFF"
    )
    history_frame.pack(
        fill="both",
        expand=True,
        padx=45
    )

    headers = [
        "Date",
        "Child",
        "Drop-off",
        "Pick-up",
        "Nap Time",
        "Activities",
        "Actions"
    ]

    for column, header in enumerate(headers):

        tk.Label(
            history_frame,
            text=header,
            font=("Arial", 10, "bold"),
            bg="#B9E3F5",
            fg="#294A5A",
            padx=12,
            pady=10
        ).grid(
            row=0,
            column=column,
            sticky="ew"
        )

    records = list(
        activities_collection.find().sort(
            "date",
            -1
        )
    )

    def delete_activity(record):

        answer = messagebox.askyesno(
            "Delete Activity",
            "Are you sure you want to delete this activity record?"
        )

        if answer:

            activities_collection.delete_one({
                "_id": record["_id"]
            })

            messagebox.showinfo(
                "Deleted",
                "Activity record deleted successfully."
            )

            admin_activities(
                main_area,
                window
            )

    def edit_activity(record):

        edit_window = tk.Toplevel(window)

        edit_window.title("Edit Activity")
        edit_window.geometry("400x400")
        edit_window.configure(bg="#FFFFFF")

        tk.Label(
            edit_window,
            text="Edit Activity",
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
            text="Drop-off Time",
            bg="#FFFFFF",
            fg="#294A5A"
        ).pack()

        drop_off = tk.Entry(
            edit_window,
            bg="#EAF7FC",
            relief="flat"
        )
        drop_off.insert(
            0,
            record.get("drop_off", "")
        )
        drop_off.pack(
            pady=5,
            ipady=5
        )

        tk.Label(
            edit_window,
            text="Pick-up Time",
            bg="#FFFFFF",
            fg="#294A5A"
        ).pack()

        pick_up = tk.Entry(
            edit_window,
            bg="#EAF7FC",
            relief="flat"
        )
        pick_up.insert(
            0,
            record.get("pick_up", "")
        )
        pick_up.pack(
            pady=5,
            ipady=5
        )

        tk.Label(
            edit_window,
            text="Nap Time",
            bg="#FFFFFF",
            fg="#294A5A"
        ).pack()

        nap_time = tk.Entry(
            edit_window,
            bg="#EAF7FC",
            relief="flat"
        )
        nap_time.insert(
            0,
            record.get("nap_time", "")
        )
        nap_time.pack(
            pady=5,
            ipady=5
        )

        tk.Label(
            edit_window,
            text="Activities",
            bg="#FFFFFF",
            fg="#294A5A"
        ).pack()

        activities = tk.Entry(
            edit_window,
            bg="#EAF7FC",
            relief="flat"
        )
        activities.insert(
            0,
            record.get("activities", "")
        )
        activities.pack(
            pady=5,
            ipady=5
        )

        def save_edit():

            activities_collection.update_one(
                {"_id": record["_id"]},
                {
                    "$set": {
                        "drop_off": drop_off.get(),
                        "pick_up": pick_up.get(),
                        "nap_time": nap_time.get(),
                        "activities": activities.get()
                    }
                }
            )

            messagebox.showinfo(
                "Updated",
                "Activity record updated successfully."
            )

            edit_window.destroy()

            admin_activities(
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

        values = [
            record.get("date", ""),
            record.get("child_name", ""),
            record.get("drop_off", ""),
            record.get("pick_up", ""),
            record.get("nap_time", ""),
            record.get("activities", "")
        ]

        for column, value in enumerate(values):

            tk.Label(
                history_frame,
                text=value,
                font=("Arial", 9),
                bg="#EAF7FC",
                fg="#294A5A",
                padx=12,
                pady=8,
                anchor="w"
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
            command=lambda r=record: edit_activity(r)
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
            command=lambda r=record: delete_activity(r)
        ).pack(
            side="left",
            padx=3
        )

    history_frame.grid_columnconfigure(0, weight=1)
    history_frame.grid_columnconfigure(1, weight=2)
    history_frame.grid_columnconfigure(2, weight=1)
    history_frame.grid_columnconfigure(3, weight=1)
    history_frame.grid_columnconfigure(4, weight=1)
    history_frame.grid_columnconfigure(5, weight=3)
    history_frame.grid_columnconfigure(6, weight=2)