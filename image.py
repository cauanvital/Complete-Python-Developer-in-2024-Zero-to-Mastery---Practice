import sys
import os
from PIL import Image

img_folder = sys.argv[1]
otp_folder = sys.argv[2]

if not os.path.exists(otp_folder):
    os.makedirs(f'./{img_folder}{otp_folder}', 'w')
