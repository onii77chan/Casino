from casino import (
    Casino, CardGame,
    deck,

)
separate_of_the_text = '_____________________________________________________________________'


def start_new_game():
    print(f'{separate_of_the_text}\n'
          'start_new_game_method_called\n'
          f'{separate_of_the_text}')


commands_in_main_menu = {
    '1': start_new_game, '2': 'exit'
}


def user_input(list_of_available_commands):
    while True:
        print("Список доступных команд:")
        for key, value in list_of_available_commands.items():
            if callable(value):
                print(f"{key}: {value.__name__}")
            else:
                print(f"{key}: {value}")

        user_input_data = input("Input: ")

        if user_input_data == '2':
            return 'exit'
        elif user_input_data in list_of_available_commands:
            command = list_of_available_commands[user_input_data]
            if callable(command):
                command()
            else:
                print(f"Executing command: {command}")
        else:
            print(f"{separate_of_the_text}"
                  "\nInvalid input\n"
                  f"{separate_of_the_text}")


def main():
    while True:
        result = user_input(commands_in_main_menu)
        if result == 'exit':
            print(f'{separate_of_the_text}\n'
                  'bye bye\n')
            break


if __name__ == "__main__":
    main()
