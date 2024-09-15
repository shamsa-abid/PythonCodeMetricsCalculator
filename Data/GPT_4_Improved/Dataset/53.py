def add(x: int, y: int) -> int:
    try:
        return x + y
    except (TypeError, ValueError):
        return "Invalid inputs. Both inputs should be integers."
