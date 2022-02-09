from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", 'wb') as key_file:
        key_file.write(key)

## write_key()

def load_key():
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)

# functions



def view():
    with open("passwords.txt", 'r') as f:
        for lines in f.readlines():
            data = lines.rstrip()
            user, passw = data.split("|")
            print("User:", user, "password:", fer.decrypt(passw.encode()).decode() + "\n")

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

#Main loop
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to Quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. ")
        continue