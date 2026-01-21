import PIL.Image

# 1. 定义字符集：从"密集"到"稀疏"排列
# 你可以自己调整这个列表，比如用 '$' 替换 '@'
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resize_image(image, new_width=100):
    """
    调整图片大小。
    注意：因为终端的字符高度通常是宽度的2倍，所以我们在计算高度时乘以了 0.55 这个系数，
    用来抵消字符的'拉长'效果，防止图片变形。
    """
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def grayify(image):
    """将图片转换为灰度图 (Grayscale)"""
    return image.convert("L")


def pixels_to_ascii(image):
    """将每个像素值映射为对应的 ASCII 字符"""
    pixels = image.getdata()
    ascii_str = ""

    # 计算每个字符涵盖的灰度范围 (0-255)
    # 例如：256 / 11(字符数) ≈ 23
    bucket_size = 256 // len(ASCII_CHARS)

    for pixel in pixels:
        # pixel 是 0-255 的整数
        # 比如 pixel=255(白)，index 就是 255//23 = 11 (取最后一个字符 '.')
        # 比如 pixel=0(黑)，index 就是 0 (取第一个字符 '@')
        index = pixel // bucket_size

        # 防止 index 超出列表范围（极少数情况）
        if index >= len(ASCII_CHARS):
            index = len(ASCII_CHARS) - 1

        ascii_str += ASCII_CHARS[index]

    return ascii_str


def main():
    # 2. 获取用户输入的图片路径
    # path = input("请输入图片的路径 (例如: test.jpg): ")
    path = r"D:\DESKTOP\MyPythonStudy\ascii-art-python\assets\ascii-pineapple.jpg"
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "不是一个有效的图片路径，请检查拼写。")
        return

    # 3. 核心处理流程：Resize -> Grayscale -> ASCII Mapping
    new_width = image.size[1]  # 你可以调整这个宽度
    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    # 4. 格式化输出
    # 因为 pixels_to_ascii 返回的是一长串字符，我们需要每隔 new_width 个字符换行
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""

    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i + img_width] + "\n"

    # 5. 打印结果并保存到文件
    print(ascii_img)

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)
    print("转换完成！结果已保存到 ascii_image.txt")


if __name__ == "__main__":
    main()