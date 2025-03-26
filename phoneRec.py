phonebook = {
    "John": ("209 Trafalgar Road", "905-666-7777"),
    "Rosie": ("1439 Trafalgar Road", "487-423-7721"),
    "Alex": ("5 Main Street", "905-222-1234")
}

with open("SpeedDial1.txt", "w") as file:
    for info in phonebook.values():
        file.write(info[1] + "\n")
