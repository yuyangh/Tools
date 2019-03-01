import os
import json
from os import listdir, getcwd
from os.path import join


# classes = ["Person", "Car", "Bicycle", "Dog", "Other Vehicle"]


def convert(size, box, decimal_precision=6):
    """
    box form[x,y,w,h]
    :param size: a tuple(height, width)
    :param box:
    :param decimal_precision: round to how many decimals
    :return: a tuple (x, y, w, h)
    """
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = round(box[0] * dw, decimal_precision)
    y = round(box[1] * dh, decimal_precision)
    w = round(box[2] * dw, decimal_precision)
    h = round(box[3] * dh, decimal_precision)
    return (x, y, w, h)


def convert_json_annotation(JSON_path, txt_folder_path):
    with open(JSON_path, 'r') as f:
        data = json.load(f)
        item = data['image']
        # print(item)
        image_id = item['id']
        file_name = item['file_name']
        width = item['width']
        height = item['height']

        # write information into .txt
        with open(txt_folder_path + "/" + file_name + ".txt", "w") as file:
            for annotation in data['annotation']:
                category_id = annotation['category_id']
                bbox = annotation['bbox']
                yolo_format_info = convert((width, height), bbox)
                print(category_id, yolo_format_info[0], yolo_format_info[1], yolo_format_info[2], yolo_format_info[3],
                      file=file)


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


def convert_all(json_folder_path, txt_folder_path):
    """

    :param json_folder_path: folder that has all .json files
    :param txt_folder_path: folder that saves all converted .txt files
    :return:
    """
    path_names = get_file_addresses_in_dir(json_folder_path)
    for path in path_names:
        convert_json_annotation(path, txt_folder_path)


def testing():
    # local path
    # json_path = "/Users/yuyang/Downloads/FLIR_08862.json"
    # output_folder = "/Users/yuyang/Downloads"
    # convert_json_annotation(json_path, output_folder)
    pass


def main():
    json_folder_path = "/data/projects/FireSpotter/FLIR_ADAS/training/Annotations"
    txt_output_folder = "/data/projects/FireSpotter/FLIR_ADAS/training/Annotations_txt"
    convert_all(json_folder_path, txt_output_folder)


if __name__ == "__main__":
    main()
