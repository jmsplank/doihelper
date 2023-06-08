"""Get info from DOI."""
from re import sub
from urllib.parse import urljoin

import requests

from .doi import DOI

DOI_BASE = "https://doi.org/"


def get_doi_url(url: str, DOI_BASE: str = DOI_BASE) -> str:
    """Make sure URL is valid.

    Args:
        url (str): URL to process.
        DOI_BASE (str, optional): Base URL for DOI. Defaults to DOI_BASE.

    Returns:
        str: Valid URL.
    """
    url = url.strip()

    url = sub(r"^.*doi.org\/", DOI_BASE, url)

    if not url.startswith(DOI_BASE):
        url = urljoin(DOI_BASE, url)

    return url


def request_doi_json(url: str) -> DOI:
    """Make a request to DOI API for metadata in JSON format.

    Note:
        Schema is defined at:
            https://github.com/citation-style-language/schema/blob/master/schemas/input/csl-data.json
        Header difinitions at:
            https://citation.crosscite.org/docs.html

    Args:
        url (str): The URL of the paper.

    Returns:
        DOI: A DOI object.
    """
    headers = {"Accept": "application/vnd.citationstyles.csl+json"}
    res = requests.get(url, headers=headers).json()

    return DOI(
        title=res["title"],
        authors=[res["author"][i]["family"] for i in range(len(res["author"]))],
        year=str(res["issued"]["date-parts"][0][0]),
        url=res["URL"],
    )


def request_text_citation(url: str) -> str:
    headers = {"Accept": "text/x-bibliography"}
    res = requests.get(url, headers=headers)
    return res.text


def get_doi(doi: str) -> DOI:
    """Get a DOI from a URL or a doi.

    Args:
        doi (str): the doi, http://doi.org/ part is optional

    Returns:
        DOI: DOI object
    """
    url = get_doi_url(doi)
    data = request_doi_json(url)
    return data
