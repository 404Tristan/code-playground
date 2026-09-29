# Day 4: List and Functions
# Task : create "Task Tracker / To-Do List Tool"

tasks = []

def add_task(task_list,user_added_task):
    task_list.append(user_added_task)
    return task_list

def show_tasks(user_tasks):
    print("Your current task: ")
    for task in user_tasks:
        print(f" - {task}")

print("Just press enter or type 'Done' if your finished adding task")
while True:
    user_task_input = input("Add task: ").lower()
    if user_task_input == '' or user_task_input == "done":
        break

    tasks = add_task(tasks,user_task_input)

print()

show_task = input("Show task, Yes or No? ").lower()
for has_y in show_task:
    if has_y == 'y':
        show_tasks(tasks)
        break

    else:
        print("Thanks for using our app :)")
        break
