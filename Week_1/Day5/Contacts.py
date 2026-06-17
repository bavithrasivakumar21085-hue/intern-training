#contact book
contacts ={}

def add_contact():
    name= input("Enter the name:") 
    try:
        phone= int(input("Enter phone number:"))
        contacts[name]=phone
        print("Contact Added")
    except ValueError:
        print("Phone number must be integer")       
               

def find_contact():
    name= input("enter contact name:")
    try:
        print(contacts[name])
    except KeyError:
            print("contact not found")
   
    

def list_contact():
    try:
        for name,number in contacts.items():
            print(name,number)
        if not contacts:
            print("no contacts found")
    except Exception as e:
        print(e)

