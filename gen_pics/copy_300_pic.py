import json
import os
import shutil


def is_contains_chinese(strs):
    return any('\u4e00' <= _char <= '\u9fa5' for _char in strs)


def copy300times(dir, imgs):
    for i in range(450, 700):
        destination = dir + "\\" + str(i) + ".jpg"
        shutil.copy(imgs, destination)


if __name__ == '__main__':

    root_path = "D:\\LOL_DATA\\avatar_en"
    for directory in os.listdir(root_path):
        for imgs in os.listdir(root_path + "\\" + directory):
            copy300times(root_path + "\\" + directory,
                         root_path + "\\" + directory + "\\" + imgs)
