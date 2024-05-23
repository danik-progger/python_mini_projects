from PIL import Image


def compressMe(file_path, quality=30, compressed_path="./compressed_images"):
    file_name = file_path.split("/")[-1]
    picture = Image.open(file_path)

    picture.save(compressed_path + "/" + file_name,
                 "JPEG", optimize=True, quality=quality)

compressMe("./img/lake.jpg")
compressMe("./img/kobe.jpg")
compressMe("./img/bmw.jpg")
