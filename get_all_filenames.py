import os
import random
import json

def get_file_addresses_in_dir(file_dir):
    file_address_in_file_dir = list()
    for root, dirs, file_list in os.walk(file_dir):
        for file_name in file_list:
            # print(root+"/"+file_name)
            file_address_in_file_dir.append(root + "/" + file_name)
    return file_address_in_file_dir


def write_list_to_file(file_address, list):
    with open(file_address, "w")as file:
        for line in list:
            file.write(line+"\n")

def test():
    list=get_file_addresses_in_dir(os.getcwd())
    write_list_to_file("/Users/yuyang/PycharmProjects/Tools/test.txt", list)

def main():
    txt_file_address = "/data/projects/FireSpotter/FLIR_ADAS/training/Annotations_txt"
    file_address_list = get_file_addresses_in_dir(txt_file_address)
    write_list_to_file("/Users/yuyang/PycharmProjects/Tools/test.txt", file_address_list)

if __name__ == "__main__":
    main()