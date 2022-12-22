broika=int(input())
register={}
for broi in range(broika):
    command=input().split()
    username = command[1]

    if command[0]=="register":
        license_plate_number = command[2]

        if username not in register:
            register[username]=license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        elif username in register.keys():
            print(f'ERROR: already registered with plate number {license_plate_number}')
    if command[0]=="unregister":
        if username not in register:
            print(f"ERROR: user {username} not found")
        elif username in register.keys():
            register.pop(username)
            print(f"{username} unregistered successfully")
for username,license_plate_number in register.items():
    print(f"{username} => {license_plate_number}")