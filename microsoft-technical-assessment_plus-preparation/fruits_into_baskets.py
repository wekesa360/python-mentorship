
# you're visiting a farm to collect fruits
# the frm has a single row of fruit trees
# you'll be given two baskets, and your goal is to pick as amany fruits as possible to be placed in the baskets.

# You'll be given an array of characters where each character represents a fruit tree.
# the farm has the following restrictions:

    # Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold
    # You can start with any tree, but you can't skip a tree once you've started
    # You will pick exactly one fruit from every tree until you cannot, i.e, you wil stop when you have to pick from a third type

# write a function to return the maximum number of fruits in both baskets

# (In this problem, we need to find the longest subarray with no more than two distinct characters(or fruit types!))


def fruits_into_baskets(fruits):
    window_start = 0
    max_length = 0
    fruit_frequency = {}

    # try to extend the range [window_start, window_end]
    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1

        #shrink the sliding window, until we are left with '2' fruits in the first
        # frequency dictionary
        while len(fruit_frequency) > 2:
            left_fruit = fruits[window_start]
            fruit_frequency [left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            window_start += 1 # shrink the window
        max_length = max(max_length, window_end-window_start + 1)
    return max_length
def main():
    print("Maximum number of fruits: "
          + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: "
          + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()