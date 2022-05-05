from modules.output import *
from modules.task_list import *
from modules.input import *


def list_status(user_input):
    if user_input == "yes":
        from data.task_list import tasks

        return tasks
    if user_input == "no":
        from data.task_list import new_tasks

        return new_tasks


tasks = list_status(print_load_tasks())
while True:
    print_menu()
    option = input("Select an option 1, 2, 3, 4, 5, 6, 7, 8 display (m)enu or (q)uit: ")
    if option.lower() == "q":
        break
    if option == "1":
        print_list(tasks)
    elif option == "2":
        print_list(get_uncompleted_tasks(tasks))
    elif option == "3":
        print_list(get_completed_tasks(tasks))
    elif option == "4":
        description = get_description()
        task = get_task_with_description(tasks, description)
        if task is not None:
            mark_task_complete(task)
            print("Task marked complete")
        else:
            print("Task not found")
    elif option == "5":
        time = get_time_taken()
        print_list(get_tasks_taking_at_least(tasks, time))
    elif option == "6":
        description = get_description()
        print(get_task_with_description(tasks, description))
    elif option == "7":
        description = get_description()
        time_taken = get_time_taken()
        task = create_task(description, time_taken)
        tasks.append(task)
    elif option == "8":
        status = get_status()
        print_list(get_tasks_by_status(tasks, status))
    else:
        print("Invalid Input - choose another option")
