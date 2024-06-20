import tkinter as tk
from tkinter import messagebox, ttk


class TkinterUi:
    def __init__(self):
        self.window = None

    def init_window(self):
        if self.window is None or not self.window.winfo_exists():
            self.window = tk.Tk()
            self.window.title("UI Manager")
            self.window.geometry("300x200")
        else:
            self.window.deiconify()

    def destroy_window(self):
        if self.window and self.window.winfo_exists():
            self.window.destroy()
            self.window = None

    def mode_select(self) -> str:
        self.init_window()
        selected_mode = tk.StringVar(value="Twitter")

        def set_mode():
            self.window.quit()

        tk.Label(self.window, text="Select mode:").pack(pady=10)
        tk.Radiobutton(self.window, text="Twitter mode", variable=selected_mode, value="Twitter").pack(anchor=tk.W)
        tk.Radiobutton(self.window, text="News mode", variable=selected_mode, value="News").pack(anchor=tk.W)
        tk.Button(self.window, text="Select", command=set_mode).pack(pady=10)

        self.window.mainloop()
        self.destroy_window()

        return selected_mode.get()

    def personal_user_select(self, users: dict) -> dict:
        self.init_window()
        selected_user = tk.StringVar(value=list(users.keys())[0])

        def set_user():
            self.window.quit()

        tk.Label(self.window, text="Select user:").pack(pady=10)

        user_menu = ttk.Combobox(self.window, textvariable=selected_user, values=list(users.keys()))
        user_menu.pack(pady=5)

        tk.Button(self.window, text="Select", command=set_user).pack(pady=10)

        try:
            self.window.mainloop()
        except Exception as e:
            print("Exception occurred:")
            import traceback
            traceback.print_exc()
        finally:
            self.destroy_window()

        return users[selected_user.get()]

    def prompt_select(self, prompts: dict) -> str:
        self.init_window()
        selected_prompt = tk.StringVar(value=list(prompts.keys())[0])

        def set_prompt():
            self.window.quit()

        tk.Label(self.window, text="Select prompt:").pack(pady=10)

        prompt_menu = ttk.Combobox(self.window, textvariable=selected_prompt, values=list(prompts.keys()))
        prompt_menu.pack(pady=5)

        tk.Button(self.window, text="Select", command=set_prompt).pack(pady=10)

        self.window.mainloop()
        self.destroy_window()

        return prompts[selected_prompt.get()]

    def target_user_select(self) -> int:
        self.init_window()
        user_id = tk.StringVar()

        def set_user_id():
            if user_id.get().isdigit():
                self.window.quit()
            else:
                messagebox.showerror("Invalid Input", "Please enter a valid number.")

        tk.Label(self.window, text="Enter user ID:").pack(pady=10)
        tk.Entry(self.window, textvariable=user_id).pack(pady=5)
        tk.Button(self.window, text="Submit", command=set_user_id).pack(pady=10)

        self.window.mainloop()
        self.destroy_window()

        return int(user_id.get())

    def target_url_select(self) -> str:
        self.init_window()
        url = tk.StringVar()

        def set_url():
            if url.get():
                self.window.quit()
            else:
                messagebox.showerror("Invalid Input", "Please enter a valid URL.")

        tk.Label(self.window, text="Enter target URL:").pack(pady=10)
        tk.Entry(self.window, textvariable=url).pack(pady=5)
        tk.Button(self.window, text="Submit", command=set_url).pack(pady=10)

        self.window.mainloop()
        self.destroy_window()

        return url.get()

    def continue_select(self) -> str:
        self.init_window()
        response = tk.StringVar(value="n")

        def set_response():
            self.window.quit()

        tk.Label(self.window, text="¿Desea realizar otra operación? (y/n):").pack(pady=10)
        tk.Radiobutton(self.window, text="Sí", variable=response, value="y").pack(anchor=tk.W)
        tk.Radiobutton(self.window, text="No", variable=response, value="n").pack(anchor=tk.W)
        tk.Button(self.window, text="Aceptar", command=set_response).pack(pady=10)

        self.window.mainloop()
        self.destroy_window()

        return response.get()

    def error(self, error_text: str):
        self.init_window()
        messagebox.showerror("Error", error_text)
        self.destroy_window()
