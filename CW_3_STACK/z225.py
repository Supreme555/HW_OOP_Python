array = list(map(int, input().split()))
x = int(input())

closest_element = array[0]
min_distance = abs(x - array[0])

for num in array:
    distance = abs(x - num)
    if distance < min_distance:
        closest_element = num
        min_distance = distance

print(closest_element)
