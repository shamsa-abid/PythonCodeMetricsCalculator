from typing import List
def parse_music(music_string: str) -> List[int]:
    duration_map = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    result = [duration_map[note] for note in notes]
    return result
