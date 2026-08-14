import tkinter as tk
from tkinter import ttk
from database import children_collection
from tkinter import messagebox


def children(main_area, window):

    for item in main_area.winfo_children():
        item.destroy()

    title = tk.Label(
        main_area,
        text="Children",
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
        text="Manage all children registered at Ellisam Daycare.",
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

    add_child_button = tk.Button(
        actions_frame,
        text="Add Child",
        font=("Arial", 11, "bold"),
        bg="#6FB6D6",
        fg="#FFFFFF",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=lambda: add_child(window)
    )
    add_child_button.pack(
        side="right",
        padx=(15, 0),
        ipady=8,
        ipadx=15
    )
    children_frame = tk.Frame(
            main_area,
            bg="#FFFFFF"
    )
    
    children_frame.pack(
            fill="both",
            expand=True,
            padx=45,
            pady=20
    )
    for child in children_collection.find():

       child_card = tk.Frame(
        children_frame,
        bg="#EAF7FC"
    )

    child_card.pack(
        fill="x",
        pady=8
    )

    name = tk.Label(
        child_card,
        text=f"{child['first_name']} {child['last_name']}",
        font=("Arial", 13, "bold"),
        bg="#EAF7FC",
        fg="#294A5A"
    )

    name.grid(
        row=0,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )

    gender = tk.Label(
        child_card,
        text=f"Gender: {child['gender']}",
        font=("Arial", 10),
        bg="#EAF7FC",
        fg="#6F8A96"
    )

    gender.grid(
        row=1,
        column=0,
        padx=20,
        pady=5,
        sticky="w"
    )

    dob = tk.Label(
        child_card,
        text=f"Date of Birth: {child['date_of_birth']}",
        font=("Arial", 10),
        bg="#EAF7FC",
        fg="#6F8A96"
    )

    dob.grid(
        row=2,
        column=0,
        padx=20,
        pady=5,
        sticky="w"
    )

    parent = tk.Label(
        child_card,
        text=f"Parent / Guardian: {child['parent']}",
        font=("Arial", 10),
        bg="#EAF7FC",
        fg="#6F8A96"
    )

    parent.grid(
        row=0,
        column=1,
        padx=40,
        pady=15,
        sticky="w"
    )

    phone = tk.Label(
        child_card,
        text=f"Phone: {child['phone']}",
        font=("Arial", 10),
        bg="#EAF7FC",
        fg="#6F8A96"
    )

    phone.grid(
        row=1,
        column=1,
        padx=40,
        pady=5,
        sticky="w"
    )

    allergies = tk.Label(
        child_card,
        text=f"Allergies: {child['allergies']}",
        font=("Arial", 10),
        bg="#EAF7FC",
        fg="#6F8A96"
    )

    allergies.grid(
        row=2,
        column=1,
        padx=40,
        pady=5,
        sticky="w"
    )

    medical_notes = tk.Label(
        child_card,
        text=f"Medical Notes: {child['medical_notes']}",
        font=("Arial", 10),
        bg="#EAF7FC",
        fg="#6F8A96"
    )

    medical_notes.grid(
        row=0,
        column=2,
        rowspan=3,
        padx=40,
        pady=15,
        sticky="w"
    )


def add_child(window):

    add_window = tk.Toplevel(window)

    add_window.title("Add Child")
    add_window.geometry("500x600")
    add_window.configure(bg="#FFFFFF")
    add_window.resizable(False, False)

    title = tk.Label(
        add_window,
        text="Add New Child",
        font=("Arial", 22, "bold"),
        bg="#FFFFFF",
        fg="#294A5A"
    )
    title.pack(pady=(25, 20))

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
    ).grid(row=0, column=0, sticky="w", pady=5)

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
    ).grid(row=0, column=1, sticky="w", pady=5)

    last_name = tk.Entry(form)
    last_name.grid(
        row=1,
        column=1,
        pady=(0, 15),
        ipady=5
    )

    tk.Label(
        form,
        text="Date of Birth",
        bg="#FFFFFF",
        fg="#294A5A"
    ).grid(row=2, column=0, sticky="w", pady=5)

    date_of_birth = tk.Entry(form)
    date_of_birth.grid(
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
    ).grid(row=2, column=1, sticky="w", pady=5)

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

    tk.Label(
        form,
        text="Parent / Guardian",
        bg="#FFFFFF",
        fg="#294A5A"
    ).grid(row=4, column=0, sticky="w", pady=5)

    parent = tk.Entry(form)
    parent.grid(
        row=5,
        column=0,
        padx=(0, 10),
        pady=(0, 15),
        ipady=5
    )

    tk.Label(
        form,
        text="Phone Number",
        bg="#FFFFFF",
        fg="#294A5A"
    ).grid(row=4, column=1, sticky="w", pady=5)

    phone = tk.Entry(form)
    phone.grid(
        row=5,
        column=1,
        pady=(0, 15),
        ipady=5
    )

    tk.Label(
        form,
        text="Allergies",
        bg="#FFFFFF",
        fg="#294A5A"
    ).grid(row=6, column=0, sticky="w", pady=5)

    allergies = tk.Entry(form)
    allergies.grid(
        row=7,
        column=0,
        padx=(0, 10),
        pady=(0, 15),
        ipady=5
    )

    tk.Label(
        form,
        text="Medical Notes",
        bg="#FFFFFF",
        fg="#294A5A"
    ).grid(row=6, column=1, sticky="w", pady=5)

    medical_notes = tk.Entry(form)
    medical_notes.grid(
        row=7,
        column=1,
        pady=(0, 15),
        ipady=5
    )
    def save_child():
        first = first_name.get()
        last = last_name.get()
        dob = date_of_birth.get()
        child_gender = gender.get()
        guardian = parent.get()
        child_phone = phone.get()
        child_allergies = allergies.get()
        notes = medical_notes.get()

        child_data = {
        "first_name": first,
        "last_name": last,
        "date_of_birth": dob,
        "gender": child_gender,
        "parent": guardian,
        "phone": child_phone,
        "allergies": child_allergies,
        "medical_notes": notes
    }
        children_collection.insert_one(child_data)

        messagebox.showinfo(
            "Success",
            "Child added successfully!"
        )

        add_window.destroy()

    save_button = tk.Button(
        form,
        text="SAVE CHILD",
        bg="#6FB6D6",
        fg="white",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=save_child
    )
    save_button.grid(
        row=8,
        column=0,
        columnspan=2,
        sticky="ew",
        pady=20,
        ipady=8
    )
