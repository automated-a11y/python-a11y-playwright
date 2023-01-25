from typing import List

from marshmallow_dataclass import dataclass


@dataclass
class RelatedNode:
    html: str
    target: List[str]
