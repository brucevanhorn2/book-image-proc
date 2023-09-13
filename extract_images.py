import os
import sys
import re
import docx2txt

def extract_images_from_docx(docx_file, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Use docx2txt to convert the DOCX document to plain text
    text = docx2txt.process(docx_file, output_folder)

    # Define a regular expression to find image references in the plain text
    image_pattern = re.compile(r'!\[.*?\]\((.*?)\)')

    # Find all image references in the plain text
    image_matches = image_pattern.findall(text)

    # Counter for the image index
    image_index = 0

    for image_match in image_matches:
        # Check if the image reference contains a valid image file extension (e.g., .png, .jpg)
        if any(image_match.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif']):
            # Copy the image file to the output folder
            image_path = os.path.join(os.path.dirname(docx_file), image_match)
            if os.path.exists(image_path):
                image_filename = f"image_{image_index}.png"  # Rename the image
                image_output_path = os.path.join(output_folder, image_filename)
                with open(image_path, "rb") as source, open(image_output_path, "wb") as destination:
                    destination.write(source.read())
                image_index += 1

    print("Image extraction completed!")

if __name__ == "__main__":
    # Check if the script is invoked with the correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python3 extract_images.py <docx_file> <output_folder>")
        sys.exit(1)

    # Get the command-line arguments
    docx_file = sys.argv[1]
    output_folder = sys.argv[2]

    extract_images_from_docx(docx_file, output_folder)
