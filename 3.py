import customtkinter as ctk
from tkinter import messagebox

# Инициализация customtkinter
ctk.set_appearance_mode("System")  # "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Авторизация")
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="Введите свои учетные данные")
        self.label.pack(pady=20)

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Имя пользователя")
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Пароль", show="*")
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(self, text="Войти", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Пример проверки учетных данных
        if username == "admin" and password == "password":
            messagebox.showinfo("Успех", "Вы успешно вошли в систему!")
            self.open_first_window()
        else:
            messagebox.showerror("Ошибка", "Неверное имя пользователя или пароль.")

    def open_first_window(self):
        FirstWindow(self)

class FirstWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Первое окно")
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="Это первое окно")
        self.label.pack(pady=20)

        self.switch_button = ctk.CTkButton(self, text="Перейти ко второму окну", command=self.open_second_window)
        self.switch_button.pack(pady=10)

        self.second_window = None  # Переменная для хранения ссылки на второе окно

    def open_second_window(self):
        if self.second_window is None or not self.second_window.winfo_exists():
            self.second_window = SecondWindow(self)

class SecondWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Второе окно")
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="Это второе окно")
        self.label.pack(pady=20)

        self.switch_button = ctk.CTkButton(self, text="Вернуться к главному окну", command=self.open_main_window)
        self.switch_button.pack(pady=10)

    def open_main_window(self):
        self.destroy()  # Закрываем текущее окно

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

    def check_login_password(self):
        login = self.login_entry.get()
        password = self.password_entry.get()
        if login and password:
            try:
                conn = self.db.connect()
                cursor = conn.cursor()
                cursor.execute("""SELECT id_user, login, password FROM users WHERE login=? and password=?""",
                               (login, password))
                admin = cursor.fetchone()
                conn.close()
                if admin:
                    self.current_admin_uid = admin[0]
                    showinfo(title='Вход', message='Успешный вход')
                    self.auth_win.destroy()  # Закрываем окно авторизации
                    self.open_admin_window()  # Открываем окно администрирования
                else:
                    showerror(title='Ошибка', message='Неверный логин или пароль.')
            except Exception as e:
                showwarning(title='warning', message=f'Ошибка при входе в систему: {e}')
        else:
            showerror(title='Error', message='Введите логин и пароль')