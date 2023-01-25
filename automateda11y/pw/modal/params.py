import json


class Params:
    def __init__(self):
        self.ignoreCodes = []
        self.standard = "WCAG2AA"
        self.pageTitle = None

    def set_standard(self, standard):
        self.standard = standard

    def set_ignore_codes(self, ignore_codes):
        self.ignoreCodes = ignore_codes

    def set_page_title(self, page_title):
        self.pageTitle = page_title

    def to_json(self):
        return json.dumps(self.__dict__)
