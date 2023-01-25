from dataclasses import field
from typing import List

from marshmallow_dataclass import dataclass

from automateda11y.pw.modal.axe.node import Node


@dataclass
class IssueType:
    description: str
    help: str
    helpUrl: str
    id: str
    impact: str = field(metadata={"allow_none": True})
    nodes: List[Node]
    tags: List[str]
