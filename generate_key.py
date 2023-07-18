from cryptography.fernet import Fernet


key = Fernet.generate_key()

question = input("generating a new key will overwrite current key.txt. proceed? (y/n) ")
if question == "y" or question == "Y":
    with open("./key.txt", "wb") as key_file:
        key_file.write(key)
    print("generation complete")
