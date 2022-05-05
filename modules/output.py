from modules.input import *


def print_task(task):
    print(f'Description: { task["description"] }')
    print(f'Status: { "Completed" if task["completed"] else "Incomplete"}')
    print(f'Time Taken: {task["time_taken"]} mins')


def print_list(list):
    for task in list:
        print_task(task)


def print_menu():
    print("Options:")
    print("1: Display All Tasks")
    print("2: Get Uncompleted Tasks")
    print("3: Get Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("8: Get List of Tasks with Given Status")
    print("M or m: Display this menu")
    print("Q or q: Quit")


def print_load_tasks():
    print("would you like to populate the list?")
    return get_list()
