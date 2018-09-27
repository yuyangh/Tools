import json
import sys
import os
import cv2
import requests
from multiprocessing import Pool
import requests
import os
import time
sys.path.append("../")
from OCR_Project.Utilities.check_webpage_existence import check_webpage_existence

def download(url,filePath,name):
    # compress the image size
    compress_code = "%40100w_300h_1e_1l%7Cwatermark%3D0"
    if not check_webpage_existence(url):
        with open("/Users/yuyanghuang/Downloads/Data/shopfront_error_list.txt", mode="a") as shopfront_error_list_writer:
            shopfront_error_list_writer.write(name+"\t"+url[:len(url)-len(compress_code)]+"\n")
            print(str(count) + "th picture cannot be opened. ID: " + name + " url: " + url)
        return
    cap = cv2.VideoCapture(url)
    ret = cap.isOpened()
    while (ret):
        ret, img = cap.read()
        if cv2.waitKey(10) >= -10:
            # print(filePath+name+".jpg")
            # filePath[:len(filePath)-4] is for 3 digits file extension name

            cv2.imwrite(filePath+name+".jpg", img)
            cv2.destroyAllWindows()
            break

def download_quick(url,filePath,name):
    compress_code = "%40100w_300h_1e_1l%7Cwatermark%3D0"
    r = requests.get(url+compress_code)
    # filename = url.split("/")[-1]
    # end = filename.find(".jpg")
    open(filePath+name+ '.jpg', 'wb').write(r.content)
    # open('data/300x600/' + filename[:end] + '.jpg', 'wb').write(r.content)

if __name__ == "__main__":
    urls=[]
    p = Pool(20)
    filePath = "/Users/yuyanghuang/Downloads/Data/shopfront_pic/"
    compress_code = "%40100w_300h_1e_1l%7Cwatermark%3D0"
    count=0+18516
    with open("/Users/yuyanghuang/Downloads/Data/shopfront_list.txt", mode="r") as shopfront_list_reader:
        shopfront_list=shopfront_list_reader.readlines()
        with open("/Users/yuyanghuang/Downloads/Data/shopfront_selected_list.txt", mode="r") as shopfront_selected_list_reader:
            shopfront_selected_list=shopfront_selected_list_reader.readlines()
            for shopfront_selected in shopfront_selected_list[1+18516:]:
                # print(shopfront_list[int(shopfront_selected.strip())].strip().split("\t"))
                name,url=shopfront_list[int(shopfront_selected.strip())].strip().split("\t")[:2]
                download_quick(url+compress_code,filePath,name)
                # if count%5==0:
                print(str(count)+"th picture")
                count+=1

    # test
    # url="http://p0.meituan.net/mogu/373c71d08b9cbb5660eb7f3e47762bad1392547.jpg"
    # name="1"
    # print(str(len(compress_code)))
    # url+=(compress_code)
    # download(url,filePath,name)
    pass
