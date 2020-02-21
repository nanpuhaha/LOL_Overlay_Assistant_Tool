import json
import os
import shutil
import cv2

if __name__ == '__main__':

    root_path = "D:\\Projects\\League-of-Legends-Assitant-Tool\\PoroApp\\resources\\assets"
    for directory in os.listdir(root_path):
        for imgs in os.listdir(root_path + "\\" + directory):
            img = cv2.imread(root_path + "\\" + directory + "\\" + imgs, cv2.IMREAD_UNCHANGED)
            img_new = cv2.resize(img, (128, 128), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(filename=root_path + "\\" + directory + "\\" + imgs,
                        img=img_new)
