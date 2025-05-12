def sumaFunction(flag, a, second_a, third_a):
    suma = []
    
    suma.append(a[0] + a[1] + a[2] + second_a[1] + third_a[0] + third_a[1] + third_a[2])
    suma.append(a[1] + a[2] + a[3] + second_a[2] + third_a[1] + third_a[2] + third_a[3])
    suma.append(a[2] + a[3] + a[4] + second_a[3] + third_a[2] + third_a[3] + third_a[4])
    suma.append(a[3] + a[4] + a[5] + second_a[4] + third_a[3] + third_a[4] + third_a[5])

    # print(suma)
    return max(suma)

def hourglassSum(arr):
    # print(max(arr))

    arr0, arr1, arr2, arr3, arr4, arr5 = arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]
    suma = 0
    high = 0

    for a in arr:
        if a == arr0:
            suma = sumaFunction(0, arr0, arr1, arr2)
        elif a == arr1:
            suma = sumaFunction(1, arr1, arr2, arr3)
        elif a == arr2:
            suma = sumaFunction(2, arr2, arr3, arr4)
        elif a == arr3:
            suma = sumaFunction(3, arr3, arr4, arr5)
        else:
            break

        if suma > high or (suma < 0 and high == 0 and a == arr0):
            high = suma
            suma = 0

    # print(high)
    return high

# 0
hourglassSum([[-1,  1, -1,  0,  0,  0],
    [ 0, -1,  0,  0,  0,  0],
    [-1, -1, -1,  0,  0,  0],
    [ 0, -9,  2, -4, -4,  0],
    [-7,  0,  0, -2,  0,  0],
    [ 0,  0, -1, -2, -4,  0]])

# -6
# hourglassSum([[-1, -1,  0, -9, -2, -2],
#     [-2, -1, -6, -8, -2, -5],
#     [-1, -1, -1, -2, -3, -4],
#     [-1, -9, -2, -4, -4, -5],
#     [-7, -3, -3, -2, -9, -9],
#     [-1, -3, -1, -2, -4, -5]])
