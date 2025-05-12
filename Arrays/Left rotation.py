def rotLeft(a, d):
    for i in range(d):
        element = a[0]

        # print("Before: ", a)

        a.pop(0)
        a.append(element)

        # print("After: ", a)

    
    # print(a)

    return a


rotLeft([1, 2, 3, 4, 5], 4)
