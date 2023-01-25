from marshmallow_dataclass import dataclass


@dataclass
class TestEnvironment:
    orientationAngle: int
    orientationType: str
    userAgent: str
    windowHeight: int
    windowWidth: int
    