from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    seen = set()

    for num in numbers:
        for seen_num in seen:
            if abs(num - seen_num) < threshold:
                return True
        seen.add(num)

    return False
