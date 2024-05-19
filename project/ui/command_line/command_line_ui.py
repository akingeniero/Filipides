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
