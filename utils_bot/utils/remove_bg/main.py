from rembg import remove
from PIL import Image

inputPath = "img/bmw.jpg"
outputPath = "without_bg/img.png"

input = Image.open(inputPath)
output = remove(input)
output.save(outputPath)
