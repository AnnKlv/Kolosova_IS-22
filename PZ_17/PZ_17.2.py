#Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №2 - 9.

import tkinter as tk

def inverse_case(s):
    return s.swapcase()

def main():
    root = tk.Tk()
    root.title("Преобразователь обратного регистра")

    label = tk.Label(root, text="Введите строку:")
    label.pack()

    entry = tk.Entry(root, width=50)
    entry.pack()

    def convert():
        string = entry.get()
        result = inverse_case(string)
        result_label.config(text=result)

    button = tk.Button(root, text="Преобразовать", command=convert)
    button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()