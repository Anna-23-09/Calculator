from asyncio.windows_events import NULL


def menu_check(val: str):
    if val.isdigit():
        return val
    return NULL