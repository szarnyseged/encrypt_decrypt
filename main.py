import os
from cryptography.fernet import Fernet
import accessory_funcs


def load_key():
    try:
        with open("./key.pem", "r") as key_file:
            key = key_file.read()
        print(f"key loaded")
        return key
    except:
        print("error. maybe create a key first?")


def encrypt_one(file_path):
    # hidden files -> permission error. -> remove hidden then reset when encryption is done
    if accessory_funcs.check_for_hidden(file_path):
        accessory_funcs.remove_hidden(file_path)
        was_hidden = True
    else:
        was_hidden = False

    with open(file_path, "rb") as one_file:
        datas = one_file.read()
        encrypted = Fernet(key).encrypt(datas)
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
        decrypted = Fernet(key).decrypt(encrypted)
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
    dir_struckture = os.walk(target)
    for elem in dir_struckture:
        print(elem)
    print("")
    proceed = input("proceed? (y/n) ")
    if proceed == "y" or proceed == "Y":
        return target


key = load_key()
target = choose_target()
if target != None:
    enc_or_dec = input("encrypt or decrypt? ")
    if enc_or_dec == "encrypt":
        encrypt_all(target)
    elif enc_or_dec == "decrypt":
        decrypt_all(target)
