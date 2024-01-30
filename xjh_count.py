from PIL import Image

# 打开彩色图像
image = Image.open(r"data/cityscapes/gtFine/val/09a_000002.png")

# 获取图像的颜色信息
colors = image.getcolors(image.size[0] * image.size[1])

# 输出颜色信息
for color in colors:
    print(color)
