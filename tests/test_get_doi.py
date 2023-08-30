import pytest

from doihelper.doi import DOI
from doihelper.get_doi import DOI_URL


@pytest.mark.parametrize(
    "url",
    [
        "https://doi.org/10.1063/1.2164808",
        "http://doi.org/10.1063/1.2164808",
        "doi.org/10.1063/1.2164808",
        "10.1063/1.2164808",
    ],
)
def test_url_format(url):
    link = "https://doi.org/10.1063/1.2164808"
    assert DOI_URL(url).url == link


def test_json():
    link = "https://doi.org/10.1063/1.2164808"
    data = DOI_URL(link).json()
    assert isinstance(data, DOI)


def test_text():
    link = "10.1029/2022GL099544"
    text = DOI_URL(link).text()
    expected_text = """Ng, J., Chen, L. â\x80\x90J., Bessho, N., Shuster, J., Burkholder, B., & Yoo, J. (2022). Electronâ\x80\x90Scale Reconnection in Threeâ\x80\x90Dimensional Shock Turbulence. Geophysical Research Letters, 49(15). Portico. https://doi.org/10.1029/2022gl099544\n"""
    assert text == expected_text
