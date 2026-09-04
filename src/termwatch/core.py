def changed(previous: str, current: str) -> bool:
    """Return whether terminal text differs after normalizing line endings."""
    return previous.replace('\r\n','\n') != current.replace('\r\n','\n')
