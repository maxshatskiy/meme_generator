"""Module for a quote."""
class QuoteModel:
    """A base Quote Model Class."""

    def __init__(self, body, author):
        """Create a new quote.

        :body (str): text of the body
        :author (str): author of the quote
        """
        self.body = body
        self.author = author

    def __str__(self):
        """Provide object description."""
        return self.body + '-' + self.author
