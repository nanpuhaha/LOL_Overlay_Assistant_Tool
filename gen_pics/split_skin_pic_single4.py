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
    for i in range(2):
        for offset in numpy.random.randint(1, 32, 10):
            for height in get_array(center[1], offset):
                for width in get_array(center[0], offset):
                    cropImg = image[height:height + 2 * step_size,
                              width:width + 2 * step_size]  # height , width
                    cropImg = cv2.resize(cropImg, (64, 64), interpolation=cv2.INTER_CUBIC)
                    cv2.imwrite(output_path + "\\" + str(index) + ".jpg", cropImg)
                    index += 1


# when you have a skin pic whose dimension is 980x500,
# you can use this method,
#
if __name__ == '__main__':
    # give me a dir path where saved a list of skin_pic
    root_path = "D:\\LOL_DATA\\heroSkin2\\4"
    # give me a list of center point where you want to focus
    center_point = [

        [711, 130], [412, 70], [588, 88], [574, 49], [570, 67],
        [698, 52], [663, 61], [527, 133], [549, 162], [282, 129],
        [447, 184], [172, 54], [689, 242], [752, 118], [667, 42],

    ]
    # default step size = 64
    step_size = [
        # 生成图片范围大 缩小step_size
        40, 84, 45, 52, 50,
        40, 64, 108, 64, 40,
        50, 96, 50, 108, 96,

    ]
    # output dir setting

    for skin_pic_path, center, step in zip(os.listdir(root_path), center_point, step_size):
        output_path = root_path + "\\results"
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        print("pic -> ", root_path + "\\" + skin_pic_path)
        original_image = cv2.imread(root_path + "\\" + skin_pic_path)
        splitPic(original_image, center,
                 output_path + "\\" + skin_pic_path.split(".")[0], step)
