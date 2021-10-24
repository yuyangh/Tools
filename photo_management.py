import os
import time
import datetime
import queue
import shutil
import re

ROOT_DIRECTORY = ""
DESTINATION = ""
# only select files within TIME_LIMIT
TIME_LIMIT = 3600 * 24 * 365
CURRENT_TIME = time.time()
SPECIAL_WORD = "py"

"""
copy jpeg pictures in folders with specific ending to another folder, 
if exist, not override

steps:
get all pictures' path in folders with criteria e.g. time, name
get pictures' folder name
create all picture's corresponding folder in destination folder if not exist
copy picture from original folder to desitnation folder
 
"""


class TypeError(Exception):
    pass


def within_time_limit(time, time_limit=TIME_LIMIT):
    return (CURRENT_TIME - time) < time_limit


def bfs(directory):
    folders = queue.Queue()
    folders.put(directory)
    documents = list()

    while not folders.empty():
        folder = folders.get()

        if os.path.exists(folder):
            if within_time_limit(os.path.getmtime(folder)):
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        # print(root)
                        # print(file)
                        if SPECIAL_WORD in file:
                            absolute_addr = os.path.join(root, file)
                            if within_time_limit(os.path.getmtime(absolute_addr)):
                                # todo change into a tuple, which is file_addr, new_name
                                documents.append(absolute_addr)
                    for dir in dirs:
                        absolute_addr = os.path.join(root, dir)
                        if within_time_limit(os.path.getmtime(absolute_addr)):
                            folders.put(absolute_addr)
    print(documents)
    return documents


def copy_files(old_directory, new_directory, fileList=None, postfix=""):
    """
    :param old_directory: original directory
    :param new_directory: new directory
    :param fileList: a list of relative file path in old_directory to copy
    :param postfix: postfix for the new file
    :return: none
    """
    if fileList == None:
        fileList = os.listdir(old_directory)
    count = 0
    for i in fileList:
        aa, bb = i.split(".")
        oldname = old_directory + aa + "." + bb
        newname = new_directory + aa + postfix + "." + bb
        # print(oldname, newname)
        count += 1
        if (len(newname) > 0 and "." == newname[0]):
            continue
        # shutil.copyfile(oldname, newname)


def rename_files(directory, prefix_ignored_regex="^\d{4}.", include_subdirectory=True,
                 suffix_matching_regex="augmented", verbose=False):
    folders = queue.Queue()
    folders.put(directory)

    while not folders.empty():
        folder = folders.get()

        if os.path.exists(folder):
            for root, dirs, files in os.walk(folder):

                count = 0
                for file in files:
                    # print(file)

                    # ignore hidden files
                    if file.startswith('.'):
                        continue
                    # ignore specific regex
                    if re.search(prefix_ignored_regex, file) is not None:
                        continue

                    # regex search successfully
                    if re.search(suffix_matching_regex, file) is not None:
                        absolute_addr = os.path.join(root, file)
                        new_absolute_addr = os.path.join(root, os.path.basename(root) + " " + file)
                        if verbose:
                            print()
                            print("prev file address:", absolute_addr)
                            print("curr file address:", new_absolute_addr)
                        os.rename(absolute_addr, new_absolute_addr)
                        count += 1

                print(count, "replaced in folder:", root)

                # child folders
                if include_subdirectory:
                    for dir in dirs:
                        absolute_addr = os.path.join(root, dir)
                        folders.put(absolute_addr)
    pass


def test_rename_files():
    directory = "/Volumes/Yuyang/Photography temp"
    rename_files(directory, prefix_ignored_regex="^\d{4}.", include_subdirectory=True,
                 suffix_matching_regex="augmented")


def main():
    '''
    BFS from the directory
        if the directory's modification date is within 1 year (parameter),
            move the directory to the queue
            check its sub directory
    go through items (non folders) in the queue,
    copy specific items to destination address

    :return:
    '''
    files = bfs("/Users/yuyang/PycharmProjects/Tools")

    # if (len(os.sys.argv) < 1):
    #     raise TypeError()
    # else:
    #     print("os.sys.argv[0]: %s" % os.sys.argv[0])
    #     # os.sys.argv[0] is the current file, in this case, file_ctime.py
    # f = os.sys.argv[0]
    # mtime = time.ctime(os.path.getmtime(f))
    # ctime = time.ctime(os.path.getctime(f))
    # print("Last modified : %s, last created time: %s" % (mtime, ctime))


if __name__ == '__main__':
    test_rename_files()
