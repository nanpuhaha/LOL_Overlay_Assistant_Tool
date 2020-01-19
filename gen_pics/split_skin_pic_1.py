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
    for i in range(3):
        for offset in numpy.random.randint(4, 65, 10):
            for height in get_array(center[1], offset):
                for width in get_array(center[0], offset):
                    cropImg = image[height:height + 2 * step_size,
                              width:width + 2 * step_size]  # height , width
                    cropImg = cv2.resize(cropImg, (64,64), interpolation=cv2.INTER_CUBIC)
                    cv2.imwrite(output_path + "\\" + str(index) + ".jpg", cropImg)
                    index += 1


# when you have a skin pic whose dimension is 980x500,
# you can use this method,
#
if __name__ == '__main__':
    # give me a dir path where saved a list of skin_pic
    root_path = "D:\\tft_skins_cost\\1"
    # give me a list of center point where you want to focus
    # center_point = [[637, 225], [552, 36], [675, 57], [333, 79],
    #                 [643, 98], [685, 68], [519, 191], [527, 120],
    #                 [523, 172], [526, 43], [715, 61], [479, 70],
    #                 [414, 133]]
    center_point = [[394, 103], [507, 110], [617, 205], [526, 64],
                    [523, 172], [582, 40], [343, 79], [479, 70],
                    [655, 64], [715, 64], [685, 68], [500, 181],
                    [643, 98]]
    # default step size = 64
    step_size = [128, 128, 128, 64,
                 72, 64, 64, 96,
                 72, 64, 64, 108,
                 64]
    # output dir setting

    for skin_pic_path, center, step in zip(os.listdir(root_path), center_point, step_size):
        output_path = root_path + "\\results"
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        print("pic -> ", root_path + "\\" + skin_pic_path)
        original_image = cv2.imread(root_path + "\\" + skin_pic_path)
        splitPic(original_image, center,
                 output_path + "\\" + skin_pic_path.split(".")[0], step)
