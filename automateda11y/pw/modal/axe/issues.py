from typing import List

from marshmallow_dataclass import dataclass

from automateda11y.pw.modal.axe.issuetype import IssueType
from automateda11y.pw.modal.axe.testengine import TestEngine
from automateda11y.pw.modal.axe.testenvironment import TestEnvironment
from automateda11y.pw.modal.axe.testrunner import TestRunner
from automateda11y.pw.modal.axe.tooloptions import ToolOptions


@dataclass
class Issues:
    browser: str
    date: str
    device: str
    dimension: str
    id: str
    testEngine: TestEngine
    testEnvironment: TestEnvironment
    testRunner: TestRunner
    timestamp: str
    title: str
    toolOptions: ToolOptions
    url: str
    violations: List[IssueType]
    inapplicable: List[IssueType]
    incomplete: List[IssueType]
