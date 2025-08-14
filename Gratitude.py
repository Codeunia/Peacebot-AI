def log_gratitude_noninteractive(items):
    """Save a provided list of 1-3 gratitude items in non-interactive contexts.

    Parameters
    ----------
    items : list[str]
        One to three short gratitude statements.
    """
    import json as _json
    import datetime as _dt

    if not items or not isinstance(items, list):
        raise ValueError("items must be a non-empty list of strings")

    trimmed = [str(x).strip() for x in items if str(x).strip()]
    if not trimmed:
        raise ValueError("no valid items provided")
    if len(trimmed) > 3:
        trimmed = trimmed[:3]

    try:
        with open(DATA_FILE, "r") as f:
            data = _json.load(f)
    except FileNotFoundError:
        data = []

    entry = {
        "timestamp": str(_dt.datetime.now()),
        "gratitude": trimmed,
        "source": "noninteractive",
    }
    data.append(entry)

    with open(DATA_FILE, "w") as f:
        _json.dump(data, f, indent=4)

    return "Saved your gratitude list.
