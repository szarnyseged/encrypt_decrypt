import os


def check_for_hidden(file_path):
    # hidden files -> permission error. -> remove hidden then reset when encryption is done
    file_attributes = os.stat(file_path).st_file_attributes
    # print(file_attributes)
    # binary & attrib 2 means -> hidden attribute true.
    if file_attributes & 2:
        return True
    else:
        return False


# os.system path can't contain spaces -> leads to error
# solution: putting quotes around the path.
# https://stackoverflow.com/questions/6977215/os-system-to-invoke-an-exe-which-lies-in-a-dir-whose-name-contains-whitespace
def remove_hidden(file_path):
    os.system("attrib -h " + '"' + file_path + '"')


def add_hidden(file_path):
    os.system("attrib +h " + '"' + file_path + '"')
