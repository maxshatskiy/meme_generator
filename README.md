This project is used to generate memes. A text is read from a csv, txt, pdf or docx file and added to a picture.
To read text from pdf a xpdf reader should be installed.

**Module QuoteEngine**: provides functionality to read quotes from different types of files.

**Module MemeGerator**: provides functionality to read picture, crop it to be maximum 500 width, add text to it and 
save to a specified location.

It is possible to use meme generator from command line as follows:

python3 meme.py --path --body --author

where 
* --path - is a path to an image file
* --body - is a text of the meme
* --author - is an author of the meme
* 
all 3 parameters are optional. If not provided, a randomly generated parameters are used.
Another options is to use flask application by running:

python3 app.py

Functionality is similar to the one provided via command line interface.