from dataclasses import field
from typing import List

from marshmallow import EXCLUDE
from marshmallow_dataclass import dataclass

from automateda11y.pw.modal.axe.runonly import RunOnly


@dataclass
class ToolOptions:
    reporter: str = field(default=None, metadata={"allow_none": True})
    resultTypes: List[str] = field(default=None, metadata={"allow_none": True})
    runOnly: RunOnly = field(default=None, metadata={"allow_none": True})

    class Meta:
        unknown = EXCLUDE
