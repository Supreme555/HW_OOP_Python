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


def get_nodes_with_two_children(root, nodes):
  """Собирает вершины с двумя детьми в список."""
  if root is None:
    return

  if root.left is not None and root.right is not None:
    nodes.append(root.value)

  get_nodes_with_two_children(root.left, nodes)
  get_nodes_with_two_children(root.right, nodes)


def main():
  """Считывает последовательность чисел, строит из них бинарное дерево поиска
  и выводит список вершин с двумя детьми в порядке возрастания."""
  root = None
  nodes_with_two_children = []

  while True:
    value = int(input())
    if value == 0:
      break

    root = insert(root, value)

  get_nodes_with_two_children(root, nodes_with_two_children)
  nodes_with_two_children.sort()
  print(*nodes_with_two_children)


if __name__ == "__main__":
  main()
