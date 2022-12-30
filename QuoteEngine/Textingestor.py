"""Module to ingest data from TXT files."""
from typing import List
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.IngestorInterface import IngestorInterface


class TextIngestor(IngestorInterface):
    """Class to ingest data from TXT files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from the a file.

        :param path (str): path to a file
        :return List[Quotes]: list of quotes
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest')

        quotes = []
        with open(path, 'r') as file:
            for line in file:
                row = line.split('-')
                new_quote = QuoteModel(row[0], row[1])
                quotes.append(new_quote)

        return quotes


if __name__ == '__main__':
    print(TextIngestor.parse(
        '/mnt/d/max/courses/meme_generator/_data/DogQuotes/DogQuotesTXT.txt'))
