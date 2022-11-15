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
    for _ in range(2):
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
    root_path = "D:\\LOL_DATA\\heroSkin2\\5"
    # give me a list of center point where you want to focus
    center_point = [

        [534, 116], [600, 90], [575, 89], [699, 24], [622, 75],
        [687, 197], [645, 171], [540, 117], [260, 272], [552, 90],
        [521, 173], [720, 127], [675, 132], [453, 51], [893, 167],
        [748, 101], [619, 89], [593, 63], [775, 165], [731, 61],

    ]
    # default step size = 64
    step_size = [
        # 生成图片范围大 缩小step_size
        160, 45, 45, 45, 40,
        40, 64, 50, 64, 72,
        84, 64, 50, 96, 40,
        45, 60, 110, 140, 38,

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
