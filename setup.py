from pathlib import Path
from setuptools import setup, find_packages

# Package meta-data.
NAME = 'python-a11y-playwright'
DESCRIPTION = 'Automate Web Accessibility Testing using AXE/HTMLCS with Playwright Python'
URL = 'https://github.com/automated-a11y/python-a11y-playwright'
EMAIL = 'sridhar.bandi.ece@gmail.com'
AUTHOR = 'Sridhar Bandi'
VERSION = '1.0.1'
CLASSIFIERS = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
]

this_directory = Path(__file__).parent
long_description = (this_directory / "ReadMe.md").read_text()

setup(
    name=NAME,
    version=VERSION,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    package_data={'automateda11y.pw.resources': ['js/*.js']},
    include_package_data=True,
    url=URL,
    license='MIT',
    classifiers=CLASSIFIERS,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    install_requires=['marshmallow-dataclass', 'marshmallow'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
