import json

phonebook = {
    "John": ("209 Trafalgar Road", "905-666-7777"),
    "Rosie": ("1439 Trafalgar Road", "487-423-7721"),
    "Alex": ("5 Main Street", "905-222-1234")
}

with open("Speeddial2.json", "w") as file:
    json.dump(phonebook, file, indent=4)

with open("Speeddial2.json", "r") as file:
    data = json.load(file)
    for name, value in data.items():
        print(name + ": " + value[0] + " - " + value[1])