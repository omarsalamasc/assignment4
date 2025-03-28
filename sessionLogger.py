class IPException(Exception):
    pass

def validate_ip(ip):
    for ch in ip:
        if not (ch.isdigit() or ch == "."):
            raise IPException("Invalid character in IP: " + ch)

credentials = []

while True:
    try:
        username = input("Enter username (or 'q' to quit): ")
        if username.lower() == "q":
            break
        password = input("Enter password: ")
        ip = input("Enter IP: ")

        validate_ip(ip)

        credentials.append([username, password, ip])
    except IPException as e:
        print("Error: " + str(e))

with open("SessionLogger.txt", "w") as file:
    for entry in credentials:
        file.write(str(entry) + "\n\n")  # Added an extra \n for spacing between entries