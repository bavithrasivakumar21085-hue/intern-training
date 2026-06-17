# To do list program

tasks=[1,2,3,4]

def add_task():
    add_task= input("Enter Task:")
    tasks.append(add_task)
    print("Task added")


def remove_task():
    remove_task = input("Enter the task to remove:")
    if remove_task in tasks:
        tasks.remove(remove_task)
        print("Task Removed")
    else:
        print("Invalid Task")
    
def list_tasks():
    for task in tasks:
        print(task)

