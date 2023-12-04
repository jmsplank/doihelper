"""Command line interface for paper_title."""
import typer

from .doi import DOI
from .get_doi import get_doi, get_text_citation


def pdf(d):
    print(get_doi(d).pdf_title)


def citation(doi, style: str = "default"):
    """Create an in-text citation in a specific --style.

    doi: the DOI, with or without the preceding `https://` and/or `doi.org/`
    --style (str, optional): The style, can be `default` or `APA`.
    """
    print(get_doi(doi).citation(cite_type=style))


def formatted(doi):
    text = get_text_citation(doi)
    print(text)


def paperpdf():
    """Make a .pdf filename."""
    typer.run(pdf)


def papercitation():
    """Make an inline citation."""
    typer.run(citation)


def paperformatted():
    """Make a formatted full-text citation."""
    typer.run(formatted)
