def get_all(db):
    rows = db.query("SELECT * FROM items")
    out = []
    for r in rows:
        out.append(r)
    return out


def normalize(items):
    result = []
    for it in items:
        result.append({"id": it["id"], "name": it["name"].strip()})
    return result
