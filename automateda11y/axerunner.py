from marshmallow import EXCLUDE

from automateda11y.a11y.engine import Engine
from automateda11y.modal.axe.issues import Issues
from automateda11y.modal.params import Params
from automateda11y.util.a11y import A11y


class AxeRunner:

    def __init__(self, page):
        self.a11y = A11y(page)
        self.params = Params()

    def set_page_title(self, page_title):
        self.params.set_page_title(page_title)

    def execute(self):
        data = self.a11y.execute(Engine.AXE, self.params)
        return Issues.Schema().load(data, unknown=EXCLUDE)
