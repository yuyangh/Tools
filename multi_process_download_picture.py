from multiprocessing import Pool
import requests
import os
import time
import datetime

_FILEPATH="/Users/yuyanghuang/Downloads/Data/shopfront_picture/"

def download(url):
    r = requests.get(url)
    filename = url.split("/")[-1]
    end = filename.find(".jpg")
    open(_FILEPATH + filename[:end] + '.jpg', 'wb').write(r.content)

def download_quick(info):
    compress_code = "%40100w_300h_1e_1l%7Cwatermark%3D0"
    r = requests.get(info[1]+compress_code)
    # filename = url.split("/")[-1]
    # end = filename.find(".jpg")
    open(_FILEPATH+info[0]+ '.jpg', 'wb').write(r.content)
    # open('data/300x600/' + filename[:end] + '.jpg', 'wb').write(r.content)

if __name__ == '__main__':
    urls=[]
    info = []
    i = 91000
    p = Pool(20)

    if not os.path.exists('/Users/yuyanghuang/Downloads/Data/shopfront_picture'):
        os.makedirs('/Users/yuyanghuang/Downloads/Data/shopfront_picture')

    with open('/Users/yuyanghuang/Downloads/Data/shopfront_list.txt', 'r') as f:
        for line in f.readlines()[91001:]:
            # print(line.split("\t"))
            i += 1
            if i > 100000:
                break
            # urls.append(line.split("\t")[2])
            # print(tuple(line.strip().split("\t")[:2]))
            info.append(tuple(line.strip().split("\t")[:2]))
            # Download every 100
            if i % 1000 == 0:
                print(i,end="\t")
                print(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))
                # p.map(download, urls)
                p.map(download_quick,info)
                urls = []
                time.sleep(1)

    # with Pool(5) as p:
    # p = Pool(20)
    # print(p.map(download, urls))
