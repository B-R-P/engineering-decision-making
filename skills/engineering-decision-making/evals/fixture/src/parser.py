import json

def parse(text):
    # accepts untrusted input
    data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError("expected object")
    return data.get("value")

def parse_many(text):
    items = json.loads(text)
    return [parse_one(x) for x in items]

def parse_one(x):
    return x.strip().lower()
