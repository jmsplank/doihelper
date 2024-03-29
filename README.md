# paper-title

<p align='center'>
    <img src='https://img.shields.io/badge/python-v3.10-blue'>
    <img src='https://img.shields.io/badge/code%20format-black-black'>
    <img src='https://img.shields.io/badge/testing-pytest-yellowgreen'>
</p>

Get a formatted pdf filename for a paper specified by a DOI.

## Usage

### Title for .pdf file

```shell
$ papertitle https://doi.org/10.1038/nature05116

Drake_2006_Electron_Acceleration_From_Contracting_Magnetic_Islands_During_Reconnection.pdf
```

The format is: `AuthorSurname_Year_Title_Of_Paper.pdf`

### Short citation
```shell
$ papercitation https://doi.org/10.1038/nature05116

Drake et al - 2006 - Electron acceleration from contracting magnetic islands during reconnection
```

### Full APA style formatted citation
```shell
$ paperformatted https://doi.org/10.1038/nature05116

Drake, J. F., Swisdak, M., Che, H., & Shay, M. A. (2006). Electron acceleration from contracting magnetic islands during reconnection. Nature, 443(7111), 553–556. https://doi.org/10.1038/nature05116
```

## Requirements

- `python>=3.10`
- `typer>=0.9`
- `requests>=2.30`
- `pytest>=7.3`

## Installation

```shell
$ git clone git@github.com:jmsplank/paper-title.git
$ cd paper_titles
$ pip install .
```

## Testing

This project usses `pytest` to test the code.

```bash
$ pytest
```

To get a coverage report, use:

```bash
pytest --cov-report=html --cov
```

This generates coverage html, view it by opening `./htmlcov/index.html`.
