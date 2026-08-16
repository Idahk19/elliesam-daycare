import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import date

from database import children_collection
from database import activities_collection


def activities(main_area, window):

    for item in main_area.winfo_children():
        item.destroy()

    title = tk.Label(
        main_area,
        text="Activities",
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
        text=f"Record the child's daily activities.   {today}",
        font=("Arial", 11),
        bg="#FFFFFF",
        fg="#6F8A96"
    )

    subtitle.pack(
        anchor="w",
        padx=45,
        pady=(0, 25)
    )

    form = tk.Frame(
        main_area,
        bg="#EAF7FC"
    )

    form.pack(
        fill="x",
        padx=45,
        pady=10
    )

    # Child

    tk.Label(
        form,
        text="Child",
        font=("Arial", 10, "bold"),
        bg="#EAF7FC",
        fg="#294A5A"
    ).grid(
        row=0,
        column=0,
        sticky="w",
        padx=15,
        pady=(15, 5)
    )

    children = list(children_collection.find())

    child_names = []

    for child in children:

        name = (
            f"{child.get('first_name', '')} "
            f"{child.get('last_name', '')}"
        ).strip()

        child_names.append(name)

    child_box = ttk.Combobox(
        form,
        values=child_names,
        state="readonly",
        width=25
    )

    child_box.grid(
        row=1,
        column=0,
        padx=15,
        pady=(0, 15),
        ipady=5
    )

    # Drop off

    tk.Label(
        form,
        text="Drop-off Time",
        font=("Arial", 10, "bold"),
        bg="#EAF7FC",
        fg="#294A5A"
    ).grid(
        row=0,
        column=1,
        sticky="w",
        padx=15,
        pady=(15, 5)
    )

    drop_off = tk.Entry(
        form,
        font=("Arial", 10),
        bg="#FFFFFF",
        relief="flat"
    )

    drop_off.grid(
        row=1,
        column=1,
        padx=15,
        pady=(0, 15),
        ipady=5
    )

    # Pick up

    tk.Label(
        form,
        text="Pick-up Time",
        font=("Arial", 10, "bold"),
        bg="#EAF7FC",
        fg="#294A5A"
    ).grid(
        row=0,
        column=2,
        sticky="w",
        padx=15,
        pady=(15, 5)
    )

    pick_up = tk.Entry(
        form,
        font=("Arial", 10),
        bg="#FFFFFF",
        relief="flat"
    )

    pick_up.grid(
        row=1,
        column=2,
        padx=15,
        pady=(0, 15),
        ipady=5
    )

    # Nap time

    tk.Label(
        form,
        text="Nap Time",
        font=("Arial", 10, "bold"),
        bg="#EAF7FC",
        fg="#294A5A"
    ).grid(
        row=2,
        column=0,
        sticky="w",
        padx=15,
        pady=(5, 5)
    )

    nap_time = tk.Entry(
        form,
        font=("Arial", 10),
        bg="#FFFFFF",
        relief="flat"
    )

    nap_time.grid(
        row=3,
        column=0,
        padx=15,
        pady=(0, 15),
        ipady=5
    )

    # Activities

    tk.Label(
        form,
        text="Activities",
        font=("Arial", 10, "bold"),
        bg="#EAF7FC",
        fg="#294A5A"
    ).grid(
        row=2,
        column=1,
        sticky="w",
        padx=15,
        pady=(5, 5)
    )

    activities_entry = tk.Entry(
        form,
        font=("Arial", 10),
        bg="#FFFFFF",
        relief="flat"
    )

    activities_entry.grid(
        row=3,
        column=1,
        columnspan=2,
        sticky="ew",
        padx=15,
        pady=(0, 15),
        ipady=5
    )

    def save_activity():

        selected_child = child_box.get()

        if not selected_child:
            messagebox.showwarning(
                "Missing Information",
                "Please select a child."
            )
            return

        if not drop_off.get().strip():
            messagebox.showwarning(
                "Missing Information",
                "Please enter the drop-off time."
            )
            return

        if not pick_up.get().strip():
            messagebox.showwarning(
                "Missing Information",
                "Please enter the pick-up time."
            )
            return

        if not nap_time.get().strip():
            messagebox.showwarning(
                "Missing Information",
                "Please enter the nap time."
            )
            return

        if not activities_entry.get().strip():
            messagebox.showwarning(
                "Missing Information",
                "Please enter the activities."
            )
            return

        selected_child_data = None

        for child in children:

            name = (
                f"{child.get('first_name', '')} "
                f"{child.get('last_name', '')}"
            ).strip()

            if name == selected_child:
                selected_child_data = child
                break

        activities_collection.insert_one(
            {
                "child_id": selected_child_data["_id"],
                "child_name": selected_child,
                "date": date.today().strftime("%Y-%m-%d"),
                "drop_off": drop_off.get().strip(),
                "pick_up": pick_up.get().strip(),
                "nap_time": nap_time.get().strip(),
                "activities": activities_entry.get().strip()
            }
        )

        messagebox.showinfo(
            "Success",
            "Activity record saved successfully!"
        )

        activities(
            main_area,
            window
        )

    save_button = tk.Button(
        form,
        text="SAVE ACTIVITY",
        font=("Arial", 10, "bold"),
        bg="#6FB6D6",
        fg="white",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=save_activity
    )

    save_button.grid(
        row=4,
        column=0,
        columnspan=3,
        pady=(5, 15),
        ipadx=20,
        ipady=8
    )

    # Activity history

    history_title = tk.Label(
        main_area,
        text="Daily Activity Records",
        font=("Arial", 18, "bold"),
        bg="#FFFFFF",
        fg="#294A5A"
    )

    history_title.pack(
        anchor="w",
        padx=45,
        pady=(20, 10)
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

    headers = [
        "Date",
        "Child",
        "Drop-off",
        "Pick-up",
        "Nap",
        "Activities"
    ]

    for column, header in enumerate(headers):

        tk.Label(
            history_frame,
            text=header,
            font=("Arial", 10, "bold"),
            bg="#B9E3F5",
            fg="#294A5A",
            padx=10,
            pady=10
        ).grid(
            row=0,
            column=column,
            sticky="ew"
        )

    records = activities_collection.find().sort(
        "date",
        -1
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
                padx=10,
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
    history_frame.grid_columnconfigure(5, weight=3)