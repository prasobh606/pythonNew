import random
import time


def naive_search(source_array, search_for):

    for i in range(len(source_array)):
        if source_array[i] == search_for:
            return i

    return -1


def binary_search(source_array, search_for, low=0, high=0):

    if low > high:
        return -1
    elif high == 0:
        high = len(source_array)

    midpoint = (low + high)//2

    if search_for == source_array[midpoint-1]:

        return midpoint-1

    elif search_for < source_array[midpoint-1]:

        return binary_search(source_array, search_for, low, midpoint - 1)

    elif search_for > source_array[midpoint-1]:

        return binary_search(source_array, search_for, midpoint + 1, high)


length = 10000
sorted_list = set()

while len(sorted_list) < length:
    index = random.randint(0, length)
    sorted_list.add(index)
sorted_list = sorted(list(sorted_list))
# print(sorted_list)
# Search every element from sorted_list usng binary search
bs_search_start_time = time.time()

for search_item in sorted_list:
    result = binary_search(sorted_list, search_item)

bs_search_end_time = time.time()
total_bs_search_time = (bs_search_end_time - bs_search_start_time)
print(f"execution time for binary search is {total_bs_search_time} seconds")

# Search every element from sorted_list using naive search
naive_search_start_time = time.time()

for search_item in sorted_list:
    result = naive_search(sorted_list, search_item)

naive_search_end_time = time.time()
total_naive_search_time = (naive_search_end_time - naive_search_start_time)
print(f"execution time for normal search is {total_naive_search_time} seconds")

# OUT PUT
# execution time for binary search is 0.07420635223388672 seconds
# execution time for normal search is 3.5167219638824463 seconds
# Binary search is faster
