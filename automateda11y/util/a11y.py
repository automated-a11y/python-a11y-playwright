import json
import os
import uuid

from pathlib import Path


def root_dir():
    return Path(__file__).parent.parent.parent.__str__()


class A11y:

    def __init__(self, page):
        self.page = page

    def execute(self, engine, params=None):
        self.page.wait_for_load_state("domcontentloaded")
        js_text = Path(root_dir() + "/resources/js/", engine.name.lower()+".js").read_text()
        self.page.evaluate("async (js)=> await window.eval(js)", js_text)
        data = self.page.evaluate("async (param) => await axeData(param)", params.to_json()) if engine.value == 2 else \
            self.page.evaluate("async (param) => await getData(param)", params.to_json())
        file_name = root_dir() + '/reports/' + engine.name.lower() + '/json/' + uuid.uuid4().__str__() + '.json'
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return data
