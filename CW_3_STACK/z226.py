array = list(map(int, input().split()))
x = int(input())

indices = [str(i + 1) for i, num in enumerate(array) if num == x]
# индекс элемента и его значение
if indices:
    print(' '.join(indices))
