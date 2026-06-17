#contact book
contacts ={}

def add_contact():
    name= input("Enter the name:")
    phone= input("Enter phone number:") 
    contacts[name]=phone
    print("Contact Added")

def find_contact():
    name= input("enter contact name:")
    if name in contacts:
        print(contacts[name])
    else:
        print("contact not found")

def list_contact():
    for name,number in contacts.items():
        print(name,number)
    if not contacts:
        print("no contacts found")

while True:
    print("1. Add Contact")
    print("2. Find Contact")
    print("3. List Contacts")
    print("4. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        add_contact()

    elif choice == "2":
        find_contact()
    
    elif choice == "3":
        list_contact()

    elif choice == "4":
        break
    else:
        print("Invalid choice")

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

while True:
    print("1.Add Task:")
    print("2.Remove")
    print("List tasks")
    print("4. Exit")
    choice= input("Enter your choice:")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        list_tasks()
    elif choice == "4":
        break
    else:
        print("invalid input")
