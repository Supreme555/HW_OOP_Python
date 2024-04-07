def check_occurrence(arr, x):
    for num in arr:
        if num == x:
            return "YES"
    return "NO"

array = list(map(int, input().split()))

x = int(input())

print(check_occurrence(array, x))
