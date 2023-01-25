from typing import List

from marshmallow_dataclass import dataclass

from automateda11y.pw.modal.axe.checks import Checks


@dataclass
class Node:
    all: List[Checks]
    any: List[Checks]
    html: str
    impact: str
    none: List[Checks]
    target: List[str]
