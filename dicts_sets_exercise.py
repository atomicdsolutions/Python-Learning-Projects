# Create a contact list using a dictionary.
contact =[
    {"name": "John Doe",
    "phone": "123-456-7890"},
    {"name": "Jane Doe",
    "phone": "123-456-7890"},
    {"name": "John Smith",
    }
]

def add_contact(name, phone):
    contact.append({"name": name, "phone": phone})
    
def remove_contact(name):
    for i in range(len(contact)):
        if contact[i]["name"] == name:
            contact.pop(i)
            break
def list_contacts():
    for i in range(len(contact)):
        print(f'{contact[i]["name"]}: {contact[i]["phone"]}')

cities_visited ={"NYC", "LA", "SF"}

def add_city(city):
    cities_visited.add(city)

def check_city(city):
    return city in cities_visited

list_contacts()

add_contact("John Done", "123-456-7890")

remove_contact("John Done")

print(check_city("NYC"))

add_city("BS")