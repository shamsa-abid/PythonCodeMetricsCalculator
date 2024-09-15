planet_names = ("Mercury", "Venus", "Earth", "Mars",
                "Jupiter", "Saturn", "Uranus", "Neptune")


def bf(planet1, planet2):
    if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:
        return ()

    start_idx = min(planet_names.index(planet1), planet_names.index(planet2))
    end_idx = max(planet_names.index(planet1), planet_names.index(planet2))

    return tuple(planet_names[start_idx+1:end_idx])

