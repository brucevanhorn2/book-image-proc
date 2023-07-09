# Book Image Processing Scripts

There are two scripts.  The main script is ```process_screenshots.py```.  This is a script I intend to use in conjunction with writing books for Packt, and maybe other publishers in the future.  At present, I am working on the second edition of "Hands on Application Development with PyCharm".  I am generating 30 or 40 screen shots per chapter, and each shot must be:
* Upscaled to 300 dpi to meet the requirements for printing
* Saved as a full-color image.  The publisher includes a full color image catalog of all the images in the book since the book itself is printed in black and white.
* Saved as a grayscale image.  Again, the book is printed in black and white, so the grayscale is the most important of the images.  It needs to be camera ready.

The second script is ```extract_images.py```.  This script takes a ```.docx``` file and it extracts the images.  Normally, as I write chapters, I do screenshots and just paste them into Word.  This extraction script allows me to pull the images out.

In concert, you run the extraction script against the docx file, then run the process_screenshots.py script against the extracted images.  Before I do that, though I usually batch rename them with [Core Renamer](https://gitlab.com/cubocore/coreapps/corerenamer).

## Usage

Generally, my work flow is to write, and as I do I take screen shots of software running in an isolated VM.  I usually just copy and paste the screenshots straight into Word.  Then after my editor makes her first pass, she sends back all my required corrections.  On the second pass, I correct the manuscript, then pull the images out with the extract script, convert with the process script, then go back through the copy and replace the images manually.  I could probably automate that too, but I take the opportunity as I'm replaceing to make sure the image numbering is right.

The commands run the scripts are:

```python3 extract_images.py <path-to-docx-file.docx>```
    
```python3 process_screenshots.py <input_folder> <output_folder>```


## Requirements

I used the ```pillow``` library to handle the image processing, and ```python-docx``` to process Word files.  The requirements are in the ```requirements.txt``` file per usual with Python projects.

## You can use this for whatever you want

Seriously, this isn't exactly rocket surgery or the cure for cancer.  If this script helps you, you can use it for whatever you want.  I don't need credit.  If you're married to a lawyer like I am, I guess you need this:

## License

This script is released into the public domain.
