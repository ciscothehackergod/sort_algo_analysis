def insertion_sort(arr):
    n = len(arr)
    comparison_count = 0

    for i in range(1, n):
        key = arr[i]  # Current value to insert
        j = i - 1

        print(f"\nInserting {key} at position {i}")

        # Shift elements to the right to make space
        while j >= 0 and arr[j] > key:
            comparison_count += 1
            print(f"  {arr[j]} > {key}, so shifting {arr[j]} to the right")
            arr[j + 1] = arr[j]
            j -= 1

        # One final comparison that breaks the while loop
        if j >= 0:
            comparison_count += 1
            print(f"  {arr[j]} <= {key}, stop shifting")

        arr[j + 1] = key
        print(f"Array after pass {i}: {arr}")

    print("\nTotal comparisons:", comparison_count)
    return arr

# Example
arr = [8, 3, 5, 1]
print("Original array:", arr)
sorted_arr = insertion_sort(arr)
print("Sorted array:  ", sorted_arr)
