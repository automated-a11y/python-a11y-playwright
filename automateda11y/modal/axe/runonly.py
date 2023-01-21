from marshmallow_dataclass import dataclass
from typing import List


@dataclass
class RunOnly:
    type: str
    values: List[str]
