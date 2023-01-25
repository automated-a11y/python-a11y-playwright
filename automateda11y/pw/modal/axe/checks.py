from dataclasses import field
from typing import List

from marshmallow import EXCLUDE
from marshmallow_dataclass import dataclass

from automateda11y.pw.modal.axe.relatednode import RelatedNode


@dataclass
class Checks:
    id: str = field(default=None, metadata={"allow_none": True})
    impact: str = field(default=None, metadata={"allow_none": True})
    message: str = field(default=None, metadata={"allow_none": True})
    relatedNodes: List[RelatedNode] = field(default=None, metadata={"allow_none": True})

    class Meta:
        unknown = EXCLUDE
