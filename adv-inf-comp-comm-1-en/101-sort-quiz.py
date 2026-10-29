# fuck this stupid quiz fuck yuo fuck everything

def insertion_sort(unsorted_list):
    comparisons = 0
    insertions = 0
    sorted_list = []
    for unsorted_element in unsorted_list:
        smallest_index = -1 # -1 + 1 = 0,

        for i in range(len(sorted_list)-1, -1, -1):
            comparisons += 1 # monitoring
            if sorted_list[i] > unsorted_element:
                continue

            smallest_index = i
            break
        sorted_list.insert(smallest_index+1, unsorted_element)
        insertions += 1 # monitoring
        print(sorted_list)

    print("Comparisons:", comparisons)
    print("Insertions:", insertions)
    return sorted_list

def selection_sort(unsorted_list):
    sorted_list = []

    comparisons = 0 # monitoring
    selections = 0 # monitoring

    # as many iterations as there are elements in the list
    unsorted_list_len = len(unsorted_list) # keep the original length
    for _ in range(unsorted_list_len):
        smallest_element = unsorted_list[0]
        smallest_index = 0
        for index, unsorted_element in enumerate(unsorted_list):
            comparisons += 1 # monitoring
            if unsorted_element < smallest_element:
                smallest_element = unsorted_element
                smallest_index = index
        sorted_list.insert(0, smallest_element)
        unsorted_list.pop(smallest_index)
        selections += 1
        print(sorted_list, "|", unsorted_list)

    print("Comparisons:", comparisons)
    print("Selections:", selections)
    return sorted_list

def bubble_sort(list):
    print(list)
    comparisons = 0
    swaps = 0
    while True:
        # iterate through the list
        swap_was_performed = False
        for index in range(len(list)-1):
            # if out of order
            element_1 = list[index]
            element_2 = list[index + 1]
            comparisons += 1
            if element_1 > element_2:
                # swap the elements
                swap_was_performed = True
                swaps += 1
                list[index] = element_2
                list[index + 1] = element_1

        print(list)

        # no swaps performed, list is sorted.
        if not swap_was_performed:
            break;

    print("Comparisons: ", comparisons)
    print("Swaps: ", swaps)
    return list


list = [-3, 2, -10, -6, 5]
list_copy = list.copy()

print("INSERTION SORT")
insertion_sort(list)
print("SELECTION SORT")
selection_sort(list_copy)
print("BUBBLE SORT")
bubble_sort(list)

# 36 comparisons
# 8 selections

# 36
# 8

# 45
# 9