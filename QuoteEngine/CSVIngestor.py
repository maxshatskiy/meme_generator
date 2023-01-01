"""Module to ingest data from CSV files."""
from typing import List
import pandas as pd
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.IngestorInterface import IngestorInterface


class CSVIngestor(IngestorInterface):
    """Class to ingest data from CSV files."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from a file.

        :param path (str): path to a file
        :return List[Quotes]: list of quotes
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest')

        quotes = []
        quotes_df = pd.read_csv(path, header=0)

        for _, row in quotes_df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes


if __name__ == '__main__':
    print(CSVIngestor.parse(
        '/mnt/d/max/courses/meme_generator/_data/DogQuotes/DogQuotesCSV.csv'))
