"""Command line interface for paper_title."""
import typer

from .doi import DOI
from .get_doi import get_doi_url, request_doi_json, request_text_citation


def main(doi: str) -> DOI:
    """Command line script.

    Args:
        doi (str): The DOI to process.
    """
    url = get_doi_url(doi)
    doi_data = request_doi_json(url)
    # print(doi_data.pdf_title)
    return doi_data


def pdf(d):
    print(main(d).pdf_title)


def citation(d):
    print(main(d).citation)


def formatted(doi):
    url = get_doi_url(doi)
    text = request_text_citation(url)
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
