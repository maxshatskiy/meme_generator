"""Module MemeGenerator provides a functionality to generate memes."""
import os
from PIL import Image, ImageDraw, ImageFont

class MemeEngine:
    """Class to generate memes by placing a text with author to a picture."""

    def __init__(self, output_dir):
        """Assign output dir to a new instance."""
        self.output_dir = output_dir

    @staticmethod
    def read_and_crop(img_path, width):
        """Read image from the path specified and resize it.

        :param path (str): path to a file
        :return image: scaled image
        """
        img = Image.open(img_path)
        if img.size[1] < 500:
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        return img

    @staticmethod
    def add_quote(img, text, author):
        """Add quote to an image.

        :param img (PIL image): image
        :param text (str): text to add to image
        :param author (str): author of the text to add to an image
        """
        if text is not None and author is not None:

            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=30)
            draw.text((10, 30), text + '-' + author, font=font, fill='black')

        return img

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a meme by placing a text and author of the text on an image.

        :param img_path (str): path the the image used for the meme.
        :param text (str): text to be placed on a an image.
        :param author (str): author of the text.
        :param width (int): a width to resize an image.
        :return (str): path to the resulting image meme.

        """
        img_name = os.path.split(img_path)[1]
        img = self.read_and_crop(img_path, width)
        img = self.add_quote(img, text, author)
        output_image = os.path.join(self.output_dir, 'meme_' + img_name)
        img.save(output_image)

        return output_image

if __name__ == "__main__":
    meme = MemeEngine('/mnt/d/max/courses/meme_generator/tmp')
    path = meme.make_meme(
        img_path='/mnt/d/max/courses/meme_generator/_data/photos/dog/xander_1.jpg',
        text="test quote",
        author="test author")
