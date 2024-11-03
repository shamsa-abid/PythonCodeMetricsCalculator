def get_max_triples(n):
    # Array to store the counts of elements that are mods of 0, 1 and 2 respectively.
    count = [0, 0, 0]

    # Each element in the array can be represented as (i*i - i + 1) % 3
    # which becomes (i^2 - i + 1) % 3.
    # As i^2 and i both are congruent modulo 3. It simplifies to 1 % 3, which is always 1
    # Therefore every element in the array will be 1 when taken modulo 3.

    count[1] = n

    # The sum of any three numbers will be divisible by 3, if and only if sum of their remainders when divided by 3, is also divisible by 3.
    # Therefore, we can form a group of three numbers if and only if all of them are 1.
    # The total such groups of three numbers can be given by nC3 as all elements are similar.

    return count[1] * (count[1] - 1) * (count[1] - 2) // 6
