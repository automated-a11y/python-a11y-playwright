from dataclasses import field

from marshmallow_dataclass import dataclass
from typing import List
from automateda11y.modal.axe.data import Data
from automateda11y.modal.axe.relatednode import RelatedNode


@dataclass
class Checks:
    data: Data = field(default=None, metadata={"allow_none": True})
    id: str = field(default=None, metadata={"allow_none": True})
    impact: str = field(default=None, metadata={"allow_none": True})
    message: str = field(default=None, metadata={"allow_none": True})
    relatedNodes: List[RelatedNode] = field(default=None, metadata={"allow_none": True})
