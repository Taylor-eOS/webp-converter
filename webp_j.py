import os
from PIL import Image
import time

#Converts all WEBP files in the direcotry to PNG format
directory = '~/Desktop'

def convert_webp_to_png(directory):
    directory = os.path.expanduser(directory)

    #webp_directory = os.path.join(directory, "webp_files")
    #if not os.path.exists(webp_directory):
    #    os.makedirs(webp_directory)

    documents_directory = os.path.expanduser("~/Documents")
    webp_directory = os.path.join(documents_directory, "webp_files")
    if not os.path.exists(webp_directory):
        os.makedirs(webp_directory)
    desktop_directory = os.path.expanduser("~/Desktop")
    os.chdir(desktop_directory)

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
            img.save(new_file_path, 'JPEG', quality=95)
            print(f"Converted {filename} to JPEG")
            time.sleep(0.2)
            #os.remove(webp_filename)

# Specify the directory containing the WEBP files
convert_webp_to_png(directory)
