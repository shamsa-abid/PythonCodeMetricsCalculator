def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars",
               "Jupiter", "Saturn", "Uranus", "Neptune"]

    if planet1 not in planets or planet2 not in planets:
        return ()

    start_index = planets.index(planet1)
    end_index = planets.index(planet2)

    if start_index > end_index:
        start_index, end_index = end_index, start_index

    result = planets[start_index+1:end_index]
    return tuple(result)


# Test cases
print(bf("Jupiter", "Neptune"))  # Output: ("Saturn", "Uranus")
print(bf("Earth", "Mercury"))     # Output: ("Venus")
# Output: ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
print(bf("Mercury", "Uranus"))
