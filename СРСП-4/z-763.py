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


def get_nodes_with_one_child(root, nodes):
  """Собирает вершины с одним ребёнком в список."""
  if root is None:
    return

  if (root.left is not None and root.right is None) or \
     (root.left is None and root.right is not None):
    nodes.append(root.value)

  get_nodes_with_one_child(root.left, nodes)
  get_nodes_with_one_child(root.right, nodes)


def main():
  """Считывает последовательность чисел, строит из них бинарное дерево поиска
  и выводит список вершин с одним ребёнком в порядке возрастания."""
  root = None
  nodes_with_one_child = []

  while True:
    value = int(input())
    if value == 0:
      break

    root = insert(root, value)

  get_nodes_with_one_child(root, nodes_with_one_child)
  nodes_with_one_child.sort()
  print(*nodes_with_one_child)


if __name__ == "__main__":
  main()
