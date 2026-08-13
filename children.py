import tkinter as tk
from tkinter import ttk


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

    save_button = tk.Button(
        form,
        text="SAVE CHILD",
        bg="#6FB6D6",
        fg="white",
        relief="flat",
        bd=0,
        cursor="hand2"
    )
    save_button.grid(
        row=8,
        column=0,
        columnspan=2,
        sticky="ew",
        pady=20,
        ipady=8
    )