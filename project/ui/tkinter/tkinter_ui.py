import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os
import re


class TkinterUi:
    """
    Graphical User Interface for user interaction using Tkinter.
    """

    def __init__(self):
        """
        Initializes the TkinterUi class, setting up the main window.
        """
        self.window = tk.Tk()
        self.window.title("UI Manager")
        self.window.geometry("400x300")
        self.current_frame = None

    def switch_frame(self, new_frame):
        """
        Switches the current frame to a new frame.

        Args:
            new_frame (tk.Frame): The new frame to switch to.
        """
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill="both", expand=True)

    @staticmethod
    def add_info_button(frame, info_text):
        """
        Adds an information button with an icon to the frame.

        Args:
            frame (tk.Frame): The frame to which the button will be added.
            info_text (str): The information text to display when the button is clicked.
        """

        def show_info():
            messagebox.showinfo("Information", info_text)

        current_dir = os.path.dirname(__file__)
        icon_path = os.path.join(current_dir, "information-button.png")

        icon = Image.open(icon_path)
        icon = icon.resize((25, 25), Image.LANCZOS)
        icon_image = ImageTk.PhotoImage(icon)

        info_button = tk.Button(frame, image=icon_image, command=show_info, width=30, height=30)
        info_button.image = icon_image
        info_button.pack(anchor='ne', padx=5, pady=5)

    def mode_select(self) -> str:
        """
        Allows the user to select a mode (Twitter or News).

        Returns:
            str: Selected mode ('Twitter' or 'News').
        """
        frame = tk.Frame(self.window)
        selected_mode = tk.StringVar(value="Twitter")

        def set_mode():
            self.window.quit()

        tk.Label(frame, text="Seleccione la fuente para la extracción de información:").pack(pady=10)
        modes = [("Twitter", "Twitter"), ("Periódicos", "News")]
        for text, value in modes:
            tk.Radiobutton(frame, text=text, variable=selected_mode, value=value).pack(anchor=tk.W)
        tk.Button(frame, text="Continuar", command=set_mode).pack(pady=10)

        self.add_info_button(frame, "Seleccione 'Twitter' para extraer información de un usuario de Twitter "
                                    "o 'News' para extraer información de una noticia de un periódico en línea. "
                                    "Las extracciones se guardarán automáticamente en un archivo. Una vez "
                                    "seleccionado el modo, haga clic en 'Continuar'")
        self.switch_frame(frame)
        self.window.mainloop()
        return selected_mode.get()

    def personal_user_select(self, users: dict) -> dict:
        """
        Allows the user to select a personal user from the given dictionary of users.

        Args:
            users (dict): Dictionary of users where keys are user IDs and values are user details.

        Returns:
            dict: Details of the selected user.
        """
        frame = tk.Frame(self.window)
        selected_user = tk.StringVar(value=list(users.keys())[0])

        def set_user():
            self.window.quit()

        tk.Label(frame, text="Seleccione la cuenta para realizar la extracción:").pack(pady=10)
        user_menu = ttk.Combobox(frame, textvariable=selected_user, values=list(users.keys()))
        user_menu.pack(pady=5)
        user_menu.bind("<FocusIn>", lambda args: user_menu.selection_range(0, 'end'))
        tk.Button(frame, text="Continuar", command=set_user).pack(pady=10)

        self.add_info_button(
            frame,
            '''Seleccione la cuenta de la que desea extraer información. 
            Previamente, debe haber ingresado las credenciales en el archivo conf.py de la siguiente manera:

            user_dic = {
                "twitter_user": {
                    "username": "",
                    "password": "",
                    "email": "",
                    "account_password": ""
                }
            }
            Una vez seleccionada la cuenta, haga clic en Continuar''')
        self.switch_frame(frame)
        self.window.mainloop()
        return users[selected_user.get()]

    def prompt_select(self, prompts: dict) -> str:
        """
        Allows the user to select a prompt from the given dictionary of prompts.

        Args:
            prompts (dict): Dictionary of available prompts.

        Returns:
            str: Selected prompt.
        """
        frame = tk.Frame(self.window)
        selected_prompt = tk.StringVar(value=list(prompts.keys())[0])

        def set_prompt():
            self.window.quit()

        tk.Label(frame, text="Seleccione el prompt para realizar el informe:").pack(pady=10)
        prompt_menu = ttk.Combobox(frame, textvariable=selected_prompt, values=list(prompts.keys()))
        prompt_menu.pack(pady=5)
        prompt_menu.bind("<FocusIn>", lambda args: prompt_menu.selection_range(0, 'end'))
        tk.Button(frame, text="Continuar", command=set_prompt).pack(pady=10)

        self.add_info_button(frame, "Seleccione el prompt para realizar el informe. Luego, haga clic en Continuar")
        self.switch_frame(frame)
        self.window.mainloop()
        return prompts[selected_prompt.get()]

    def target_user_select(self) -> int:
        """
        Allows the user to enter the target user ID.

        Returns:
            int: Selected target user ID.
        """
        frame = tk.Frame(self.window)
        user_id = tk.StringVar()

        def set_user_id():
            if user_id.get().isdigit():
                self.window.quit()
            else:
                messagebox.showerror("Entrada Invalida", "Por favor introduce un número válido")

        tk.Label(frame, text="Introduce el ID de Twitter del cual quieres extraer información:").pack(pady=10)
        user_entry = tk.Entry(frame, textvariable=user_id)
        user_entry.pack(pady=5)
        user_entry.insert(0, "Introduce user ID")
        user_entry.bind("<FocusIn>", lambda args: user_entry.selection_range(0, 'end'))
        tk.Button(frame, text="Continuar", command=set_user_id).pack(pady=10)

        self.add_info_button(frame, "Introduce el ID del usuario de Twitter puedes utilizar la url: "
                                    "https://socialdata.tools/get-twitter-user-id. Una vez introducido el ID, "
                                    "haga clic en Continuar ")
        self.switch_frame(frame)
        self.window.mainloop()
        return int(user_id.get())

    def target_url_select(self) -> str:
        """
        Allows the user to enter a target URL.

        Returns:
            str: Selected target URL.
        """
        frame = tk.Frame(self.window)
        url = tk.StringVar()

        def is_valid_url(url: str) -> bool:
            pattern = re.compile(r"https?://(www\.)?(larazon|elmundo|elpais)\.(es|com)/.*")
            return bool(pattern.match(url))

        def set_url():
            if is_valid_url(url.get()):
                self.window.quit()
            else:
                messagebox.showerror("URL no válida", "Solo se permiten URLs de los periódicos La Razón, El Mundo y El País.")

        tk.Label(frame, text="Introduce la URL de la noticia de la que quieres extraer información:").pack(pady=10)
        url_entry = tk.Entry(frame, textvariable=url)
        url_entry.pack(pady=5)
        url_entry.insert(0, "Introduce la URL")
        url_entry.bind("<FocusIn>", lambda args: url_entry.selection_range(0, 'end'))
        tk.Button(frame, text="Continuar", command=set_url).pack(pady=10)

        self.add_info_button(frame, "Introduce la URL de la noticia del periódico en línea de la que quieres extraer "
                                    "información. Los periódicos compatibles son: La Razón, El Mundo, El País. Luego, "
                                    "haga clic en Continuar")
        self.switch_frame(frame)
        self.window.mainloop()
        return url.get()

    def continue_select(self) -> str:
        """
        Asks the user if they want to perform another operation.

        Returns:
            str: User's response in lowercase ('y' or 'n').
        """
        frame = tk.Frame(self.window)
        response = tk.StringVar(value="n")

        def set_response():
            self.window.quit()

        tk.Label(frame, text="¿Quiéres realizar más informes?").pack(pady=10)
        options = [("Sí", "y"), ("No", "n")]
        for text, value in options:
            tk.Radiobutton(frame, text=text, variable=response, value=value).pack(anchor=tk.W)
        tk.Button(frame, text="Continuar", command=set_response).pack(pady=10)

        self.add_info_button(frame, "Seleccione 'Sí' para realizar otra operación o 'No' para salir. Luego, "
                                    "haga clic en Continuar")
        self.switch_frame(frame)
        self.window.mainloop()
        return response.get()

    def model_select(self, models: list) -> str:
        """
        Allows the user to select a model from the given list of models.

        Args:
            models (list): List of available models.

        Returns:
            str: Selected model.
        """
        frame = tk.Frame(self.window)
        selected_model = tk.StringVar(value=models[0])

        def set_model():
            self.window.quit()

        tk.Label(frame, text="Selecciona el LLM con el que quieres realizar el informe:").pack(pady=10)
        model_menu = ttk.Combobox(frame, textvariable=selected_model, values=models)
        model_menu.pack(pady=5)
        model_menu.bind("<FocusIn>", lambda args: model_menu.selection_range(0, 'end'))
        tk.Button(frame, text="Continuar", command=set_model).pack(pady=10)

        self.add_info_button(frame, "Elija un modelo en el menú desplegable. Luego, haga clic en Continuar")
        self.switch_frame(frame)
        self.window.mainloop()
        return selected_model.get()

    def error(self, error_text: str):
        """
        Shows an error message.

        Args:
            error_text (str): The error message to display.
        """
        frame = tk.Frame(self.window)
        tk.Label(frame, text=error_text, fg="red").pack(pady=20)
        tk.Button(frame, text="OK", command=self.window.quit).pack(pady=10)

        self.add_info_button(frame, "Se ha producido un error. Por favor, siga las instrucciones para resolverlo.")
        self.switch_frame(frame)
        self.window.mainloop()

    def technology_select(self) -> str:
        """
        Allows the user to select a technology (OpenAI or Llama).

        Returns:
            str: Selected technology ('OpenAI' or 'Llama').
        """
        frame = tk.Frame(self.window)
        selected_technology = tk.StringVar(value="OpenAI")

        def set_technology():
            self.window.quit()

        tk.Label(frame, text="Selecciona la tecnología con el que quiere realizar el informe:").pack(pady=10)
        technologies = [("OpenAI", "OpenAI"), ("Llama", "Llama")]
        for text, value in technologies:
            tk.Radiobutton(frame, text=text, variable=selected_technology, value=value).pack(anchor=tk.W)
        tk.Button(frame, text="Continuar", command=set_technology).pack(pady=10)

        self.add_info_button(frame, "Selecciona 'OpenAI' o 'Llama' como tecnología a utilizar. Luego, haga clic en "
                                    "Continuar.")
        self.switch_frame(frame)
        self.window.mainloop()
        return selected_technology.get()

    def environment_select(self) -> str:
        """
        Allows the user to select an environment (Local or Online).

        Returns:
            str: Selected environment ('Local' or 'Online').
        """
        frame = tk.Frame(self.window)
        selected_environment = tk.StringVar(value="Local")

        def set_environment():
            self.window.quit()

        tk.Label(frame, text="Seleccione el entorno:").pack(pady=10)
        environments = [("Local", "Local"), ("Online", "Online")]
        for text, value in environments:
            tk.Radiobutton(frame, text=text, variable=selected_environment, value=value).pack(anchor=tk.W)
        tk.Button(frame, text="Continuar", command=set_environment).pack(pady=10)

        self.add_info_button(frame, "Seleccione 'Local' para generar un informe a partir de información ya extraída, "
                             "u 'Online' para realizar la extracción y luego el análisis. Luego, haga clic en "
                             "'Continuar'")
        self.switch_frame(frame)
        self.window.mainloop()
        return selected_environment.get()

    def file_select(self) -> str:
        """
        Allows the user to enter a file path.

        Returns:
            str: Selected file path.
        """
        frame = tk.Frame(self.window)
        file_path = tk.StringVar()

        def set_file_path():
            if file_path.get():
                self.window.quit()
            else:
                messagebox.showerror("Entrada no válida", "Please enter a valid file path.")

        tk.Label(frame, text="Enter the file path:").pack(pady=10)
        file_entry = tk.Entry(frame, textvariable=file_path)
        file_entry.pack(pady=5)
        file_entry.insert(0, "Introduce la ruta de un informe de información")
        file_entry.bind("<FocusIn>", lambda args: file_entry.selection_range(0, 'end'))
        tk.Button(frame, text="Continuar", command=set_file_path).pack(pady=10)

        self.add_info_button(frame, "La ruta debe ser de un informe en formato JSON creado por el programa en una "
                             "ejecución anterior. Introduce la ruta del archivo y luego haga clic en 'Continuar'.")

        self.switch_frame(frame)
        self.window.mainloop()
        return file_path.get()

    def show_report(self, report_type: str):
        """
        Shows a final screen indicating the end of the process.

        Args:
            report_type (str): The type of report generated.
        """
        frame = tk.Frame(self.window)
        tk.Label(frame, text=f"Se ha escrito {report_type}").pack(pady=20)
        tk.Button(frame, text="Continuar", command=self.window.quit).pack(pady=10)

        self.add_info_button(frame, f'Se ha escrito el informe {report_type} de manera correcta')
        self.switch_frame(frame)
        self.window.mainloop()
