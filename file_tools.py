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


if __name__ == "__main__":
    '''
    national="/Users/yuyanghuang/Downloads/Data/shopfront_counter_screenshot/From_National_Geographic_Magazine_screenshot_cropped/"
    citizenfour="/Users/yuyanghuang/Downloads/Data/shopfront_counter_screenshot/Citizenfour_screenshot/"
    so_sorry="/Users/yuyanghuang/Downloads/Data/shopfront_counter_screenshot/so_sorry_English_Subtitles_YouTube_screenshot/"
    office="/Users/yuyanghuang/Downloads/Data/shopfront_counter_screenshot/office_video_screenshot/"
    risk="/Users/yuyanghuang/Downloads/Data/shopfront_counter_screenshot/Risk_2016_screenshot/"
    new0 = "/Users/yuyanghuang/Downloads/Data/shopfront_orginal_file/test_data_20180719/0/"
    copy_files(national, new0, postfix="_national")
    copy_files(citizenfour, new0, postfix="_citizenfour")
    copy_files(so_sorry, new0, postfix="_so_sorry")
    copy_files(office, new0, postfix="_office")
    copy_files(risk, new0, postfix="_risk")
    '''
    '''
    shopfront="/Users/yuyanghuang/Downloads/Data/shopfront_picture/"
    new1 = "/Users/yuyanghuang/Downloads/Data/shopfront_orginal_file/test_data_20180719/1/"
    copy_files(shopfront, new1, postfix="_top100thousand")
    '''
    '''
    train_extra0="/Users/yuyanghuang/Downloads/Data/ILSVRC2013_DET_train_extra/ILSVRC2013_DET_train_extra0/"
    train_extra1 = "/Users/yuyanghuang/Downloads/Data/ILSVRC2013_DET_train_extra/ILSVRC2013_DET_train_extra1/"
    train_extra2 = "/Users/yuyanghuang/Downloads/Data/ILSVRC2013_DET_train_extra/ILSVRC2013_DET_train_extra2/"
    train_extra3 = "/Users/yuyanghuang/Downloads/Data/ILSVRC2013_DET_train_extra/ILSVRC2013_DET_train_extra3/"
    train_extra4 = "/Users/yuyanghuang/Downloads/Data/ILSVRC2013_DET_train_extra/ILSVRC2013_DET_train_extra4/"
    new0 = "/Users/yuyanghuang/Downloads/Data/shopfront_orginal_file/test_data_20180719/0/"
    copy_files(train_extra0, new0)
    copy_files(train_extra1, new0)
    copy_files(train_extra2, new0)
    copy_files(train_extra3, new0)
    copy_files(train_extra4, new0)
    '''
    '''
    path0="/Users/yuyanghuang/Downloads/Data/shopfront_orginal_file/test_tfdata_20180720/0/"
    path1="/Users/yuyanghuang/Downloads/Data/shopfront_orginal_file/test_tfdata_20180720/1/"
    pathLostInHongkong="/Users/yuyanghuang/Downloads/Data/shopfront_counter_screenshot/Lost_in_Hongkong_screenshot/"
    deleteNullFile(path1)
    copy_files(pathLostInHongkong,path0,select_random(pathLostInHongkong,300))
    '''


    # with open("/Users/yuyanghuang/PycharmProjects/TF/iip-ocr-header-classification/slim/temp.txt",mode="r") as f:
    #     download_files(f.readlines(),"/Users/yuyanghuang/Downloads/online_test/")

    # select_random(path0,3)

    # detectNullFile("/Users/yuyanghuang/Downloads/online_test")
    for file in os.listdir("/Users/yuyang/Downloads"):
        print(file)
    # originalDirectory = "/Users/yuyanghuang/PycharmProjects/MachineLearning/OCR_Project/data/门头定位-数据图片/"
    # newDirectory = "/Users/yuyanghuang/PycharmProjects/MachineLearning/OCR_Project/data/门头定位-数据图片 estimate对比不一致 原图/"
    # selectedFilesListPath = '/Users/yuyanghuang/PycharmProjects/MachineLearning/OCR_Project/data/differentEstimatedPicturePath.txt'
    # filesList = os.listdir(originalDirectory)
    # copyFilesListFile = open(selectedFilesListPath, mode="r", encoding='utf-8')
    # copyFilesList = copyFilesListFile.readlines()
    # copyFilesListFile.close()
