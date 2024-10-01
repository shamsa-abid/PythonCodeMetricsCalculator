def bf(planet1, planet2):
    planet_names = ("Mercury", "Venus", "Earth", "Mars",
                    "Jupiter", "Saturn", "Uranus", "Neptune")

    if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:
        return ()

    planet1_index = planet_names.index(planet1)
    planet2_index = planet_names.index(planet2)

    min_index = min(planet1_index, planet2_index)
    max_index = max(planet1_index, planet2_index)

    # Using list slicing to get the planets between the orbit of planet1 and planet2
    result = planet_names[min_index+1: max_index]

    return tuple(result) if planet1_index < planet2_index else tuple(result[::-1])
