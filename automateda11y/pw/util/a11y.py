import json
import os
import uuid

from pathlib import Path

from automateda11y.pw.settings import Settings


def root_dir():
    return Path(__file__).parent.parent.__str__()


def json_reports_dir():
    return Settings.report_dir


class A11y:

    def __init__(self, page):
        self.page = page

    def execute(self, engine, params=None):
        if json_reports_dir() is None:
            raise Exception("Reports path is not set, 'Settings.report_dir = <report_path>' is mandate")
        self.page.wait_for_load_state("domcontentloaded")
        js_text = Path(root_dir() + "/resources/js/", engine.name.lower() + ".js").read_text()
        self.page.evaluate("async (js)=> await window.eval(js)", js_text)
        data = self.page.evaluate("async (param) => await axeData(param)", params.to_json()) if engine.value == 2 else \
            self.page.evaluate("async (param) => await getData(param)", params.to_json())
        file_name = json_reports_dir() + '/' + engine.name.lower() + '/json/' + uuid.uuid4().__str__() + '.json'
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return data
