from typing import List


def parse_music(music_string: str) -> List[int]:
    music_string = music_string.split()
    result = []
    for each in music_string:
        if each == 'o':
            result.append(4)
        elif each == 'o|':
            result.append(2)
        elif each == '.|':
            result.append(1)
    return result
