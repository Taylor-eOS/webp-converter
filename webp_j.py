import os
from PIL import Image
import time

default = '~/Desktop'
directory = input(f'Input ({default}): ') or default
backup_folder = 'webp_files'
silent_deleting = True

def convert_webp_to_png(directory):
    directory = os.path.expanduser(directory)
    documents_directory = os.path.expanduser("~/Documents")
    webp_directory = os.path.join(documents_directory, backup_folder)
    if not os.path.exists(webp_directory):
        os.makedirs(webp_directory)
    is_default_desktop = os.path.normpath(directory) == os.path.normpath(os.path.expanduser(default))
    desktop_directory = os.path.expanduser(default)
    os.chdir(desktop_directory)
    for filename in os.listdir(directory):
        if filename.lower().endswith((".png", ".webp")):
            file_path = os.path.join(directory, filename)
            base, _ = os.path.splitext(filename)
            new_filename = base + ".jpeg"
            new_file_path = os.path.join(directory, new_filename)
            backup_path = os.path.join(webp_directory, filename)
            os.rename(file_path, backup_path)
            try:
                img = Image.open(backup_path)
                if img.mode not in ('RGB', 'JPEG', 'L'):
                    img = img.convert('RGB')
                img.save(new_file_path, 'JPEG', quality=95)
                print(f"Converted {filename} to JPEG")
                if not is_default_desktop:
                    try:
                        os.remove(backup_path)
                        if not silent_deleting: print(f"removed backup copy")
                    except OSError:
                        pass
            except Exception as e:
                print(f"Error processing {filename}: {e}")
            time.sleep(0.2)

convert_webp_to_png(directory)

