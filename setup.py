from setuptools import find_packages, setup

with open("requirements.txt", "r") as file:
    requirements = [line.strip() for line in file.readlines()]

setup(
    name="doihelper",
    version="0.0.2",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "paperpdf = paper_title.cli:paperpdf",
            "papercitation = paper_title.cli:papercitation",
            "paperformatted = paper_title.cli:paperformatted",
        ]
    },
)
