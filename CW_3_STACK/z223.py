def count_occurrences(arr, x):
    count = 0
    for num in arr:
        if num == x:
            count += 1
    return count

array = list(map(int, input().split()))

x = int(input())

print(count_occurrences(array, x))
