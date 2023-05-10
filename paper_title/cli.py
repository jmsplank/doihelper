"""Command line interface for paper_title."""
import typer

from .get_doi import get_doi_url, request_doi_json


def main(doi: str):
    """Command line script.

    Args:
        doi (str): The DOI to process.
    """
    url = get_doi_url(doi)
    doi_data = request_doi_json(url)
    print(doi_data.pdf_title)


def cli():
    """Entry point."""
    typer.run(main)
