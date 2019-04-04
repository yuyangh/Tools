# -*- coding: utf-8 -*-
# !/usr/bin/env python
# title           :
# description     :file tools
# author          :huangyuyang
# date            :2018/7/23
# version         :
# usage           :
# notes           :
# python_version  :3.6
# ==============================================================================
import os
import random
import json
import shutil
from sys import argv
import requests


def copy_files(old_directory, new_directory, fileList=None, postfix=""):
    '''
    :param old_directory: original directory
    :param new_directory: new directory
    :param fileList: a list of relative file path in old_directory to copy
    :param postfix: postfix for the new file
    :return: none
    '''
    if fileList == None:
        fileList = os.listdir(old_directory)
    count = 0
    for i in fileList:
        aa, bb = i.split(".")
        oldname = old_directory + aa + "." + bb
        newname = new_directory + aa + postfix + "." + bb
        # print(oldname, newname)
        count += 1
        if (count % (len(fileList) // 5) == 0):
            print(old_directory + " copy\t" + str(round(count / len(fileList) * 100, 3)) + "% completed")
        if (len(newname) > 0 and "." == newname[0]):
            continue
        shutil.copyfile(oldname, newname)


def detectNullFile(directory, delete=False):
    '''
    delete file which is empty
    :param directory: folder path
    :return: none
    '''
    print("Working in\t", directory)
    count = 0
    os.chdir(directory)
    '''delete all empty files'''
    files = os.listdir(os.getcwd())
    for file in files:
        if os.path.getsize(file) == 0:  # get file size
            if delete:
                os.remove(file)
            print(file + " detected.")
            count += 1
    print(count, "empty files detected/deleted")


def select_random(directory, num, absolute_file_path=False, seed=0):
    '''
    :param directory: 
    :param num: number of files to be selected
    :param seed: random seed
    :return: list of selected files
    '''
    random.seed(seed)
    filelist = os.listdir(directory)
    selected_files = random.sample(filelist, num)
    if (absolute_file_path):
        for index in range(len(selected_files)):
            selected_files[index] = directory + selected_files[index]
    # print(selected_files)
    return selected_files


def download_files(urllist, directory=os.getcwd() + "/"):
    '''
    :param urllist: list of url
    :param directory: directory to save download files
    :return: none
    '''
    compress_code = "%40100w_300h_1e_1l%7Cwatermark%3D0"
    count = 0
    for url in urllist:
        url = url.strip()
        r = requests.get(url + compress_code)
        filename = url.split("/")[-1]
        # end = filename.find(".jpg")
        open(directory + filename, 'wb').write(r.content)
        count += 1
        if (count % (len(urllist) // 5) == 0):
            print(str(round(count / len(urllist) * 100, 3)) + "% completed")


def merge_files(meragefiledir=None):
    # 获取目标文件夹的路径
    if meragefiledir == None:
        meragefiledir = os.getcwd()
    # 获取当前文件夹中的文件名称列表
    filenames = os.listdir(meragefiledir)
    # 打开当前目录下的result.txt文件，如果没有则创建
    file = open('result.txt', 'w')
    # 向文件中写入字符

    # 先遍历文件名
    for filename in filenames:
        filepath = meragefiledir + ''
        filepath = filepath + filename
        # 遍历单个文件，读取行数
        for line in open(filepath):
            file.writelines(line)
        file.write('\n')
    # 关闭文件
    file.close()


def get_file_addresses_in_dir(file_dir):
    file_address_in_file_dir = list()
    for root, dirs, file_list in os.walk(file_dir):
        # print("current path:",end="")
        print(root)  # 当前目录路径
        # print("current path's dir:",end="")
        # print(dirs)  # 当前路径下所有子目录, in list format
        # print(file_list)  # 当前路径下所有非目录子文件, in list format
        for file_name in file_list:
            # print(root+"/"+file_name)
            file_address_in_file_dir.append(root + "/" + file_name)
    return file_address_in_file_dir


def write_list_to_file(file_address, list):
    with open(file_address, "w")as file:
        for line in list:
            file.write(line + "\n")


def copy_rename_files(source_folder, postfix=""):
    """
    copy file and rename
    将某个目录下的文件修改文件名后复制到相同的文件夹
    """

    file_list = os.listdir(source_folder)
    for file_obj in file_list:
        file_path = os.path.join(source_folder, file_obj)

        file_name, file_extend = os.path.splitext(file_obj)
        new_name = file_name + postfix + file_extend

        newfile_path = os.path.join(source_folder, new_name)

        shutil.copyfile(file_path, newfile_path)


def copy_rename_file(file_path, postfix=""):
    """
    copy and rename single file
    :param file_path:
    :param postfix:
    :return: none
    """

    folder_address = os.path.dirname(file_path)
    file_name, file_extend = os.path.splitext(file_path)
    new_name = file_name + postfix + file_extend

    newfile_path = os.path.join(folder_address, new_name)

    shutil.copyfile(file_path, newfile_path)


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


if __name__ == "__main__":
    get_file_addresses_in_dir(os.getcwd())
    write_list_to_file("/Users/yuyang/PycharmProjects/Tools/test.txt", ["aefbn", "abe"])
