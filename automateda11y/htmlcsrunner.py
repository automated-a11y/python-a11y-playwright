from automateda11y.a11y.engine import Engine
from automateda11y.modal.htmlcs.issues import Issues
from automateda11y.modal.params import Params
from automateda11y.util.a11y import A11y


class HtmlCsRunner:

    def __init__(self, page):
        self.a11y = A11y(page)
        self.params = Params()

    def set_standard(self, standard="WCAG2AA"):
        self.params.set_standard(standard)

    def set_ignore_code(self, codes):
        self.params.set_ignore_codes(codes)

    def set_page_title(self, page_title):
        self.params.set_page_title(page_title)

    def execute(self):
        data = self.a11y.execute(Engine.HTMLCS, self.params)
        return Issues.Schema().load(data, )

