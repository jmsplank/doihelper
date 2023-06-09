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
    authors: list[str]
    year: str
    url: str

    @staticmethod
    def remove_illegal_chars(s: str, sub_illegal: str = "") -> str:
        out = sub(r"[^\w\s\-\u2010]+", sub_illegal, s)
        return out

    @staticmethod
    def parse_field(field: str):
        """Make string filename safe.

        Args:
            field (str): Field to parse.

        Returns:
            str: Parsed field.
        """
        out = field.replace("-", " ")
        out = DOI.remove_illegal_chars(out, sub_illegal="")
        out = out.strip().title().replace(" ", "_")
        return out

    def fmt_authors(self) -> str:
        """Format author string based on no. authors.

        If num_authors <= 2:
        "Aauthor and Bauthor"

        If num_authors > 2:
        "Aauthor et al."

        Returns:
            str: Formatted string
        """
        num_authors = len(self.authors)

        if num_authors > 2:
            return f"{self.authors[0]} et al."
        else:
            return " and ".join(self.authors[:2])

    @property
    def citation(self) -> str:
        """Text friendly citation of article.

        Returns:
            str: Single line citation
        """
        return self.remove_illegal_chars(
            f"{self.fmt_authors()} - {self.year} - {self.title}", sub_illegal=""
        )

    @property
    def first_author(self) -> str:
        """Property surname of first author.

        Returns:
            str: Surname
        """
        return self.authors[0]

    @property
    def pdf_title(self) -> str:
        """Preoperty to return the PDF title.

        Returns:
            str: The PDF title.
        """
        return (
            f'{self.parse_field(f"{self.first_author}_{self.year}_{self.title}")}.pdf'
        )
