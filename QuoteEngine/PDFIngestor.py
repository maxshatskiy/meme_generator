"""Module to ingest data from PDF files."""
import os
import subprocess
from typing import List
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.Textingestor import TextIngestor

class PDFIngestor(IngestorInterface):
    """Class to ingest data from PDF files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from the a file.

        :param path (str): path to a file
        :return List[Quotes]: list of quotes
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest')

        _ = subprocess.call(['pdftotext', '-layout', '-nopgbrk', path])
        quotes = TextIngestor.parse(path.replace('.pdf', '.txt'))
        os.remove(path.replace('.pdf', '.txt'))

        return quotes


if __name__ == '__main__':
    print(PDFIngestor.parse(
        '/mnt/d/max/courses/meme_generator/_data/DogQuotes/DogQuotesPDF.pdf'))
