from split_image import split_image
from PIL import Image
image_path = "AnimationSheet_Character.png"
rows = 9
cols = 8
im = Image.open(image_path)

im_width, im_height = im.size
split_image(image_path=image_path, rows=rows, cols=cols, should_square=False, should_cleanup=False, output_dir='./ngu')