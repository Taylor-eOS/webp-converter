import os
from PIL import Image
import time

directory = input('Input: ') or '~/Desktop'
backup_folder = 'webp_files'

def convert_webp_to_png(directory):
    directory = os.path.expanduser(directory)
    documents_directory = os.path.expanduser("~/Documents")
    webp_directory = os.path.join(documents_directory, backup_folder)
    if not os.path.exists(webp_directory):
        os.makedirs(webp_directory)
    desktop_directory = os.path.expanduser("~/Desktop")
    os.chdir(desktop_directory)
    for filename in os.listdir(directory):
        if filename.endswith((".png", ".webp")):
            file_path = os.path.join(directory, filename)
            base, _ = os.path.splitext(filename)
            new_filename = base + ".jpeg"
            new_file_path = os.path.join(directory, new_filename)
            webp_filename = os.path.join(webp_directory, filename)
            os.rename(file_path, webp_filename)
            img = Image.open(webp_filename)
            if img.mode not in ('RGB', 'JPEG', 'L'):
                img = img.convert('RGB')
            img.save(new_file_path, 'JPEG', quality=95)
            print(f"Converted {filename} to JPEG")
            time.sleep(0.2)

convert_webp_to_png(directory)

