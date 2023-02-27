import interface
import data

data.import_from_file("contacts")

while True:
    num_op = interface.action_choice()
    print(interface.start_action(num_op))
    if num_op == 5:
        break