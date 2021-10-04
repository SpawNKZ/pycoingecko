def permutations(arr):
    arr1 = arr.copy()
    print(" ".join(arr1), end=" ")
    count = len(arr1)
    for x in range(len(arr)):
        tmp = []
        for i in arr:
            for k in arr1:
                if i not in k:
                    tmp.append(k + i)
                    count += 1

        print(" ".join(tmp), end=" ")
        arr1 = tmp


arr = input().split()
permutations(arr)
