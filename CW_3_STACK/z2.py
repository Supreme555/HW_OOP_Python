def binary_search_closest(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    if right < 0:
        return arr[left]
    if left >= len(arr):
        return arr[right]
    
    if x - arr[right] <= arr[left] - x:
        return arr[right]
    else:
        return arr[left]

N, K = map(int, input().split())
first_array = list(map(int, input().split()))
second_array = list(map(int, input().split()))

for num in second_array:
    print(binary_search_closest(first_array, num))
