def iscube(a):
    if a < 0:
        a = abs(a)
    cbrt = round(a**(1./3.))
    return cbrt**3 == a
