from project.ui.ui_manager import UiManager


class CommandLineUi(UiManager):
    """
    Command-line interface for user interaction, inheriting from UiManager.

    Methods:
        personal_user_select(users: dict) -> dict:
            Allows user to select a personal user from a provided dictionary of users.

        prompt_select(prompts: dict) -> str:
            Allows user to select a prompt from a provided dictionary of prompts.

        target_user_select() -> int:
            Allows user to enter a target user's ID.
    """

    def mode_select(self: 'CommandLineUi') -> str:
        """
        Allows the user to select a mode (Twitter or News) and a personal user from the given dictionary of users.

        Args:
            self: Instance of CommandLineUi.
            users (dict): Dictionary of users where keys are user IDs and values are user details.

        Returns:
            dict or None: Selected user's details (ID and mode).
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
            dict: Selected user's ID.
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
        Allows the user to select a prompt from the given list of prompts.

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
        Allows the user to enter a target url.

        Args:
            self: Instance of CommandLineUi.

        Returns:
            str: Selected target url.
        """
        while True:
            url_input = input("Enter the target url: ").strip()
            return url_input

    def continue_select(self) -> str:
        """
        Asks the user if they want to perform another operation.

        Returns:
            str: The user's response in lowercase.
        """
        while True:
            response = input("Do you want to perform another operation? (y/n): ").strip().lower()
            if response in ['y', 'n']:
                return response
            else:
                print("Invalid answer. Please enter 'y' for yes or 'n' for no.")
