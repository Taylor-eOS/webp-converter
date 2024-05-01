import os
from PIL import Image

#Converts all WEBP files in the direcotry to PNG format
directory = '~/Desktop'

def convert_webp_to_png(directory):
    # Expand the user's home directory
    directory = os.path.expanduser(directory)

    webp_directory = os.path.join(directory, "webp_files")
    if not os.path.exists(webp_directory):
        os.makedirs(webp_directory)

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".webp"):
            # Construct full file path
            file_path = os.path.join(directory, filename)
            # Open the WEBP file with Pillow
            img = Image.open(file_path)
            #print(f"Convert {filename}")
            if img.mode == 'RGBA':
                rgb_img = img.convert('RGB')  # Convert to RGB, dropping the alpha channel
                new_filename = filename[:-4] + "jpg"
                new_file_path = os.path.join(directory, new_filename)
                rgb_img.save(new_file_path, 'JPEG', quality=95)
            else:
                new_filename = filename[:-4] + "jpg"
                new_file_path = os.path.join(directory, new_filename)
                img.save(new_file_path, 'JPEG', quality=95)
            print(f"Converted {filename} to JPEG")
            #os.remove(file_path)
            os.rename(file_path, os.path.join(webp_directory, filename))

# Specify the directory containing the WEBP files
convert_webp_to_png(directory)
