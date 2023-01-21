from typing import Set

from marshmallow_dataclass import dataclass


@dataclass
class Issue:
    type: int
    code: str
    techniques: Set[str]
    msg: str
    tag: str
    element: str
