def parse_music(music_string: str) -> List[int]:
    """ Function to parseMusic"""
    music_legends_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    music_list = music_string.split()
    parsed_music = [music_legends_map[m] for m in music_list]
    return parsed_music
