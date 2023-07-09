# Screenshot Processor

This is a script I intend to use in conjunction with writing books for Packt, and maybe other publishers in the future.  At present, I am working on the second edition of "Hands on Application Development with PyCharm".  I am generating 30 or 40 screen shots per chapter, and each shot must be:
* Upscaled to 300 dpi to meet the requirements for printing
* Saved as a full-color image.  The publisher includes a full color image catalog of all the images in the book since the book itself is printed in black and white.
* Saved as a grayscale image.  Again, the book is printed in black and white, so the grayscale is the most important of the images.  It needs to be camera ready.

## Usage

```python3 process_screenshots.py input_folder```

The script should be run with one argument which is a full path to a folder containing a collection of screen shots in .png format.  For my own workflow, I manually rename these images to match the figure number in the book, then run this script to generate the images in the final format.  I then go back through my copy in Word and replace the images with the processed grayscale.

This script, then, takes each image and performs the operations described earlier saving new versions of the original image in JPEG format.  The color image bears a suffix of "-color" while the black and white version bears the suffix "-bw".

The script adds metadata to the saved images including my name as the creator and a few other details.

## Requirements

I used the pillow library to handle the image processing.

## You can use this for whatever you want

Seriously, this isn't exactly rocket surgery or the cure for cancer.  If this script helps you, you can use it for whatever you want.  I don't need credit.  If you're married to a lawyer like I am, I guess you need this:

## License

This script is released into the public domain.
