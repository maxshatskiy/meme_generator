"""Module for Ingestion of the data."""
from typing import List
from abc import ABC, abstractmethod
from QuoteEngine.QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """Abstract class for ingestion of the data."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if certain file can be ingested by a module.

        :param path: path to a file.
        :return: bool.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method to parse data from files.

        :param path: path to a file
        :return:
        """
