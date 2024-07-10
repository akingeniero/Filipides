import re


class CommandLineUi:
    """
    Command-line interface for user interaction.
    """

    def mode_select(self) -> str:
        """
        Allows the user to select a mode (Twitter or News).

        Returns:
            str: Selected mode ('Twitter' or 'News').
        """
        while True:
            print("Seleccione el modo:")
            print("1. Modo Twitter")
            print("2. Modo Noticias")
            mode_choice = input("Ingrese la opción de modo (1 o 2): ").strip()

            if mode_choice == '1':
                return 'Twitter'
            elif mode_choice == '2':
                return 'Noticias'
            else:
                print("Opción de modo inválida. Por favor ingrese 1 o 2.")

    def personal_user_select(self, users: dict) -> dict:
        """
        Allows the user to select a personal user from the given dictionary of users.

        Args:
            users (dict): Dictionary of users where keys are user IDs and values are user details.

        Returns:
            dict: Selected user's details.
        """
        available_users = list(users.keys())
        while True:
            print("Usuarios disponibles:")
            for i, user in enumerate(available_users):
                print(f"{i + 1}. {user}")

            user_choice = input("Ingrese el número del usuario para configurar: ").strip()
            if user_choice.isdigit() and 1 <= int(user_choice) <= len(available_users):
                return users[available_users[int(user_choice) - 1]]
            else:
                print("Número de usuario inválido. Por favor seleccione un usuario válido de la lista.")

    def prompt_select(self, prompts: dict) -> str:
        """
        Allows the user to select a prompt from the given dictionary of prompts.

        Args:
            prompts (dict): Dictionary of available prompts.

        Returns:
            str: Selected prompt.
        """
        prompt_keys = list(prompts.keys())
        while True:
            print("Prompts disponibles:")
            for i, key in enumerate(prompt_keys):
                print(f"{i + 1}. {key}")

            choice = input("Por favor ingrese el número del prompt que desea usar: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(prompt_keys):
                return prompts[prompt_keys[int(choice) - 1]]
            else:
                print("Número de prompt inválido. Por favor intente de nuevo.")

    def target_user_select(self) -> int:
        """
        Allows the user to enter a target user's ID.

        Returns:
            int: Selected target user's ID.
        """
        while True:
            user_input = input("Ingrese el usuario objetivo (solo números): ").strip()
            if user_input.isdigit():
                return int(user_input)
            else:
                print("Entrada inválida. Por favor ingrese un número.")

    def target_url_select(self) -> str:
        """
        Allows the user to enter a target URL.

        Returns:
            str: Selected target URL.
        """

        def is_valid_url(url: str) -> bool:
            # Define the regex pattern for allowed URLs
            pattern = re.compile(r"https?://(www\.)?(larazon|elmundo|elpais)\.(es|com)/.*")
            return bool(pattern.match(url))

        while True:
            url_input = input("Ingrese la URL objetivo: ").strip()
            if is_valid_url(url_input):
                return url_input
            else:
                print("URL no válida. Solo se permiten URLs de los periódicos La Razón, El Mundo y El País.")

    def continue_select(self) -> str:
        """
        Asks the user if they want to perform another operation.

        Returns:
            str: The user's response in lowercase ('y' or 'n').
        """
        while True:
            response = input("¿Desea realizar otra operación? (s/n): ").strip().lower()
            if response in ['s', 'n']:
                return response
            else:
                print("Respuesta inválida. Por favor ingrese 's' para sí o 'n' para no.")

    def model_select(self, models: list) -> str:
        """
        Allows the user to select a model from the given list of models.

        Args:
            models (list): List of available models.

        Returns:
            str: Selected model.
        """
        while True:
            print("Modelos disponibles:")
            for i, model in enumerate(models):
                print(f"{i + 1}: {model}")

            try:
                model_index = int(input("Por favor ingrese el número del modelo que desea usar: ").strip())
                if 1 <= model_index <= len(models):
                    return models[model_index - 1]
                else:
                    print("Número inválido. Por favor intente de nuevo.")
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número.")

    def error(self, error_text: str):
        """
        Displays an error message.

        Args:
            error_text (str): The error message to display.
        """
        print(f"Error: {error_text}")

    def technology_select(self) -> str:
        """
        Allows the user to select a technology (OpenAI or Llama).

        Returns:
            str: Selected technology ('OpenAI' or 'Llama').
        """
        while True:
            print("Seleccione la tecnología:")
            print("1. OpenAI")
            print("2. Llama")
            tech_choice = input("Ingrese la opción de tecnología (1 o 2): ").strip()

            if tech_choice == '1':
                return 'OpenAI'
            elif tech_choice == '2':
                return 'Llama'
            else:
                print("Opción de tecnología inválida. Por favor ingrese 1 o 2.")

    def environment_select(self) -> str:
        """
        Allows the user to select an environment (Local or Online).

        Returns:
            str: Selected environment ('Local' or 'Online').
        """
        while True:
            print("Seleccione el entorno:")
            print("1. Local")
            print("2. Online")
            env_choice = input("Ingrese la opción de entorno (1 o 2): ").strip()

            if env_choice == '1':
                return 'Local'
            elif env_choice == '2':
                return 'Online'
            else:
                print("Opción de entorno inválida. Por favor ingrese 1 o 2.")

    def file_select(self) -> str:
        """
        Allows the user to enter a file path.

        Returns:
            str: Selected file path.
        """
        while True:
            file_path = input("Ingrese la ruta del archivo: ").strip()
            if file_path:
                return file_path
            else:
                print("Por favor ingrese una ruta de archivo válida.")

    def show_report(self, report_type: str):
        """
        Shows a final screen indicating the end of the process.

        Args:
            report_type (str): The type of report generated.
        """
        print(f"Se ha escrito el informe: {report_type}")
        input("Presione Enter para continuar...")
