#  Select any two sorting algorithms and write a program to show how these algorithms operate.
#  1. Merge Sort - is a divide and conquer algorithm.
#  2. Bubble Sort - a simple sorting algorithm that compares adjacent elements repeatedly till they're sorted.

from datetime import datetime


def get_input():
    """
    Takes is user input from stdin.
    Return: an array of user inputs
    """
    arr_in_str = list(input("Enter the numbers to be sorted: "))
    arr = [int(i) for i in arr_in_str]
    choice = int(input("Enter your choice (1. Merge Sort 2. Bubble Sort): "))
    output = [arr, choice]
    return output

def merge_sort(arr):
    """
    Sorts an array of integers
    parameter: 
        arr: array of integers
    return: sorted arr: array of integers
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

def bubble_sort(arr):
    """
    Sorts an array of integers
    parameter: 
        arr: array of integers
    return: sorted arr: array of integers
    """
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    output = get_input()
    arr, choice = output[0], output[1]
    if choice == 1:
        init_time = datetime.now()
        print(merge_sort(arr))
        end_time = datetime.now()
        print("\n\t\t####\t\t\nTime taken to sort: ", end_time - init_time)
    elif choice == 2:
        init_time = datetime.now()
        print(bubble_sort(arr))
        end_time = datetime.now()
        print("\n\t\t####\t\t\nTime taken to sort: ", end_time - init_time)
