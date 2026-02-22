import os
from PIL import Image

directory = '~/Desktop'

def convert_webp_to_png(directory):
    directory = os.path.expanduser(directory)
    for filename in os.listdir(directory):
        if filename.endswith(".webp"):
            file_path = os.path.join(directory, filename)
            img = Image.open(file_path)
            new_filename = filename[:-4] + "png"
            new_file_path = os.path.join(directory, new_filename)
            #img.save(new_file_path, 'PNG')
            img.save(new_file_path, 'PNG', compress_level=7, optimize=True)
            #img.save(new_file_path[:-3] + "jpeg", 'JPEG', quality=95)
            print(f"Converted {filename}")

convert_webp_to_png(directory)
