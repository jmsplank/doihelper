"""DOI object."""
from dataclasses import dataclass
from re import sub


@dataclass
class DOI:
    """DOI object.

    Attributes:
        title (str): The title of the paper.
        first_author (str): The surname of the first author.
        year (str): The year of publication.
        url (str): The URL of the paper.
    """

    title: str
    first_author: str
    year: str
    url: str

    @staticmethod
    def parse_field(field: str):
        """Make string filename safe.

        Args:
            field (str): Field to parse.

        Returns:
            str: Parsed field.
        """
        out = sub(r"[^\w\s]+", "", field)
        out = out.strip().title().replace(" ", "_")
        return out

    @property
    def pdf_title(self):
        """Preoperty to return the PDF title.

        Returns:
            str: The PDF title.
        """
        return (
            f'{self.parse_field(f"{self.first_author}_{self.year}_{self.title}")}.pdf'
        )
