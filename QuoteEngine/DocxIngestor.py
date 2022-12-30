"""Module to ingest data from DOCX files."""
from typing import List
import docx
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.IngestorInterface import IngestorInterface


class DocxIngestor(IngestorInterface):
    """Class to ingest data from DOCX files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from the a file.

        :param path (str): path to a file
        :return List[Quotes]: list of quotes
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes


if __name__ == '__main__':
    print(DocxIngestor.parse(
        '/mnt/d/max/courses/meme_generator/_data/DogQuotes/DogQuotesDOCX.docx'))
