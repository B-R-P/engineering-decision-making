def get_items(db, cache=None):
    if cache is not None and cache.has("items"):
        return cache.get("items")
    rows = db.query("SELECT id,name FROM items")
    result = [{"id": r[0], "name": r[1]} for r in rows]
    if cache is not None:
        cache.set("items", result)
    return result
