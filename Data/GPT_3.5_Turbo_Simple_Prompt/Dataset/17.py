
from typing import List


def parse_music(music_string: str) -> List[int]:
    beats_mapping = {'o': 4, 'o|': 2, '.|': 1}
    music_list = music_string.split()

    beats_list = [beats_mapping[note] for note in music_list]

    return beats_list


# Test the function
print(parse_music('o o| .| o| o| .| .| .| .| o o'))
