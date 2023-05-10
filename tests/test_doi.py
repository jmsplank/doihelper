from paper_title.doi import DOI


def test_doi_parse_field():
    doi = DOI(title="test", first_author="author", year="2023", url="https://url.org")
    assert doi.parse_field("test 123 bean's") == "Test_123_Beans"


def test_doi_pdf_title():
    doi = DOI(title="test", first_author="author", year="2023", url="https://url.org")
    assert doi.pdf_title == "Author_2023_Test.pdf"
