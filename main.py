
from Week_1.Day5 import Contacts
from Week_1.Day5 import to_do_list

while True:
    print("1. Add Contact")
    print("2. Find Contact")
    print("3. List Contacts")
    print("4. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        Contacts.add_contact()

    elif choice == "2":
        Contacts.find_contact()
    
    elif choice == "3":
        Contacts.list_contact()

    elif choice == "4":
        break
    else:
        print("Invalid choice")



while True:
    print("1.Add Task:")
    print("2.Remove")
    print("List tasks")
    print("4. Exit")
    
    try:
        choice= int(input("Enter your choice:"))
    except:
        print("The input must be integer")
   
    if choice == 1:
        to_do_list.add_task()

    elif choice == 2:
        to_do_list.remove_task()
   
    elif choice == 3:
        to_do_list.list_tasks()

    elif choice == 4:
        break
    else:
        print("invalid input")
