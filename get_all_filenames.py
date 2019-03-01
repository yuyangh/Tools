import os


def get_file_addresses_in_dir(file_dir):
    """
    get files' absolute address in this directory
    :param file_dir: folder address
    :return: a list of absolute file address in the folder
    """
    file_address_in_file_dir = list()
    for root, dirs_under_root, file_list in os.walk(file_dir):
        print(root)
        # print("current path's dir:",end="")
        # print(dirs_under_root)  # in list format
        # print(file_list)  # in list format
        for file_name in file_list:
            # print(root+"/"+file_name)
            file_address_in_file_dir.append(root + "/" + file_name)
    return file_address_in_file_dir


def write_list_to_file(file_name, lists):
    """
    write each element of the list into the file per line
    :param file_name: open this file to write
    :param lists: a list of data
    :return:
    """
    with open(file_name, "w")as file:
        for line in lists:
            file.write(line + "\n")


def test():
    list = get_file_addresses_in_dir(os.getcwd())
    write_list_to_file("/Users/yuyang/PycharmProjects/Tools/test.txt", list)


def main():
    txt_file_address = "/data/projects/FireSpotter/FLIR_ADAS/training/Annotations_txt"
    file_address_list = get_file_addresses_in_dir(txt_file_address)
    write_list_to_file("/Users/yuyang/PycharmProjects/Tools/test.txt", file_address_list)


if __name__ == "__main__":
    main()
