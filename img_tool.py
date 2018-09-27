from PIL import Image
import os.path
import sys
import math

ALLOWED_EXTENSIONS = set(['jpg', 'JPG', 'jpeg', 'JPEG', 'png'])

def create_folder(name,path=os.getcwd(),absolute_file_path=False):
    '''
    :param name: folder's name
    :param path: directory to create the folder
    :return: absolute path of the save folder
    '''
    save_path = (path[:-1] if path[-1] == '/' else path) + name
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    if absolute_file_path:
        return os.getcwd()+"/"+save_path
    else:
        return save_path

def browse_img_info(path=os.getcwd()):
    count=0
    for root, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            try:
                img = Image.open(fp)
                w, h = img.size
                # print("The size of the image is ", w, "*", h, os.path.join(root, f))
            except:
                print(os.path.join(root, f))
                count+=1
    if count!=0:
        print(str(count)+" images are broken")
    else:
        print("all images are good")



def crop_center_box(side_length=224, path=os.getcwd()):
    '''
    :param side_length: the side length of the cropped center square region counted in pixel
    :param path: path to the image
    :return: none
    '''
    small_path = (path[:-1] if path[-1] == '/' else path) + '_small'
    if not os.path.exists(small_path):
        os.mkdir(small_path)
    for root, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            img = Image.open(fp)
            w, h = img.size
            ratio = min(w, h) / side_length
            # resize to one side equals side_length
            compressed_img = img.resize((round(w / ratio), round(h / ratio)))
            w, h = round(w / ratio), round(h / ratio)
            region = compressed_img.crop(
                ((w - side_length) / 2, (h - side_length) / 2, (w + side_length) / 2, (h + side_length) / 2))
            region.save(os.path.join(small_path, f), "jpeg")
            print(fp)
            print("The size of the image is ", img.size, "cropped and compressed to\t", str(region.size))


def crop_middle_box(top_dist, bottom_dist, path=os.getcwd()):
    '''
    :param top_dist: top bar which will be cropped
    :param bottom_dist: bottom bar which will be cropped
    :param path: file path
    :return: none
    '''
    count=0
    middle_path=create_folder("_middle",path)
    for root, dirs, files in os.walk(path):
        for f in files:
            if round(100*count/len(files))%5==0:
                print(str(round(100*count/len(files)))+"%\t",end="")
            fp = os.path.join(root, f)
            img = Image.open(fp)
            w, h = img.size
            region = img.crop(
                (0, top_dist, w, h - bottom_dist))
            region.save(os.path.join(middle_path, f), "jpeg")
            # print(fp)
            # print("The size of the image is ", img.size, "cropped to\t", str(region.size))
            count+=1

def compress(ratio,path=os.getcwd()):
    '''
    :param ratio: new size = orginal size / ratio
    :param path: folder path of images
    :return: none
    '''
    save_path=create_folder("_compress",path)
    count=0
    for root, dirs, files in os.walk(path):
        for f in files:
            if round(100*count/len(files))%5==0:
                print(str(round(100*count/len(files)))+"%\t",end="")
            fp = os.path.join(root, f)
            if fp.split(".")[-1] not in ALLOWED_EXTENSIONS:
                print(fp,"\t","is not image file")
            img = Image.open(fp)
            w, h = img.size
            region=img.resize((round(w / ratio), round(h / ratio)))
            region.save(os.path.join(save_path, f))
            # print(fp)
            # print(os.path.join(save_path, f))
            count+=1


if __name__ == "__main__":
    # path1 = "/Users/yuyanghuang/Desktop/test_middle"
    # path2 = "/Users/yuyanghuang/Desktop/test"
    # path3="/Users/yuyanghuang/Desktop/"
    # path4="/Users/yuyanghuang/Downloads/Data/shopfront_orginal_file/train_data_20180719/1/"
    # browse_img_info(path4)

    compress(4,"/Users/yuyanghuang/Desktop/test")
    # browse_img_info(path=path1)
    # crop_center_box(path=path2)
    # crop_middle_box(35,70,path2) # parameter for From_National_Geographic_Magazine_screenshot
