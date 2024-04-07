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

    # Теперь left указывает на элемент, который больше x,
    # а right указывает на элемент, который меньше x.
    # Найдем ближайший элемент к x.
    if right < 0:
        return arr[left]
    if left >= len(arr):
        return arr[right]
    
    if x - arr[right] <= arr[left] - x:
        return arr[right]
    else:
        return arr[left]

# Чтение входных данных
N, K = map(int, input().split())
first_array = list(map(int, input().split()))
second_array = list(map(int, input().split()))

# Для каждого числа из второго массива находим ближайшее число в первом массиве
for num in second_array:
    print(binary_search_closest(first_array, num))
