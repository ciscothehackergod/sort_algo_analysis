def bubble_sort(arr):
    n = len(arr)
    comparison_count = 0

    for i in range(n):
        swapped = False  # Track if a swap happened this pass

        print(f"\nPass {i + 1}")
        for j in range(0, n - 1 - i):
            comparison_count += 1
            print(f"  Comparing {arr[j]} and {arr[j + 1]}")
            if arr[j] > arr[j + 1]:
                print(f"  Swapping {arr[j]} and {arr[j + 1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        print("  Array now:", arr)
        if not swapped:
            print("  No swaps — array is sorted early!")
            break  # Optimization: stop if no swaps happened

    print("\nTotal comparisons:", comparison_count)
    return arr

# Example usage
arr = [5, 3, 8, 4]
print("Original array:", arr)
sorted_arr = bubble_sort(arr)
print("Sorted array:  ", sorted_arr)
