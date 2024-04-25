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


def inorder_traversal(root):
  """Обход дерева в порядке возрастания."""
  if root is None:
    return

  inorder_traversal(root.left)
  print(root.value)
  inorder_traversal(root.right)


def main():
  """Считывает последовательность чисел, строит из них бинарное дерево поиска
  и выводит его элементы в порядке возрастания."""
  root = None

  while True:
    value = int(input())
    if value == 0:
      break

    root = insert(root, value)

  inorder_traversal(root)


main()
