# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    uncompleted_tasks = []
    for l in list:
        if l["completed"] == False:
            uncompleted_tasks.append(l)
    return uncompleted_tasks


## Get a list of completed tasks
def get_completed_tasks(list):
    completed_list = []
    for l in list:
        if l["completed"] == True:
            completed_list.append(l)
    return completed_list


## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    time_taken = []
    for l in list:
        if l["time_taken"] > time:
            time_taken.append(l)
    return time_taken


## Find a task with a given description
def get_task_with_description(list, description):
    for l in list:
        if l["description"] == description:
            return l


# Extention (Function):

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    tasks = []
    for l in list:
        if l["completed"] == status:
            tasks.append(l)
    return tasks


def mark_task_complete(task):
    task["completed"] = True


def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task


def add_to_list(list, task):
    list.append(task)
