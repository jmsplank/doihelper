from setuptools import find_packages, setup

with open("requirements.txt", "r") as file:
    requirements = [line.strip() for line in file.readlines()]

setup(
    name="paper-title",
    version="0.0.1",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={"console_scripts": ["paper-title = paper_title.cli:cli"]},
)
