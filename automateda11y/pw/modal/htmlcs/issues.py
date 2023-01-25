from typing import List

from marshmallow_dataclass import dataclass

from automateda11y.pw.modal.htmlcs.issue import Issue


@dataclass
class Issues:
    errors: int
    warnings: int
    notices: int
    standard: str
    date: str
    dimension: str
    device: str
    browser: str
    url: str
    title: str
    results: List[Issue]
    id: str

