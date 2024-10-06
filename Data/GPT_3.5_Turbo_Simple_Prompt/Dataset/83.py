def starts_one_ends(n):
    count = 0
    for i in range(10**(n-1), 10**n):  # iterate through all n-digit positive integers
        if str(i)[0] == '1' or str(i)[-1] == '1':  # check if the number starts or ends with 1
            count += 1
    return count


# Test the function
n = 3
print(starts_one_ends(n))  # Output will depend on the value of n given
