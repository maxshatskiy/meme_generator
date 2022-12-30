"""Module to ingest data from CSV, TXT, DOCX amd PDF files."""
from typing import List
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.PDFIngestor import PDFIngestor
from QuoteEngine.Textingestor import TextIngestor
from QuoteEngine.CSVIngestor import CSVIngestor
from QuoteEngine.DocxIngestor import DocxIngestor
from QuoteEngine.QuoteModel import QuoteModel



class Ingestor(IngestorInterface):
    """Ingestor class to parse quotes from pdf, txt, docx, csv formats."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from the a file.

        :param path (str): path to a file
        :return List[Quotes]: list of quotes
        """
        if path[-3:] == 'pdf':
            quotes = PDFIngestor.parse(path)
        if path[-3:] == 'txt':
            quotes = TextIngestor.parse(path)
        if path[-4:] == 'docx':
            quotes = DocxIngestor.parse(path)
        if path[-3:] == 'csv':
            quotes = CSVIngestor.parse(path)

        return quotes


if __name__ == '__main__':
    print(Ingestor.parse(
        '/mnt/d/max/courses/meme_generator/_data/DogQuotes/DogQuotesCSV.csv'))
