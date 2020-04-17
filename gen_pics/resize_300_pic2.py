import json
import os
import shutil
import cv2

if __name__ == '__main__':

    root_path = "D:\\Projects\\League-of-Legends-Assitant-Tool\\PoroApp\\resources\\data\\profile_big"
    for imgs in os.listdir(root_path):
        img = cv2.imread(root_path + "\\" + imgs, cv2.IMREAD_UNCHANGED)
        img_new = cv2.resize(img, (24, 24), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(filename=root_path + "\\" + imgs,
                    img=img_new)
