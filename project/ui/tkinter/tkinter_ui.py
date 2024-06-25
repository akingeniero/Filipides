import tkinter as tk
from tkinter import messagebox, ttk


class TkinterUi:
    """
    Graphical user interface for user interaction using Tkinter.
    """

    def __init__(self):
        self.window = None

    def init_window(self):
        """
        Initializes the Tkinter window.
        """
        if self.window is None or not self.window.winfo_exists():
            self.window = tk.Tk()
            self.window.title("UI Manager")
            self.window.geometry("300x200")
        else:
            self.window.deiconify()

    def destroy_window(self):
        """
        Destroys the Tkinter window.
        """
        if self.window and self.window.winfo_exists():
            self.window.destroy()
            self.window = None

    def mode_select(self) -> str:
        """
        Allows the user to select a mode (Twitter or News).

        Returns:
            str: Selected mode ('Twitter' or 'News').
        """
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
        """
        Allows the user to select a personal user from the given dictionary of users.

        Args:
            users (dict): Dictionary of users where keys are user IDs and values are user details.

        Returns:
            dict: Selected user's details.
        """
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
        """
        Allows the user to select a prompt from the given dictionary of prompts.

        Args:
            prompts (dict): Dictionary of available prompts.

        Returns:
            str: Selected prompt.
        """
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
        """
        Allows the user to enter a target user's ID.

        Returns:
            int: Selected target user's ID.
        """
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
        """
        Allows the user to enter a target URL.

        Returns:
            str: Selected target URL.
        """
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
        """
        Asks the user if they want to perform another operation.

        Returns:
            str: The user's response in lowercase ('y' or 'n').
        """
        self.init_window()
        response = tk.StringVar(value="n")

        def set_response():
            self.window.quit()

        tk.Label(self.window, text="Do you want to perform another operation? (y/n):").pack(pady=10)
        tk.Radiobutton(self.window, text="Yes", variable=response, value="y").pack(anchor=tk.W)
        tk.Radiobutton(self.window, text="No", variable=response, value="n").pack(anchor=tk.W)
        tk.Button(self.window, text="Submit", command=set_response).pack(pady=10)

        self.window.mainloop()
        self.destroy_window()

        return response.get()

    def model_select(self, models: list) -> str:
        """
        Allows the user to select a model from the given list of models.

        Args:
            models (list): List of available models.

        Returns:
            str: Selected model.
        """
        self.init_window()
        selected_model = tk.StringVar(value=models[0])

        def set_model():
            self.window.quit()

        tk.Label(self.window, text="Select model:").pack(pady=10)

        model_menu = ttk.Combobox(self.window, textvariable=selected_model, values=models)
        model_menu.pack(pady=5)

        tk.Button(self.window, text="Select", command=set_model).pack(pady=10)

        self.window.mainloop()
        self.destroy_window()

        return selected_model.get()

    def error(self, error_text: str):
        """
        Displays an error message.

        Args:
            error_text (str): The error message to display.

        Returns:
            None
        """
        self.init_window()
        messagebox.showerror("Error", error_text)
        self.destroy_window()

    def technology_select(self) -> str:
        """
        Allows the user to select a technology (OpenAI or Llama).

        Returns:
            str: Selected technology ('OpenAI' or 'Llama').
        """
        self.init_window()
        selected_technology = tk.StringVar(value="OpenAI")

        def set_technology():
            self.window.quit()

        tk.Label(self.window, text="Select technology:").pack(pady=10)
        tk.Radiobutton(self.window, text="OpenAI", variable=selected_technology, value="OpenAI").pack(anchor=tk.W)
        tk.Radiobutton(self.window, text="Llama", variable=selected_technology, value="Llama").pack(anchor=tk.W)
        tk.Button(self.window, text="Select", command=set_technology).pack(pady=10)

        self.window.mainloop()
        self.destroy_window()

        return selected_technology.get()
