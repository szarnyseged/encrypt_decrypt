import os
from cryptography.fernet import Fernet
import accessory_funcs


def input_key():
    """
    ask for user to input his key
    """
    pass


def load_key():
    try:
        with open("./key.txt", "rb") as key_file:
            cipher = key_file.read()
        key = Fernet(cipher)
        print(f"key loaded")
        return key
    except:
        raise Exception("error. maybe create a key first?")


def encrypt_one(file_path):
    # hidden files -> permission error. -> remove hidden then reset when encryption is done
    if accessory_funcs.check_for_hidden(file_path):
        accessory_funcs.remove_hidden(file_path)
        was_hidden = True
    else:
        was_hidden = False

    with open(file_path, "rb") as one_file:
        datas = one_file.read()
        encrypted = key.encrypt(datas)
    with open(file_path, "wb") as one_file:
        one_file.write(encrypted)
    
    if was_hidden:
        accessory_funcs.add_hidden(file_path)


def decrypt_one(file_path):
    # hidden files -> permission error. -> remove hidden then reset when decryption is done
    if accessory_funcs.check_for_hidden(file_path):
        accessory_funcs.remove_hidden(file_path)
        was_hidden = True
    else:
        was_hidden = False
    
    with open(file_path, "rb") as one_file:
        encrypted = one_file.read()
        decrypted = key.decrypt(encrypted)
    with open(file_path, "wb") as one_file:
        one_file.write(decrypted)

    if was_hidden:
        accessory_funcs.add_hidden(file_path)


def encrypt_all(target_dir):
    """
    iterate trough the target_dir and encrypt files.
    """
    for root, dirnames, filenames in os.walk(target_dir):
        for file in filenames:
            file_path = os.path.join(root, file)
            encrypt_one(file_path)
            print(f"encrypted: {file_path}")
    print("encryption complete")


def decrypt_all(target_dir):
    """
    iterate trough the target_dir and decrypt files.
    """
    for root, dirnames, filenames in os.walk(target_dir):
        for file in filenames:
            file_path = os.path.join(root, file)
            decrypt_one(file_path)
            print(f"decrypted: {file_path}")
    print("decryption complete")


def choose_target():
    target = input("choose target dir to encrypt/decrypt ")
    dir_struckture = list(os.walk(target))
    if len(dir_struckture) < 1:
        raise ValueError("no files found")
    for elem in dir_struckture:
        print(elem)
    print("")
    proceed = input("proceed? (y/n) ")
    if proceed == "y" or proceed == "Y":
        return target


key = load_key()
target = choose_target()
if target != None:
    print("encrypt or decrypt? \n",
          "1 = encrypt \n",
          "2 = decrypt")
    enc_or_dec = input()
    if enc_or_dec == "1":
        encrypt_all(target)
    elif enc_or_dec == "2":
        decrypt_all(target)
