import os
from PIL import Image

def convert_webp_to_png(directory):
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
            img.save(new_file_path, 'PNG')
            print(f"Converted {filename} to {new_filename}")

# Specify the directory containing the WEBP files
directory = "path/to/folder"
convert_webp_to_png(directory)
