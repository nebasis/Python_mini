# stores and manages and encrypts the password. also decrypts them
from cryptography.fernet import Fernet  # module that allows to encrypt

'''
def write_key():
    key =Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


master_pwd = input("what is the master password? ")
key = load_key() + master_pwd.bytes
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            # strips the character turn from the file. doesnt addd a new line
            # print(line.rstrip())
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "Password: ", passw)


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
# if passwords.txt does not exist as a file then the append 'a' will create a new file
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:

    mode = input(
        "Would you like to add a new password or view existing ones (view,add)")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. ")
        continue
