import json
import os


def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False


if __name__ == '__main__':
    json_file_path = "D:\\TFT_DATA\\champions.json"
    rename_info = dict()
    with open(json_file_path, encoding="utf8") as json_file:
        champs = json.load(json_file)
        for champion in champs:
            rename_info[champion['cn_name']] = champion['champion']

    print(rename_info)
    root_path = "D:\\tft_skins_cost"
    for directory in os.listdir(root_path):
        for imgs in os.listdir(root_path + "\\" + directory):
            if is_contains_chinese(imgs):
                # print("original -> ", root_path + "\\" + directory + "\\" + imgs)
                # print("new -> ", root_path + "\\" + directory + "\\" + rename_info[imgs.split(".")[0][:-2]] + ".jpg")
                os.rename(root_path + "\\" + directory + "\\" + imgs,
                          root_path + "\\" + directory + "\\" + rename_info[imgs.split(".")[0][:-2]] + ".jpg")
