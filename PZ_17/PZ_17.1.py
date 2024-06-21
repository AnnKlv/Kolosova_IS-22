#В соответствии с номером варианта перейти по ссылке на прототип.Реализовать
#его в IDE PyCharm Community с применением пакета tk.Получить
#интерфейс максимально приближенный к оригиналу (см.таблицу 1).

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Zoo Keeper Application Form")

title_label = tk.Label(root, text="Zoo Keeper Application Form", font=("Helvetica", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

desc_label = tk.Label(root, text="Please complete the form. Mandatory fields are marked with a *", font=("Helvetica", 10))
desc_label.grid(row=1, column=0, columnspan=2, pady=5)

contact_frame = tk.LabelFrame(root, text="CONTACT DETAILS", padx=10, pady=10)
contact_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

tk.Label(contact_frame, text="Name*").grid(row=0, column=0, sticky="w")
tk.Entry(contact_frame).grid(row=0, column=1, padx=5, pady=5)

tk.Label(contact_frame, text="Telephone*").grid(row=1, column=0, sticky="w")
tk.Entry(contact_frame).grid(row=1, column=1, padx=5, pady=5)

tk.Label(contact_frame, text="Email*").grid(row=2, column=0, sticky="w")
tk.Entry(contact_frame).grid(row=2, column=1, padx=5, pady=5)

personal_frame = tk.LabelFrame(root, text="PERSONAL INFORMATION", padx=10, pady=10)
personal_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

tk.Label(personal_frame, text="Age*").grid(row=0, column=0, sticky="w")
tk.Entry(personal_frame).grid(row=0, column=1, padx=5, pady=5)

tk.Label(personal_frame, text="Gender").grid(row=1, column=0, sticky="w")
gender_combobox = ttk.Combobox(personal_frame, values=["Female", "Male", "Other"])
gender_combobox.grid(row=1, column=1, padx=5, pady=5)

tk.Label(personal_frame, text="When did you first know you wanted to be a zoo-keeper?").grid(row=2, column=0, sticky="w")
tk.Entry(personal_frame).grid(row=2, column=1, padx=5, pady=5)

animals_frame = tk.LabelFrame(root, text="PICK YOUR FAVORITE ANIMALS", padx=10, pady=10)
animals_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

animals = ["Zebra", "Cat", "Anaconda", "Human", "Elephant", "Wildebeest", "Pigeon", "Crab"]
for idx, animal in enumerate(animals):
    tk.Checkbutton(animals_frame, text=animal).grid(row=idx // 2, column=idx % 2, sticky="w")

submit_button = tk.Button(root, text="Submit Application")
submit_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
