def counting_sort(arr):
    if len(arr) == 0:
        return []

    print("Original array:", arr)

    max_val = max(arr)
    count = [0] * (max_val + 1)

    # Step 1: Count occurrences
    for num in arr:
        count[num] += 1
    print("Count array:", count)

    # Step 2: Build sorted array
    sorted_arr = []
    for num, freq in enumerate(count):
        sorted_arr.extend([num] * freq)  # Add num 'freq' times

    print("Sorted array:", sorted_arr)
    return sorted_arr

# Example usage:
arr = [4, 2, 2, 8, 3, 3, 1]
counting_sort(arr)
