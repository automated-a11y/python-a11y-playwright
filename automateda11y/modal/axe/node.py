from marshmallow_dataclass import dataclass
from typing import List
from automateda11y.modal.axe.checks import Checks


@dataclass
class Node:
    all: List[Checks]
    any: List[Checks]
    html: str
    impact: str
    none: List[Checks]
    target: List[str]
