import tkinter as tk
from tkinter import ttk

def submit_form():
    print("Форма отправлена")

def main():
    root = tk.Tk()
    root.title("HTML5 Parser Prototype")

    # Создаем рамку для ввода данных
    frame = ttk.Frame(root, padding="10")
    frame.pack(fill="both", expand=True)

    # Создаем лейбл для ввода имени
    name_label = ttk.Label(frame, text="Name:")
    name_label.pack(side="left", padx=5, pady=5)

    # Создаем текстовое поле для ввода имени
    name_entry = ttk.Entry(frame, width=30)
    name_entry.pack(side="left", padx=5, pady=5)

    # Создаем кнопку для отправки формы
    submit_button = ttk.Button(frame, text="Submit", command=submit_form)
    submit_button.pack(side="left", padx=5, pady=5)

    # Создаем рамку для вывода результатов
    result_frame = ttk.Frame(root, padding="10")
    result_frame.pack(fill="both", expand=True)

    # Создаем текстовое поле для вывода результатов
    result_text = tk.Text(result_frame, width=80, height=20)
    result_text.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()