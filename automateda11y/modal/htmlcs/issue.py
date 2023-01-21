from marshmallow_dataclass import dataclass
from typing import Set


@dataclass
class Issue:
    type: int
    code: str
    techniques: Set[str]
    msg: str
    tag: str
    element: str
