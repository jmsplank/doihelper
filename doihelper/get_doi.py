"""Get info from DOI."""
from re import sub
from urllib.parse import urljoin

import requests

from .doi import DOI


class DOI_URL:
    """Use to convert a raw_input to a queryable url.

    Attributes:
        DOI_BASE (str): Base URL for the doi database
    """

    DOI_BASE = "https://doi.org/"
    headers: dict[str, str] = {"Accept": "application/vnd.citationstyles.csl+json"}

    def __init__(self, raw_input: str) -> None:
        """Initalise DOI_URL with an unsanitised input.

        Args:
            raw_input (str): Unsanitised raw user input.
        """
        self._raw_input = raw_input
        self.url = self._get_doi_url()

    def _get_doi_url(self) -> str:
        """Validate and correct the _raw_input instance attr."""
        url = self._raw_input.strip()

        url = sub(r"^.*doi.org\/", self.DOI_BASE, url)

        if not url.startswith(self.DOI_BASE):
            url = urljoin(self.DOI_BASE, url)

        return url

    def request(self) -> requests.Response:
        """Request doi information.

        Note:
            Schema is defined at:
                https://github.com/citation-style-language/schema/blob/master/schemas/input/csl-data.json
            Header difinitions at:
                https://citation.crosscite.org/docs.html
        """
        res = requests.get(self.url, headers=self.headers)
        return res

    def json(self) -> DOI:
        res = self.request().json()
        return DOI(
            title=res["title"],
            authors=[res["author"][i]["family"] for i in range(len(res["author"]))],
            year=str(res["issued"]["date-parts"][0][0]),
            url=res["URL"],
            doi=self.url,
        )

    def text(self) -> str:
        """Use a text/x-bibliography header to get a plain text citation.

        Returns:
            str: APA formatted unicode citation
        """
        headers = {"Accept": "text/x-bibliography"}
        res = requests.get(self.url, headers=headers)
        # Force set response encoding to utf-8
        # This is based of CSL docs using only utf-8
        # https://docs.citationstyles.org/en/stable/search.html?q=encoding&check_keywords=yes&area=default
        res.encoding = "utf-8"

        return res.text  # All python strings are unicode so this should work


def get_doi(doi: str) -> DOI:
    """Get a DOI from a URL or a doi.

    Args:
        doi (str): the doi, http://doi.org/ part is optional

    Returns:
        DOI: DOI object
    """
    url = DOI_URL(doi)
    return url.json()


def get_text_citation(doi: str) -> str:
    """Get a citation from a url or doi.

    Args:
        doi (str): the doi, http://doi.org/ part is optional

    Returns:
        str: An APA style citation in unicode
    """
    url = DOI_URL(doi)
    return url.text()
