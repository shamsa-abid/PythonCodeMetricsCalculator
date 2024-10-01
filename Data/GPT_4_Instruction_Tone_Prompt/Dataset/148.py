def bf(planet1, planet2):
    # List of planets in the order of their distance from the Sun
    planets = ["Mercury", "Venus", "Earth", "Mars",
               "Jupiter", "Saturn", "Uranus", "Neptune"]

    # Check if the inputs are valid planet names
    if planet1 not in planets or planet2 not in planets:
        return ()

    # Get the indices of the input planets in the list
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)

    # Make sure index1 is less than index2
    if index1 > index2:
        index1, index2 = index2, index1

    # Return all planets between the two indices in a tuple
    return tuple(planets[index1 + 1:index2])
