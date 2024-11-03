def bf(planet1, planet2):
    planet_order = {"Mercury": 1, "Venus": 2, "Earth": 3, "Mars": 4,
                    "Jupiter": 5, "Saturn": 6, "Uranus": 7, "Neptune": 8}
    if planet1 != planet2 and planet1 in planet_order and planet2 in planet_order:
        range_min, range_max = sorted(
            (planet_order[planet1], planet_order[planet2]))
        return tuple(planet for planet, order in planet_order.items() if range_min < order < range_max)
    else:
        return ()
