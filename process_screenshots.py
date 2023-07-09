import os
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
    print("Usage: python3 process_screenshots.py <input_folder>")
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

        # Open the image
        image = Image.open(input_file)

        # Calculate the new size based on the desired DPI
        dpi = (300, 300)
        width = int(image.width * dpi[0] / image.info['dpi'][0])
        height = int(image.height * dpi[1] / image.info['dpi'][1])
        size = (width, height)

        # Resize the image
        image_resized = image.resize(size, resample=Image.LANCZOS)

        # Save the color image
        output_color = os.path.splitext(input_file)[0] + "-color.jpg"
        image_resized.save(output_color, "JPEG", dpi=dpi)

        # Convert the image to grayscale
        image_bw = image_resized.convert("L")

        # Save the grayscale image
        output_bw = os.path.splitext(input_file)[0] + "-bw.jpg"
        image_bw.save(output_bw, "JPEG", dpi=dpi)

        print(f"Conversion completed for: {file_name}. Output files: {output_color}, {output_bw}")
        