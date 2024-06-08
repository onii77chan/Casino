
from BlackJack import (
    BlackJack

)

from logic import (
    user_input,

)

from casino import (
    log_called_method_name,

)

command_list = {'1': 'start game', '2': '?', '0': 'exit'}


@log_called_method_name
def main():
    while True:
        user_input_data = user_input(command_list)


main()
