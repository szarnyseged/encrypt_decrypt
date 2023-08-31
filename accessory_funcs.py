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


def check_for_readonly(file_path):
    # read-only files -> permission error. -> remove read-only then reset when encryption is done
    file_attributes = os.stat(file_path).st_file_attributes
    # binary & attrib 1 means -> read-only attribute true
    if file_attributes & 1:
        return True
    else:
        return False


def remove_readonly(file_path):
    os.system("attrib -r " + '"' + file_path + '"')


def add_readonly(file_path):
    os.system("attrib +r " + '"' + file_path + '"')
