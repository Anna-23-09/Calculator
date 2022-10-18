def menu_check(val: str) -> str:
    if val.isdigit():
        if len(val) > 1:
            return ' '
        return val
    return ' '
