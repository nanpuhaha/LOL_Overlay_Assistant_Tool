import json
import os
import shutil
import cv2


def is_contains_chinese(strs):
    return any('\u4e00' <= _char <= '\u9fa5' for _char in strs)


def copy300times(dir, imgs):
    for i in range(450, 700):
        destination = dir + "\\" + str(i) + ".jpg"
        shutil.copy(imgs, destination)


if __name__ == '__main__':

    root_path = "D:\\Projects\\League-X\\champs"
    for directory in os.listdir(root_path):
        for imgs in os.listdir(root_path + "\\" + directory):
            img = cv2.imread(root_path + "\\" + directory + "\\" + imgs)
            try:
                img_new = cv2.resize(img, (24,24), interpolation=cv2.INTER_CUBIC)
                cv2.imwrite(filename=root_path + "\\" + directory + "\\" + imgs,
                        img=img_new)
            except:
                print("wrong ", directory)
        print("finish dir ", directory)