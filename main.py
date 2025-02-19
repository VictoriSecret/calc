import sqlite3
import customtkinter as ctk
from tkinter import messagebox

# Инициализация customtkinter
ctk.set_appearance_mode("Dark")  # "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

class Database:
    def __init__(self, db_name='podgotovka.db'):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                            id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                            login TEXT NOT NULL UNIQUE,
                            password TEXT NOT NULL,
                            role TEXT NOT NULL)
                        """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS singers (
                            id_singer INTEGER PRIMARY KEY AUTOINCREMENT,
                            nickname TEXT NOT NULL UNIQUE
                        )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS concerts (
                            id_concert INTEGER PRIMARY KEY AUTOINCREMENT,
                            name_concert TEXT NOT NULL,
                            id_singer INTEGER,
                            date DATETIME,
                            count_tickets INTEGER NOT NULL,
                            price INTEGER NOT NULL,
                            FOREIGN KEY (id_singer) REFERENCES singers(id_singer)
                        )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS registration (
                            id_registration INTEGER PRIMARY KEY AUTOINCREMENT,
                            id_user INTEGER,
                            id_concert INTEGER,
                            FOREIGN KEY (id_user) REFERENCES users(id_user),
                            FOREIGN KEY (id_concert) REFERENCES concerts(id_concert)
                        )""")
        conn.commit()
        conn.close()

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Авторизация")
        self.geometry("962x682")

        self.db = Database()
        self.db.create_table()

        self.label = ctk.CTkLabel(self, text="NightMoscow", text_color='#fafafa',
                                  font=('Arial', 55))
        self.label.place(x=320, y=200)
        self.label1 = ctk.CTkLabel(self, text="Введите данные для входа", text_color='#a9a9a9',
                                  font=('Arial', 15))
        self.label1.place(x=375, y=270)

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Login",
                                           font=('Arial', 15), text_color='#a9a9a9',
                                           width=300)
        self.username_entry.place(x=330, y=310)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*",
                                           font=('Arial', 15), text_color='#a9a9a9',
                                           width=300)
        self.password_entry.place(x=330, y=350)

        self.login_button = ctk.CTkButton(self, text="Войти", command=self.login,
                                          fg_color='transparent', hover_color='#7b68ee',
                                          border_width=1, border_color='#fafafa', width=200)
        self.login_button.place(x=380, y=400)

    def login(self):
        admin = self.username_entry.get()
        password = self.password_entry.get()

        # Пример проверки учетных данных
        if self.check_credentials(admin, password):
            messagebox.showinfo("Успех", "Вы успешно вошли в систему!")
            self.open_admin_window()
        else:
            messagebox.showerror("Ошибка", "Неверное имя пользователя или пароль.")

    def check_credentials(self, admin, password):
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT id_user FROM users WHERE login=? AND password=?", (admin, password))
            result = cursor.fetchone()
            conn.close()
            return result is not None
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при проверке учетных данных: {e}")
            return False

    def open_admin_window(self):
        AdminWindow(self)

class AdminWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Окно администрирования")
        self.geometry("962x682")

        self.label = ctk.CTkLabel(self, text="Окно администрирования",
                                  font=('Arial', 55), text_color='#fafafa')
        self.label.pack(pady=20)

        self.profile_button = ctk.CTkButton(self, text="Профиль", command=self.show_profile)
        self.profile_button.pack(pady=10)

        self.enty_admin = ctk.CTkEntry(self, placeholder_text='Start message..',
                                       font=('Arial', 15), width=300)
        self.enty_admin.pack(pady=20)

        self.text_area = ctk.CTkTextbox(self, height=10, width=100)
        self.text_area.pack(pady=20)

        var = ctk.IntVar()
        self.checkbox_admin = ctk.CTkCheckBox(self, text='Choice me', variable=var)
        self.checkbox_admin.pack(pady=20)
        var2 = ctk.IntVar()
        self.checkbox_admin2 = ctk.CTkCheckBox(self, text='Choice me', variable=var2)
        self.checkbox_admin2.pack(pady=5)

        radio_var = ctk.StringVar(value='option1')
        self.radio1 = ctk.CTkRadioButton(self, variable=radio_var, value='option1')
        self.radio2 = ctk.CTkRadioButton(self, variable=radio_var, value='option2')
        self.radio1.pack(pady=10)
        self.radio2.pack(pady=5)



    def show_profile(self):
        messagebox.showinfo("Профиль", "Здесь будет информация о профиле.")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()