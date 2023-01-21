from marshmallow_dataclass import dataclass
from typing import List
from automateda11y.modal.htmlcs.issue import Issue


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

