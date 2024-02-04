def reverseArray(arr):

    n = len(arr)


    start, end = 0, n - 1


    while start < end:

        arr[start], arr[end] = arr[end], arr[start]


        start += 1


        end -= 1


    return arr


if __name__ == '__main__':

    arr = [1, 3, 2, 4, 5]


    print("Original Array:", arr)


    reversed_arr = reverseArray(arr)


    print("Reversed Array:", reversed_arr)

#deus esta vendo que eu to tentando o meu melhor