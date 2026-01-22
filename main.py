import PIL.Image

# 字符集
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def grayify(image):
    return image.convert("L")


def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    bucket_size = 256 // len(ASCII_CHARS)
    for pixel in pixels:
        index = pixel // bucket_size
        if index >= len(ASCII_CHARS):
            index = len(ASCII_CHARS) - 1
        ascii_str += ASCII_CHARS[index]
    return ascii_str


def save_as_html(ascii_art, filename="ascii_image.html"):
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                background-color: #000;
                color: #00ff00;
                text-align: center;
            }}
            pre {{
                font-family: "Courier New", "Consolas", monospace;
                font-size: 10px;
                line-height: 8px;
                font-weight: bold;
                white-space: pre;
            }}
        </style>
    </head>
    <body>
        <pre>{}</pre>
    </body>
    </html>
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_template.format(ascii_art))


def main():
    path = input("请输入图片的路径 (例如: ascii-pineapple.jpg): ")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "不是一个有效的图片路径。")
        return

    new_width = 100
    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""

    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i + img_width] + "\n"

    # 保存为 TXT
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)

    # 保存为 HTML (新功能!)
    save_as_html(ascii_img)

    print("转换完成！请打开 ascii_image.html 查看效果。")


if __name__ == "__main__":
    main()