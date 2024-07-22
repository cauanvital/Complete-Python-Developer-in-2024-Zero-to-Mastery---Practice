import sys
import os
from PIL import Image

img_folder = sys.argv[1]
otp_folder = sys.argv[2]

if not os.path.exists(otp_folder):
    os.makedirs(otp_folder)
    
for f in os.listdir(img_folder):
    f_name = os.path.splitext(f)[0]
    
    img = Image.open(f'./{img_folder + f}')
    img.save(f'./{otp_folder + f_name}.png', 'png')
