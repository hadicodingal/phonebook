phonebook={}

def addcontact( phonebook,name,number):
    if  name in phonebook:
      print("This contact already exsists")
    else:
       phonebook[name]=number
       print("Contact added succesfully")
def deletecontact(phonebook,name):
    if  name not in phonebook:
      print("This contact does not exsist")
    else:
       del phonebook[name]
       print("Contact deleted succesfully")
def searchcontact(phonebook,name):
    if  name not in phonebook:
      print("This contact does not exsist")
    else:
       print(f"Phone number of {name} is {phonebook[name]}")
def allcontact(phonebook):
    if not phonebook:
      print("phonebook is empty")
    else:
       print("--- Phonebook Contacts ---")
       for name, number in phonebook.items():

            print(f"{name}: {number}")

            print("------------------------")
def menu():
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Get Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            addcontact(phonebook,name, number)
        elif choice==2:
           name=input("enter the name to search :")
           searchcontact(phonebook,name)
        elif choice==3:
           name=input("enter the contact name to delete")
           deletecontact(phonebook,name)
        elif choice==4:
           allcontact(phonebook)
        elif choice==5:
           break
        else :
           print("invalid input")
menu()
    



                
           
         
       
    
      
     
    