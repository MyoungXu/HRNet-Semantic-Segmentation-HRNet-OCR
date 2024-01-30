import glob
import os

from PIL import Image

def convert_pixel_value(image_path, output_path):
    # 打开图片
    image = Image.open(image_path)
    # 获取图片的像素矩阵
    pixels = image.load()

    # 定义像素值转换规则
    rules = {
        0: 7,
        1: 8,
        2: 11,
        3: 12,
        4: 13,
        5: 17,
        6: 19,
        7: 20,
        8: 21,
        9: 22,
        10: 23,
        11: 24,
        12: 25,
        13: 26,
        14: 27,
        15: 28,
        16: 31,
        17: 32,
        18: 33,
        255: 0
    }

    # 遍历每个像素点，根据规则进行转换
    for i in range(image.width):
        for j in range(image.height):
            pixel_value = pixels[i, j]
            if pixel_value in rules:
                pixels[i, j] = rules[pixel_value]

    # 保存转换后的图片
    xjh = os.path.basename(image_path)
    image.save(output_path+'/'+xjh)

folder_path = r"C:\Users\11093\Desktop\DSEC语义分割标签\zurich_city_09_e\labels"

# 获取指定文件夹中所有以"labelTrainIds.png"结尾的文件路径
file_paths = glob.glob(os.path.join(folder_path, "*labelTrainIds.png"))
output_path = r'C:\Users\11093\Desktop\label\9e'
# 执行功能A
for file_path in file_paths:
    convert_pixel_value(file_path, output_path)
