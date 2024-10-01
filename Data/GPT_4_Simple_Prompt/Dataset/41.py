def car_race_collision(n: int) -> int:
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.

    Parameters:
    n (int): The number of cars moving in each direction.

    Returns:
    int: The number of collisions.
    """

    # Since each car moving left-to-right will collide with one car moving right-to-left, the number of collisions will
    # simply equal to the number of cars in one direction.
    return n
