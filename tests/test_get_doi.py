import pytest

from doihelper.doi import DOI
from doihelper.get_doi import get_doi_url, request_doi_json


@pytest.mark.parametrize(
    "url",
    [
        "https://doi.org/10.1063/1.2164808",
        "http://doi.org/10.1063/1.2164808",
        "doi.org/10.1063/1.2164808",
        "10.1063/1.2164808",
    ],
)
def test_get_doi_url(url):
    link = "https://doi.org/10.1063/1.2164808"
    assert get_doi_url(url) == link


def test_request_doi_json():
    link = "https://doi.org/10.1063/1.2164808"
    data = request_doi_json(link)
    assert isinstance(data, DOI)
