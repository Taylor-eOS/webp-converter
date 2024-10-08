import os
from PIL import Image, ImageEnhance
import time

# Converts all WEBP files in the directory to JPEG format and reduces saturation by 10%
directory = '~/Desktop'

def reduce_saturation(image, reduction_factor):
    enhancer = ImageEnhance.Color(image)
    return enhancer.enhance(1 - reduction_factor)

def convert_webp_to_jpeg(directory):
    directory = os.path.expanduser(directory)

    webp_directory = os.path.join(directory, "webp_files")
    if not os.path.exists(webp_directory):
        os.makedirs(webp_directory)

    for filename in os.listdir(directory):
        if filename.endswith(".webp"):
            file_path = os.path.join(directory, filename)
            new_filename = filename[:-4] + "jpeg"
            new_file_path = os.path.join(directory, new_filename)
            webp_filename = os.path.join(webp_directory, filename)
            os.rename(file_path, webp_filename)
            img = Image.open(webp_filename)
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            img = reduce_saturation(img, 0.15)
            img.save(new_file_path, 'JPEG', quality=95)
            print(f"Converted {filename} to JPEG and reduced saturation")
            time.sleep(0.2)
            #os.remove(webp_filename)
    print("Done")

# Specify the directory containing the WEBP files
convert_webp_to_jpeg(directory)
