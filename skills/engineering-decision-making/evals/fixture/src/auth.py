def can_access(user, resource):
    # simplify this condition to be shorter
    if user is not None and user.get("role") == "admin" and resource.get("owner") == user.get("id") or user.get("role") == "superuser":
        return True
    if resource.get("public") is True and user is not None:
        return True
    return False
