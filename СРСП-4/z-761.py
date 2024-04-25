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


def get_leaves(root, leaves):
  """Собирает листья дерева в список."""
  if root is None:
    return

  if root.left is None and root.right is None:
    leaves.append(root.value)

  get_leaves(root.left, leaves)
  get_leaves(root.right, leaves)


def main():
  """Считывает последовательность чисел, строит из них бинарное дерево поиска
  и выводит список его листьев в порядке возрастания."""
  root = None
  leaves = []

  while True:
    value = int(input())
    if value == 0:
      break

    root = insert(root, value)

  get_leaves(root, leaves)
  leaves.sort()
  print(*leaves)


main()
