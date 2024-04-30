import os
from PIL import Image

#Converts all WEBP files in the direcotry to PNG format
directory = '~/Desktop'

def convert_webp_to_png(directory):
    # Expand the user's home directory
    directory = os.path.expanduser(directory)

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".webp"):
            # Construct full file path
            file_path = os.path.join(directory, filename)
            # Open the WEBP file with Pillow
            img = Image.open(file_path)
            # Define the new filename with the PNG extension
            new_filename = filename[:-5] + ".png"
            new_file_path = os.path.join(directory, new_filename)
            # Save the image in PNG format
            #img.save(new_file_path, 'PNG')
            img.save(new_file_path, 'PNG', compress_level=7, optimize=True)
            #img.save(new_file_path[:-3] + "jpeg", 'JPEG', quality=95)
            print(f"Converted {filename}")

# Specify the directory containing the WEBP files
convert_webp_to_png(directory)
