class Node:
  """Узел бинарного дерева поиска."""
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def insert(root, value):
  """Вставляет элемент в бинарное дерево поиска."""
  if root is None:
    return Node(value)

  if value < root.value:
    root.left = insert(root.left, value)
  else:
    root.right = insert(root.right, value)

  return root


def get_height(root):
  """Возвращает высоту бинарного дерева поиска."""
  if root is None:
    return 0

  return max(get_height(root.left), get_height(root.right)) + 1


def main():
  """Считывает последовательность чисел, строит из них бинарное дерево поиска
  и выводит его высоту."""
  root = None

  while True:
    value = int(input())
    if value == 0:
      break

    root = insert(root, value)

  height = get_height(root)
  print(height)


main()
