from typing import List

from marshmallow_dataclass import dataclass


@dataclass
class RunOnly:
    type: str
    values: List[str]
