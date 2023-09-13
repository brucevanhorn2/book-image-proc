import os
import sys
from docx import Document


def extract_images_from_docx(docx_file, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Load the docx file
    doc = Document(docx_file)

    # Counter for the image index
    image_index = 0

    # Iterate over all inline shapes in the document
    for inline_shape in doc.inline_shapes:
        if inline_shape.type == 3:  # InlineShapeType.PICTURE
            # Get the image data
            image_data = inline_shape._inline.graphic.graphicData.pic.blip.getbytes()

            # Save the image to the output folder
            image_filename = f"image_{image_index}.png"
            image_path = os.path.join(output_folder, image_filename)
            with open(image_path, "wb") as f:
                f.write(image_data)

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
