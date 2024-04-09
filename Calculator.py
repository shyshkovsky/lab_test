import tkinter as tk

def додавання():
    try:
        result = float(entry1.get()) + float(entry2.get())
        label_result.config(text="Результат: " + str(result))
    except ValueError:
        label_result.config(text="Помилка! Введіть числа.")

def віднімання():
    try:
        result = float(entry1.get()) - float(entry2.get())
        label_result.config(text="Результат: " + str(result))
    except ValueError:
        label_result.config(text="Помилка! Введіть числа.")

def множення():
    try:
        result = float(entry1.get()) * float(entry2.get())
        label_result.config(text="Результат: " + str(result))
    except ValueError:
        label_result.config(text="Помилка! Введіть числа.")

def ділення():
    try:
        result = float(entry1.get()) / float(entry2.get())
        label_result.config(text="Результат: " + str(result))
    except ZeroDivisionError:
        label_result.config(text="Помилка! Ділення на нуль.")
    except ValueError:
        label_result.config(text="Помилка! Введіть числа.")

# Створення графічного вікна
root = tk.Tk()
root.title("Калькулятор")

# Створення елементів управління
label1 = tk.Label(root, text="Введіть перше число:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Введіть друге число:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

button_додавання = tk.Button(root, text="+", command=додавання)
button_додавання.pack()

button_віднімання = tk.Button(root, text="-", command=віднімання)
button_віднімання.pack()

button_множення = tk.Button(root, text="*", command=множення)
button_множення.pack()

button_ділення = tk.Button(root, text="/", command=ділення)
button_ділення.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
