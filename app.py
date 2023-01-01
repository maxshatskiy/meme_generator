"""Flask app for meme generation."""
import random
import os
import requests
from flask import Flask, render_template, abort, request
from PIL import Image
from QuoteEngine.Ingestor import Ingestor
from MemeGenerator.MemeGenerator import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs

quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    img_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    try:
        r = requests.get(img_url)
    except requests.exceptions.ConnectionError:
        print("Invalid URL")
        return render_template('meme_error.html')

    temp_file = './tmp/temp.jpg'

    with open(temp_file, 'wb') as f:
        f.write(r.content)

    meme = MemeEngine('./tmp')
    path = meme.make_meme('./tmp/temp.jpg', body, author)

    if os.path.isfile(temp_file):
        os.remove(temp_file)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
