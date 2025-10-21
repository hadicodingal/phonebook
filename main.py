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

    
      
     
    