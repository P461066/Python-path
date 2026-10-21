contacts = {
    "Mpho": "23-456-7890",
    "lesedi": "0732 765-4321",
    "thato": "555-555-5555",
}

name = input("Enter a name to look up: ")
if name in contacts:
    print(f"{name}: {contacts[name]}")
else:
    print(f"{name} is not in the contact list.")