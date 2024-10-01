
from typing import List


def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i+1] for i in range(len(string))]
    return prefixes


# Test the function with the example given in the docstring
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
