import os
import shutil
from datetime import date
from PIL import Image

# Check if Pillow package is installed
try:
    import PIL
except ImportError:
    print("Pillow package is required but not installed. Aborting.")
    exit(1)

# Check if the script is invoked with an argument
import sys
if len(sys.argv) < 2:
    print("Usage: python3 convert_images.py <input_folder>")
    exit(1)

# Check if the input folder exists
input_folder = sys.argv[1]
if not os.path.isdir(input_folder):
    print("Input folder does not exist:", input_folder)
    exit(1)

# Iterate over all PNG files in the input folder
for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(".png"):
        input_file = os.path.join(input_folder, file_name)

        # Set the output filenames
        output_color = os.path.splitext(input_file)[0] + "-color.jpg"
        output_bw = os.path.splitext(input_file)[0] + "-bw.jpg"

        # Convert the image to color and up-sample to 300dpi
        image = Image.open(input_file)
        image_rgb = image.convert("RGB")
        image_rgb.save(output_color, dpi=(300, 300))

        # Add metadata to the color image
        shutil.copy2(input_file, output_color)
        os.system(
            f'exiftool -overwrite_original -Title="{os.path.splitext(file_name)[0]}" -Creator="Bruce M. Van Horn II" '
            f'-Date="{date.today().strftime("%Y:%m:%d")}" -Description="Figure for Hands on application development with PyCharm Second Edition" '
            f'-Keywords="PyCharm, Python, Screenshot, Packt" "{output_color}"'
        )

        # Convert the image to grayscale and up-sample to 300dpi
        image_bw = image.convert("L")
        image_bw.save(output_bw, dpi=(300, 300))

        # Add metadata to the grayscale image
        shutil.copy2(input_file, output_bw)
        os.system(
            f'exiftool -overwrite_original -Title="{os.path.splitext(file_name)[0]}" -Creator="Bruce M. Van Horn II" '
            f'-Date="{date.today().strftime("%Y:%m:%d")}" -Description="Figure for Hands on application development with PyCharm Second Edition" '
            f'-Keywords="PyCharm, Python, Screenshot, Packt" "{output_bw}"'
        )

        print(f"Conversion completed for: {file_name}. Output files: {output_color}, {output_bw}")

