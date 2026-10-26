import uuid

def charge(request_id, amount, db):
    existing = db.find_charge(request_id)
    if existing:
        return existing
    charge_id = str(uuid.uuid4())
    db.insert_charge(charge_id, request_id, amount)
    # process externally
    db.mark_processed(charge_id)
    return charge_id
