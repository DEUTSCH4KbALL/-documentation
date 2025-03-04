import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import shutil

suspicious_strings = ["malware", "virus", "trojan", "attack"]
quarantine_dir = os.path.join(os.getcwd(), "quarantine")

def scan_file(file_path):
    try:
        with open(file_path, 'r', encoding="utf8", errors='ignore') as file:
            content = file.read()
            for string in suspicious_strings:
                if string in content:
                    quarantine_file(file_path)
                    return f"Warning: Suspicious string '{string}' found and file quarantined: {file_path}"
    except Exception as e:
        return f"Error scanning {file_path}: {e}"
    return None

def quarantine_file(file_path):
    if not os.path.exists(quarantine_dir):
        os.makedirs(quarantine_dir)
    try:
        shutil.move(file_path, quarantine_dir)
    except Exception as e:
        return f"Error quarantining file {file_path}: {e}"
    return None

def scan_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            result = scan_file(file_path)
            if result:
                results.append(result)
    return results

def start_scan():
    directory = filedialog.askdirectory()
    if directory:
        results = scan_directory(directory)
        result_text.delete(1.0, tk.END)
        if results:
            for result in results:
                result_text.insert(tk.END, result + "\n")
        else:
            result_text.insert(tk.END, "No suspicious strings found.")
        messagebox.showinfo("Scan Completed", "The directory scan is completed.")
        status_bar.config(text="Сканирование завершено")

def show_about():
    messagebox.showinfo("About", "Antivirus Scanner\nVersion 1.0\nCreated by Marty with a little help from AI.")

def update_status(status):
    status_bar.config(text=status)

def schedule_scan():
    # Здесь можно добавить функциональность планирования сканирования
    messagebox.showinfo("Schedule Scan", "Функция планирования сканирования пока недоступна.")

def quarantine_files():
    quarantine_files_list = os.listdir(quarantine_dir) if os.path.exists(quarantine_dir) else []
    if quarantine_files_list:
        messagebox.showinfo("Quarantine", f"Quarantined files:\n{', '.join(quarantine_files_list)}")
    else:
        messagebox.showinfo("Quarantine", "No files in quarantine.")

def update_definitions():
    # Здесь можно добавить функциональность обновления антивирусных баз данных
    messagebox.showinfo("Update", "Антивирусные базы данных обновлены.")

def user_guide():
    guide_text = (
        "### Руководство Пользователя Антивирусного Сканера\n\n"
        "#### Введение\n"
        "Добро пожаловать в Антивирусный Сканер! Это руководство поможет вам использовать программу для сканирования и защиты ваших файлов от потенциальных угроз.\n\n"
        "#### Установка и Запуск\n"
        "1. **Скачайте программу** и сохраните её на вашем компьютере.\n"
        "2. **Запустите программу** двойным щелчком по файлу. Откроется главное окно Антивирусного Сканера.\n\n"
        "#### Основные Компоненты\n"
        "- **Меню 'Файл'**:\n"
        "  - **Сканировать директорию**: Запуск сканирования выбранной директории.\n"
        "  - **Выход**: Закрыть программу.\n\n"
        "- **Меню 'Справка'**:\n"
        "  - **О программе**: Информация о программе.\n"
        "  - **Руководство пользователя**: Открытие данного руководства.\n"
        "  - **Документация**: Ссылка на подробную документацию.\n"
        "  - **Поддержка**: Контактная информация службы поддержки.\n\n"
        "- **Боковая Панель**:\n"
        "  - **Сканировать директорию**: Запуск сканирования выбранной директории.\n"
        "  - **Планировать сканирование**: Функция планирования сканирования (пока недоступна).\n"
        "  - **Карантин**: Функция карантина файлов.\n"
        "  - **Обновить базы данных**: Функция обновления антивирусной базы данных.\n\n"
        "- **Основное Окно**:\n"
        "  - **Текстовое поле для результатов**: Отображение результатов сканирования.\n"
        "  - **Статусная строка**: Отображение текущего состояния программы.\n\n"
        "#### Использование\n"
        "1. **Сканирование директории**:\n"
        "   - Нажмите кнопку 'Сканировать директорию' на боковой панели или выберите эту опцию в меню 'Файл'.\n"
        "   - Выберите директорию, которую хотите сканировать.\n"
        "   - Дождитесь завершения сканирования. Результаты будут отображены в текстовом поле.\n\n"
        "2. **Планирование сканирования**:\n"
        "   - Нажмите кнопку 'Планировать сканирование' на боковой панели.\n"
        "   - Эта функция пока недоступна и будет реализована в будущем.\n\n"
        "3. **Карантин**:\n"
        "   - Нажмите кнопку 'Карантин' на боковой панели, чтобы увидеть список файлов в карантине.\n\n"
        "4. **Обновление базы данных**:\n"
        "   - Нажмите кнопку 'Обновить базы данных' на боковой панели для обновления антивирусной базы данных.\n\n"
        "#### Поддержка\n"
        "Если у вас возникли вопросы или проблемы, свяжитесь с нашей службой поддержки:\n"
        "- **Email**: denispahomov01@gmail.com\n"
        "- **Телефон**: +(380)-996-830-840\n\n"
        "Мы надеемся, что наш Антивирусный Сканер поможет вам защитить ваши файлы и данные. Спасибо за использование нашей программы!"
    )
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, guide_text)

def documentation():
    messagebox.showinfo("Documentation", "Ссылка на документацию:\nhttps://deutsch4kball.github.io//documentation/")

def support():
    messagebox.showinfo("Support", "Служба поддержки:\nEmail: denispahomov01@gmail.com\nТелефон: +(380)-996-830-840)")

# Создаем основное окно
root = tk.Tk()
root.title("Антивирусный сканер")
root.geometry("1000x600")  # Увеличим ширину окна
root.configure(bg="#2e8b57")

# Создаем боковую панель
side_panel = tk.Frame(root, bg="#2e8b57")
side_panel.pack(side=tk.LEFT, fill=tk.Y)

# Добавляем кнопки на боковую панель
scan_button = tk.Button(side_panel, text="Сканировать директорию", command=start_scan, bg="#006400", fg="white")
scan_button.pack(pady=10, padx=10)

schedule_button = tk.Button(side_panel, text="Планировать сканирование", command=schedule_scan, bg="#006400", fg="white")
schedule_button.pack(pady=10, padx=10)

quarantine_button = tk.Button(side_panel, text="Карантин", command=quarantine_files, bg="#006400", fg="white")
quarantine_button.pack(pady=10, padx=10)

update_button = tk.Button(side_panel, text="Обновить базы данных", command=update_definitions, bg="#006400", fg="white")
update_button.pack(pady=10, padx=10)

# Добавляем меню
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Меню "Файл"
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Сканировать директорию", command=start_scan)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)

# Меню "Справка"
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Справка", menu=help_menu)
help_menu.add_command(label="О программе", command=show_about)
help_menu.add_command(label="Руководство пользователя", command=user_guide)
help_menu.add_command(label="Документация", command=documentation)
help_menu.add_command(label="Поддержка", command=support)

# Добавляем текстовое поле для вывода результатов
result_text = tk.Text(root, wrap=tk.WORD, height=20, width=80, bg="#f0fff0", fg="#2e8b57")
result_text.pack(pady=10, padx=10)

# Добавляем статусную строку
status_bar = tk.Label(root, text="Готов к сканированию", bd=1, relief=tk.SUNKEN, anchor=tk.W, bg="#2e8b57", fg="white")
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Запускаем главное окно
root.mainloop()