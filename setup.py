from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "ReadMe.md").read_text()

setup(
    name='python-a11y-playwright',
    version='1.0.1',
    packages=['automateda11y', 'automateda11y.a11y', 'automateda11y.util', 'automateda11y.modal',
              'automateda11y.modal.axe', 'automateda11y.modal.htmlcs', 'automateda11y.resources'],
    package_data={'automateda11y.resources': ['js/*.js']},
    include_package_data=True,
    url='https://github.com/automated-a11y/python-a11y-playwright',
    license='MIT',
    author='Sridhar Bandi',
    author_email='sridhar.bandi.ece@gmail.com',
    description='Automate Web Accessibility Testing using AXE/HTMLCS with Playwright Python',
    install_requires=['marshmallow-dataclass', 'marshmallow'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
