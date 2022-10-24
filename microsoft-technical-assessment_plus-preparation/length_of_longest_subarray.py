# Given an array contianing 0s and 1s, 
# if you are allowed to replace more than 'k 0s with 1s, 
# find the length of the longest contigous subarray having all 1s.


def length_of_longest_subarray(arr, k):
    window_start, max_length, max_ones_count = 0, 0, 0

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones_count += 1

    
        # Current window sieze is from window_start to window_end, overall we ahave a maximum 
        # of 1s repeating 'max_ones_count' times, this means we can have a window with
        # 'max_ones_count' 1s and the remaining are 0s which should replace with 1s.
        # Now, if the remaining 0s are more than 'k', it is the time to shrink the window ae 
        # we are not allowed to replace more than 'k' 0s
        if (window_end - window_start + 1 - max_ones_count) > k:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length
    
def main():
    print(length_of_longest_subarray([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_subarray([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()