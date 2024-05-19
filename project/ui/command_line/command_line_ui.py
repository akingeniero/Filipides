from project.ui.ui_manager import UiManager


class CommandLineUi(UiManager):

    def personal_user_select(self, users: dict) -> str:
        available_users = users.keys()
        while True:
            print("Available user:", ', '.join(available_users))
            user = input("Enter the user for setup: ").strip()
            if user in available_users:
                return users[user]
            else:
                print("Invalid user. Please select a valid user from the list.")

    def prompt_select(self, prompts) -> str:
        while True:
            print("Available prompts:")
            for key in prompts.keys():
                print(f"- {key}")

            prompt_key = input("Please enter the key of the prompt you want to use: ")
            if prompt_key in prompts:
                return prompts[prompt_key]
            else:
                print("Invalid prompt key. Please try again.")

    def target_user_select(self) -> int:
        while True:
            user_input = input("Enter the target user (numbers only): ")
            if user_input.isdigit():
                return int(user_input)
            else:
                print("Invalid input. Please enter a number.")
