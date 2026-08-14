import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database import staff_collection


def staff(main_area, window):

    for item in main_area.winfo_children():
        item.destroy()

    title = tk.Label(
        main_area,
        text="Staff",
        font=("Arial", 24, "bold"),
        bg="#FFFFFF",
        fg="#294A5A"
    )

    title.pack(
        anchor="w",
        padx=45,
        pady=(40, 5)
    )

    subtitle = tk.Label(
        main_area,
        text="Manage all staff registered at Ellisam Daycare.",
        font=("Arial", 11),
        bg="#FFFFFF",
        fg="#6F8A96"
    )

    subtitle.pack(
        anchor="w",
        padx=45,
        pady=(0, 25)
    )

    actions_frame = tk.Frame(
        main_area,
        bg="#FFFFFF"
    )

    actions_frame.pack(
        fill="x",
        padx=45,
        pady=(10, 20)
    )

    search_entry = tk.Entry(
        actions_frame,
        font=("Arial", 11),
        bg="#EAF7FC",
        fg="#294A5A",
        relief="flat",
        bd=0
    )

    search_entry.pack(
        side="left",
        fill="x",
        expand=True,
        ipady=10
    )

    add_staff_button = tk.Button(
        actions_frame,
        text="Add Staff",
        font=("Arial", 11, "bold"),
        bg="#6FB6D6",
        fg="#FFFFFF",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=lambda: add_staff(window, main_area)
    )

    add_staff_button.pack(
        side="right",
        padx=(15, 0),
        ipady=8,
        ipadx=15
    )

    staff_frame = tk.Frame(
        main_area,
        bg="#FFFFFF"
    )

    staff_frame.pack(
        fill="both",
        expand=True,
        padx=45,
        pady=20
    )

    display_staff(
        staff_frame,
        main_area,
        window
    )


def display_staff(staff_frame, main_area, window):
    for item in staff_frame.winfo_children():
        item.destroy()

    headers = ["Name", "Gender", "Phone", "Actions"]

    for column, header in enumerate(headers):
        tk.Label(
            staff_frame,
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

    for row, person in enumerate(staff_collection.find(), start=1):

        first_name = person.get("first_name", "")
        last_name = person.get("last_name", "")
        gender = person.get("gender", "")
        phone = person.get("phone", "")

        name = f"{first_name} {last_name}".strip()

        if not name:
            name = "Unknown Staff"

        tk.Label(
            staff_frame,
            text=name,
            font=("Arial", 10),
            bg="#EAF7FC",
            fg="#294A5A",
            padx=20,
            pady=12,
            anchor="w"
        ).grid(
            row=row,
            column=0,
            sticky="ew"
        )

        tk.Label(
            staff_frame,
            text=gender,
            font=("Arial", 10),
            bg="#EAF7FC",
            fg="#294A5A",
            padx=20,
            pady=12
        ).grid(
            row=row,
            column=1,
            sticky="ew"
        )

        tk.Label(
            staff_frame,
            text=phone,
            font=("Arial", 10),
            bg="#EAF7FC",
            fg="#294A5A",
            padx=20,
            pady=12
        ).grid(
            row=row,
            column=2,
            sticky="ew"
        )

        actions = tk.Frame(
            staff_frame,
            bg="#EAF7FC"
        )

        actions.grid(
            row=row,
            column=3
        )

        edit_button = tk.Button(
            actions,
            text="Edit",
            bg="#6FB6D6",
            fg="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=lambda person=person:
                edit_staff(person, window, main_area)
        )

        edit_button.pack(
            side="left",
            padx=5,
            pady=8
        )

        delete_button = tk.Button(
            actions,
            text="Delete",
            bg="#E57373",
            fg="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=lambda person=person:
                delete_staff(person, main_area, window)
        )

        delete_button.pack(
            side="left",
            padx=5,
            pady=8
        )

    staff_frame.grid_columnconfigure(0, weight=2)
    staff_frame.grid_columnconfigure(1, weight=1)
    staff_frame.grid_columnconfigure(2, weight=2)
    staff_frame.grid_columnconfigure(3, weight=2)
    
def add_staff(window, main_area):

    add_window = tk.Toplevel(window)

    add_window.title("Add Staff")
    add_window.geometry("500x400")
    add_window.configure(bg="#FFFFFF")
    add_window.resizable(False, False)

    title = tk.Label(
        add_window,
        text="Add New Staff",
        font=("Arial", 22, "bold"),
        bg="#FFFFFF",
        fg="#294A5A"
    )

    title.pack(
        pady=(25, 20)
    )

    form = tk.Frame(
        add_window,
        bg="#FFFFFF"
    )

    form.pack(
        padx=40,
        fill="x"
    )

    tk.Label(
        form,
        text="First Name",
        bg="#FFFFFF",
        fg="#294A5A"
    ).grid(
        row=0,
        column=0,
        sticky="w",
        pady=5
    )

    first_name = tk.Entry(form)

    first_name.grid(
        row=1,
        column=0,
        padx=(0, 10),
        pady=(0, 15),
        ipady=5
    )

    tk.Label(
        form,
        text="Last Name",
        bg="#FFFFFF",
        fg="#294A5A"
    ).grid(
        row=0,
        column=1,
        sticky="w",
        pady=5
    )

    last_name = tk.Entry(form)

    last_name.grid(
        row=1,
        column=1,
        pady=(0, 15),
        ipady=5
    )

    tk.Label(
        form,
        text="Phone Number",
        bg="#FFFFFF",
        fg="#294A5A"
    ).grid(
        row=2,
        column=0,
        sticky="w",
        pady=5
    )

    phone = tk.Entry(form)

    phone.grid(
        row=3,
        column=0,
        padx=(0, 10),
        pady=(0, 15),
        ipady=5
    )

    tk.Label(
        form,
        text="Gender",
        bg="#FFFFFF",
        fg="#294A5A"
    ).grid(
        row=2,
        column=1,
        sticky="w",
        pady=5
    )

    gender = ttk.Combobox(
        form,
        values=["Male", "Female"],
        state="readonly"
    )

    gender.grid(
        row=3,
        column=1,
        pady=(0, 15),
        ipady=3
    )

    def save_staff():

        first = first_name.get()
        last = last_name.get()
        staff_gender = gender.get()
        staff_phone = phone.get()

        if not first or not last or not staff_gender or not staff_phone:

            messagebox.showwarning(
                "Missing Information",
                "Please fill in all fields."
            )

            return

        staff_data = {
            "first_name": first,
            "last_name": last,
            "gender": staff_gender,
            "phone": staff_phone
        }

        staff_collection.insert_one(
            staff_data
        )

        messagebox.showinfo(
            "Success",
            "Staff added successfully!"
        )

        add_window.destroy()

        staff(
            main_area,
            window
        )

    save_button = tk.Button(
        form,
        text="SAVE STAFF",
        bg="#6FB6D6",
        fg="white",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=save_staff
    )

    save_button.grid(
        row=4,
        column=0,
        columnspan=2,
        sticky="ew",
        pady=20,
        ipady=8
    )


def edit_staff(person, window, main_area):

    edit_window = tk.Toplevel(window)

    edit_window.title("Edit Staff")
    edit_window.geometry("500x400")
    edit_window.configure(bg="#FFFFFF")
    edit_window.resizable(False, False)

    title = tk.Label(
        edit_window,
        text="Edit Staff",
        font=("Arial", 22, "bold"),
        bg="#FFFFFF",
        fg="#294A5A"
    )

    title.pack(
        pady=(25, 20)
    )

    form = tk.Frame(
        edit_window,
        bg="#FFFFFF"
    )

    form.pack(
        padx=40,
        fill="x"
    )

    tk.Label(
        form,
        text="First Name",
        bg="#FFFFFF",
        fg="#294A5A"
    ).grid(
        row=0,
        column=0,
        sticky="w",
        pady=5
    )

    first_name = tk.Entry(form)

    first_name.insert(
        0,
        person["first_name"]
    )

    first_name.grid(
        row=1,
        column=0,
        padx=(0, 10),
        pady=(0, 15),
        ipady=5
    )

    tk.Label(
        form,
        text="Last Name",
        bg="#FFFFFF",
        fg="#294A5A"
    ).grid(
        row=0,
        column=1,
        sticky="w",
        pady=5
    )

    last_name = tk.Entry(form)

    last_name.insert(
        0,
        person["last_name"]
    )

    last_name.grid(
        row=1,
        column=1,
        pady=(0, 15),
        ipady=5
    )

    tk.Label(
        form,
        text="Phone Number",
        bg="#FFFFFF",
        fg="#294A5A"
    ).grid(
        row=2,
        column=0,
        sticky="w",
        pady=5
    )

    phone = tk.Entry(form)

    phone.insert(
        0,
        person["phone"]
    )

    phone.grid(
        row=3,
        column=0,
        padx=(0, 10),
        pady=(0, 15),
        ipady=5
    )

    tk.Label(
        form,
        text="Gender",
        bg="#FFFFFF",
        fg="#294A5A"
    ).grid(
        row=2,
        column=1,
        sticky="w",
        pady=5
    )

    gender = ttk.Combobox(
        form,
        values=["Male", "Female"],
        state="readonly"
    )

    gender.set(
        person["gender"]
    )

    gender.grid(
        row=3,
        column=1,
        pady=(0, 15),
        ipady=3
    )

    def update_staff():

        if not first_name.get() or not last_name.get():
            messagebox.showwarning(
                "Missing Information",
                "Please fill in all fields."
            )
            return

        staff_collection.update_one(
            {"_id": person["_id"]},
            {
                "$set": {
                    "first_name": first_name.get(),
                    "last_name": last_name.get(),
                    "gender": gender.get(),
                    "phone": phone.get()
                }
            }
        )

        messagebox.showinfo(
            "Success",
            "Staff updated successfully!"
        )

        edit_window.destroy()

        staff(
            main_area,
            window
        )

    update_button = tk.Button(
        form,
        text="UPDATE STAFF",
        bg="#6FB6D6",
        fg="white",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=update_staff
    )

    update_button.grid(
        row=4,
        column=0,
        columnspan=2,
        sticky="ew",
        pady=20,
        ipady=8
    )


def delete_staff(person, main_area, window):

    confirm = messagebox.askyesno(
        "Delete Staff",
        f"Are you sure you want to delete "
        f"{person['first_name']} {person['last_name']}?"
    )

    if confirm:

        staff_collection.delete_one(
            {"_id": person["_id"]}
        )

        messagebox.showinfo(
            "Success",
            "Staff deleted successfully!"
        )

        staff(
            main_area,
            window
        )