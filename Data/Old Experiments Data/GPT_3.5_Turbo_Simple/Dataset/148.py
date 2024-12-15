def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars",
               "Jupiter", "Saturn", "Uranus", "Neptune"]

    if planet1 not in planets or planet2 not in planets:
        return ()

    start_index = min(planets.index(planet1), planets.index(planet2))
    end_index = max(planets.index(planet1), planets.index(planet2))

    result = []
    for i in range(start_index+1, end_index):
        result.append(planets[i])

    return tuple(result)
