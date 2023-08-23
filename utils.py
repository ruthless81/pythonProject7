import json
from diarybook import Diary

def read_from_json_into_app(path):
    file = open(path)
    data = json.loads(file.read())
    diaries = []
    for entry in data:
        diaries.append(Diary(entry["memo"]+","+entry["tags"]))

    return diaries


def write_into_json(path):
    pass