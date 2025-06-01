def selection_sort(arr):
    n = len(arr)
    comparison_count = 0

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            comparison_count += 1
            print(f"Comparing arr[{min_index}]={arr[min_index]} and arr[{j}]={arr[j]}")
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            print(f"Swapping arr[{i}]={arr[i]} and arr[{min_index}]={arr[min_index]}")
            arr[i], arr[min_index] = arr[min_index], arr[i]

        print(f"Array after pass {i + 1}: {arr}")

    # Show total comparisons and theoretical formula
    print("\nTotal comparisons:", comparison_count)
    print("Expected by formula n(n - 1)/2:", n * (n - 1) // 2)

    return arr

# Example
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted array:  ", sorted_arr)
