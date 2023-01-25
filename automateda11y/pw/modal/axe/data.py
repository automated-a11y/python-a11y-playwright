from dataclasses import field

from marshmallow import EXCLUDE
from marshmallow_dataclass import dataclass


@dataclass
class Data:
    bgColor: str = field(default=None, metadata={"allow_none": True})
    contrastRatio: float = field(default=None, metadata={"allow_none": True})
    expectedContrastRatio: str = field(default=None, metadata={"allow_none": True})
    fgColor: str = field(default=None, metadata={"allow_none": True})
    fontSize: str = field(default=None, metadata={"allow_none": True})
    fontWeight: str = field(default=None, metadata={"allow_none": True})
    messageKey: str = field(default=None, metadata={"allow_none": True})
    shadowColor: str = field(default=None, metadata={"allow_none": True})

    class Meta:
        unknown = EXCLUDE
