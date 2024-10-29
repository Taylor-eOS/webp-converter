The script converts all WEBP files in `~/Desktop` to a more common image file format. Files are first moved to a secondary folder and converted from there, in order to preserve their placement on teh Desktop.

webp.py: Converts to PNG\
webp_j.py: Converts to JPG (use this one)\
webp_j_s.py: Converts to JPG with saturation adjustment

To make a basc script that launches the script, use this format:
```
cd path/to/webp-converter
source bin/activate
python webp_j.py
deactivate
exit
```
