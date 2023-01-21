from marshmallow_dataclass import dataclass
from typing import List


@dataclass
class RelatedNode:
    html: str
    target: List[str]
