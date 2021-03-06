import numpy as np
import cv2
import os


def gray2color_image(image_address, save_folder=None, write=False):
    # use grey mode to read image
    src = cv2.imread(image_address, 0)
    # use ctvcolor() to convert
    src_RGB = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

    # display picture
    # cv2.imshow("input", src)
    # cv2.imshow("output", src_RGB)

    image_folder = os.path.dirname(image_address)

    if save_folder is not None:
        image_folder = save_folder

    if write:
        newfile_path = os.path.join(image_folder, os.path.split(os.path.abspath(image_address))[1])
        # print(newfile_path)
        cv2.imwrite(newfile_path, src_RGB)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def get_file_new_name(file_path, postfix=""):
    """
    copy and rename single file
    :param file_path:
    :param postfix:
    :return: new file name
    """
    folder_address = os.path.dirname(file_path)
    file_name, file_extend = os.path.splitext(file_path)
    new_name = file_name + postfix + file_extend
    newfile_path = os.path.join(folder_address, new_name)
    return newfile_path


def get_file_addresses_in_dir(file_dir):
    file_address_in_file_dir = list()
    for root, dirs, file_list in os.walk(file_dir):
        # print("current path:",end="")
        print(root)  # current path
        for file_name in file_list:
            # print(root + "/" + file_name)
            file_address_in_file_dir.append(root + "/" + file_name)
    return file_address_in_file_dir


def process_image(source_folder, destination_folder):
    file_list = get_file_addresses_in_dir(source_folder)
    for file_obj in file_list:
        # print(file_obj)
        gray2color_image(file_obj, destination_folder, True)


def test():
    image_address = "/Users/yuyang/OneDrive/USC/Research/FLIR_08863.jpeg"
    image_address1 = ""
    gray2color_image(image_address, "/Users/yuyang/Desktop/", True)


def main():
    # test()
    source_folder = "/Volumes/Temp/FLIR_ADAS/training/PreviewData"
    destination_folder = "/Users/yuyang/Desktop/JPEGImages"
    process_image(source_folder, destination_folder)


if __name__ == "__main__":
    main()
