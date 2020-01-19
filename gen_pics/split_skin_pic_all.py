import os
import cv2
import numpy


def get_array(value, offset):
    low = value - offset if value - offset > 0 else 1
    high = value + offset
    return [low, value, high]


def splitPic(image, center, output_path, step_size=60):
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    index = 0
    for offset in numpy.random.randint(4, 65, 10):
        for height in get_array(center[1], offset):
            for width in get_array(center[0], offset):
                cropImg = image[height:height + 2 * step_size,
                          width:width + 2 * step_size]  # height , width
                cropImg = cv2.resize(cropImg, (128, 128), interpolation=cv2.INTER_CUBIC)
                cv2.imwrite(output_path + "\\" + str(index) + ".jpg", cropImg)
                index += 1


# when you have a skin pic whose dimension is 980x500,
# you can use this method,
#
if __name__ == '__main__':
    # give me a dir path where saved a list of skin_pic
    root_path = "D:\\tft_skins_cost2\\"
    # give me a list of center point where you want to focus
    center_point = [[414, 123], [517, 120], [637, 225], [526, 64],
                    [523, 172], [582, 40], [343, 79], [479, 70],
                    [675, 64], [715, 64], [685, 68], [519, 191],
                    [643, 98],
                    [709, 73], [418, 151], [453, 91], [892, 43],
                    [785, 161], [592, 231], [550, 108], [642, 172],
                    [521, 100], [419, 123], [906, 296], [577, 35],
                    [677, 75],
                    [581, 90], [715, 41], [588, 102], [643, 134],
                    [667, 87], [688, 96], [597, 81], [616, 133],
                    [569, 94], [577, 20], [406, 151], [880, 110],
                    [548, 113],
                    [690, 106], [879, 97], [720, 85], [778, 104],
                    [517, 140], [681, 195], [587, 247], [700, 115],
                    [517, 146], [460, 31],
                    [525, 116], [663, 139], [610, 172], [660, 103],
                    [740, 31], [520, 187],
                    [616, 60]
                    ]
    # default step size = 64
    step_size = [128, 128, 128, 64,
                 64, 64, 64, 96,
                 64, 64, 64, 128,
                 64,
                 64, 64, 64, 64,
                 128, 128, 96, 96,
                 64, 96, 64, 64,
                 64,
                 64, 32, 96, 64,
                 64, 64, 160, 128,
                 100, 96, 72, 64,
                 128,
                 96, 40, 72, 60,
                 64, 40, 64, 96,
                 96, 96,
                 130, 128, 72, 64,
                 64, 96,
                 64]
    # output dir setting

    for directory in os.listdir(root_path):
        for skin_pic_path, center, step in zip(os.listdir(root_path + "\\" + directory), center_point, step_size):
            output_path = root_path + "\\results"
            if not os.path.exists(output_path):
                os.mkdir(output_path)
            print("pic -> ", root_path + "\\" + directory + "\\" + skin_pic_path)
            original_image = cv2.imread(root_path + "\\" + directory + "\\" + skin_pic_path)
            splitPic(original_image, center,
                     output_path + "\\" + skin_pic_path.split(".")[0], step)
