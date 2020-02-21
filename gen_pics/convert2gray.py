import os
import cv2
import numpy as np

if __name__ == '__main__':
    root_path = "D:\\Projects\\CSCI_599\\build_dataset\\test_gray"
    for img_path in os.listdir(root_path):
        img = cv2.imread(root_path + "\\" + img_path)
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        cv2.imwrite(root_path + "\\" + img_path, img_gray)
