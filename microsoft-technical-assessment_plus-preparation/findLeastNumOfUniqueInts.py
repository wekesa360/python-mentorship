def findLeastNumOfUniqueInts(arr, k: int) -> int:
        i = 0
        while i < k:
            arr.pop()
            i = i + 1
        print(i)
        s_arr = set(arr)
        return len(s_arr)
    
l = [1,2,2,2,3,4]
findLeastNumOfUniqueInts(l, 3)