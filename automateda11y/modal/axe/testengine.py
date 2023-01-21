from marshmallow_dataclass import dataclass


@dataclass
class TestEngine:
    name: str
    version: str
