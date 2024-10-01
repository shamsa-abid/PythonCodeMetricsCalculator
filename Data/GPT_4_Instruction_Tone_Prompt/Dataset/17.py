def parse_music(music_string: str) -> List[int]:
    notes_dict = {'o': 4, 'o|': 2, '.|': 1}
    split_music = music_string.split()
    return [notes_dict[note] for note in split_music]
