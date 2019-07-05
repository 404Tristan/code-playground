def summationOf(*N):
    for x in N:
        if x != N[0]:
            b = b + x
        else:
            b = x
    else:
        print("the summation is done and its " + str(b))

summationOf(4,34,35,435,43,543,5,435,43,53,5,3)