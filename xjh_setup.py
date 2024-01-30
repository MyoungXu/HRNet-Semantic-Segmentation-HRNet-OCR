import os

def find_matching_images(folder_a, folder_b, txt_file):
    # 获取文件夹 A 中的所有 PNG 图片
    png_files = [f for f in os.listdir(folder_a) if f.endswith('.png')]

    # 保存匹配的图片路径的列表
    matching_images_paths = []

    # 遍历每个 PNG 图片
    for png_file in png_files:
        # 构建文件名
        filename = os.path.splitext(png_file)[0]

        # 在文件夹 B 中查找同名的图片
        if os.path.exists(os.path.join(folder_b, filename + '.png')):
            matching_images_paths.append(os.path.join(folder_a, png_file))

    # 将匹配的图片路径写入指定的 txt 文件
    with open(txt_file, 'w') as file:
        for path in matching_images_paths:
            write_path = path[path.index('/') + 1:]
            another_path = write_path.replace('gtFine', 'leftImg8bit')
            file.write(another_path + '\t' + write_path + '\n')

def replace_backslash(file_path):
    with open(file_path, "r+") as file:
        text = file.read()  # 读取文本内容
        updated_text = text.replace("\\", "/")  # 使用字符串替换将 `\` 替换为 `/?`
        file.seek(0)  # 将文件指针移到开头
        file.write(updated_text)  # 将更新后的文本写入文件
        file.truncate()  # 截断文件内容，删除原始文本之后的部分


folder_a = 'data/cityscapes/gtFine/val'
folder_b = 'data/cityscapes/leftImg8bit/val'
txt_file = 'data/val.txt'

# 调用函数进行查找和写入路径
find_matching_images(folder_a, folder_b, txt_file)
replace_backslash(txt_file)
