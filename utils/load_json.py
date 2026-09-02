import json

def load_json_file(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(fp=f)