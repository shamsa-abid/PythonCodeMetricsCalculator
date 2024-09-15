from typing import List


def parse_music(music_string: str) -> List[int]:
    note_dict = {'o': 4, 'o|': 2, '.|': 1}
    return list(map(note_dict.get, music_string.split()))
