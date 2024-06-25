class CommandLineUi:
    """
    Command-line interface for user interaction.
    """

    def mode_select(self) -> str:
        """
        Allows the user to select a mode (Twitter or News).

        Args:
            self: Instance of CommandLineUi.

        Returns:
            str: Selected mode ('Twitter' or 'News').
        """
        while True:
            print("Select mode:")
            print("1. Twitter mode")
            print("2. News mode")
            mode_choice = input("Enter mode choice (1 or 2): ").strip()

            if mode_choice == '1':
                return 'Twitter'
            elif mode_choice == '2':
                return 'News'
            else:
                print("Invalid mode choice. Please enter 1 or 2.")

    def personal_user_select(self: 'CommandLineUi', users: dict) -> dict:
        """
        Allows the user to select a personal user from the given dictionary of users.

        Args:
            self: Instance of CommandLineUi.
            users (dict): Dictionary of users where keys are user IDs and values are user details.

        Returns:
            dict: Selected user's details.
        """
        available_users = users.keys()
        while True:
            print("Available users:", ', '.join(available_users))
            user = input("Enter the user for setup: ").strip()
            if user in available_users:
                return users[user]
            else:
                print("Invalid user. Please select a valid user from the list.")

    def prompt_select(self: 'CommandLineUi', prompts: dict) -> str:
        """
        Allows the user to select a prompt from the given dictionary of prompts.

        Args:
            self: Instance of CommandLineUi.
            prompts (dict): Dictionary of available prompts.

        Returns:
            str: Selected prompt.
        """
        while True:
            print("Available prompts:")
            for key in prompts.keys():
                print(f"- {key}")

            prompt_key = input("Please enter the key of the prompt you want to use: ").strip()
            if prompt_key in prompts:
                return prompts[prompt_key]
            else:
                print("Invalid prompt key. Please try again.")

    def target_user_select(self: 'CommandLineUi') -> int:
        """
        Allows the user to enter a target user's ID.

        Args:
            self: Instance of CommandLineUi.

        Returns:
            int: Selected target user's ID.
        """
        while True:
            user_input = input("Enter the target user (numbers only): ").strip()
            if user_input.isdigit():
                return int(user_input)
            else:
                print("Invalid input. Please enter a number.")

    def target_url_select(self: 'CommandLineUi') -> str:
        """
        Allows the user to enter a target URL.

        Args:
            self: Instance of CommandLineUi.

        Returns:
            str: Selected target URL.
        """
        while True:
            url_input = input("Enter the target url: ").strip()
            return url_input

    def continue_select(self) -> str:
        """
        Asks the user if they want to perform another operation.

        Returns:
            str: The user's response in lowercase ('y' or 'n').
        """
        while True:
            response = input("Do you want to perform another operation? (y/n): ").strip().lower()
            if response in ['y', 'n']:
                return response
            else:
                print("Invalid answer. Please enter 'y' for yes or 'n' for no.")

    def model_select(self: 'CommandLineUi', models: list) -> str:
        """
        Allows the user to select a model from the given list of models.

        Args:
            self: Instance of CommandLineUi.
            models (list): List of available models.

        Returns:
            str: Selected model.
        """
        while True:
            print("Available models:")
            for i, model in enumerate(models):
                print(f"{i + 1}: {model}")

            try:
                model_index = int(input("Please enter the number of the model you want to use: ").strip())
                if 1 <= model_index <= len(models):
                    return models[model_index - 1]
                else:
                    print("Invalid number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def error(self, error_text: str):
        """
        Displays an error message.

        Args:
            self: Instance of CommandLineUi.
            error_text (str): The error message to display.

        Returns:
            None
        """
        print(error_text)

    def technology_select(self: 'CommandLineUi') -> str:
        """
        Allows the user to select a technology (OpenAI or Llama).

        Args:
            self: Instance of CommandLineUi.

        Returns:
            str: Selected technology ('OpenAI' or 'Llama').
        """
        while True:
            print("Select technology:")
            print("1. OpenAI")
            print("2. Llama")
            tech_choice = input("Enter technology choice (1 or 2): ").strip()

            if tech_choice == '1':
                return 'OpenAI'
            elif tech_choice == '2':
                return 'Llama'
            else:
                print("Invalid technology choice. Please enter 1 or 2.")
