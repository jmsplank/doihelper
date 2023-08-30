"""Command line interface for paper_title."""
import typer

from .doi import DOI
from .get_doi import get_doi, get_text_citation


def pdf(d):
    print(get_doi(d).pdf_title)


def citation(d):
    print(get_doi(d).citation)


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
