from numpy import math


def nCx(n, x):
    """Gives the number of combinations with n trials when selecting x successes. (N
    choose x)

    An example.

    Args:
        n (int) : The number of events
        x (int) : The number of outcomes of the event
    Returns:
        int : the number of combinations of that event occurring within the sample space

    """
    return int(math.factorial(n) / (math.factorial(x) * math.factorial(n - x)))


def test_combinations_coin():
    """Given 5 flips of a fair coin, I only get 2 HEADs. How many different
    combinations of this could I get?"""
    assert nCx(5, 2) == 10


def test_combinations_cards():
    """A deck of cards has 52 cards in it. A poker hand is made up of 5 cards. How
    many different combinations of hands
     could I get?

     """
    assert nCx(52, 5) == 2598960


def pascals_triangle(order):
    """Returns the values of Pascals triangle as a nest list.

    Args:
        list : Order of the desired row of pascals triangle.
    Returns:
        Nested list : the values of pascals triangle.
    """
    triangle = []
    for o in range(0, order + 1):
        coeff = []
        for n in range(0, o + 1):
            coeff.append(nCx(o, n))
        triangle.append(coeff)

    return triangle


def test_zeroth_order():
    assert pascals_triangle(0) == [[1]]


def test_first_order():
    assert pascals_triangle(1) == [[1], [1, 1]]


def test_fifth_order():
    assert pascals_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1],
                                   [1, 4, 6, 4, 1],
                                   [1, 5, 10, 10, 5, 1]]
