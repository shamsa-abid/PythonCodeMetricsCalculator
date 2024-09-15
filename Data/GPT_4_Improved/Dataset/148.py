def bf(planet1, planet2):
    planets = ("Mercury", "Venus", "Earth", "Mars",
               "Jupiter", "Saturn", "Uranus", "Neptune")

    try:
        start, end = sorted([planets.index(planet1), planets.index(planet2)])
        return planets[start + 1:end] if start != end else ()
    except ValueError:
        return ()
