# initialize contacts dictionary holding email addresses for each contact

contacts = {
    "Mpho": "mpho@example.com",
    "Thato": "thato@example.com",
    "Basile": "basile@example.com"

}
## initialize city dictionary holding city names for each contact
city = {
    "Mpho": "Johannesburg",
    "Thato": "Cape Town",
    "Basile": "Durban"
}
# print information about each contact
print("I have the following contacts:")
for name in contacts.keys():
    print("I have my frriend", name, "and their email address is", contacts[name], "and they live in", city[name])

