import tkinter as tk


def children(main_area):

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
        text="Search a child",
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
        cursor="hand2"
    )

    add_child_button.pack(
        side="right",
        padx=(15, 0),
        ipady=8,
        ipadx=15
    )