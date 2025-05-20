import networkx as nx
from collections import deque

# Створити граф
G = nx.Graph()

# Вершини (міста)
cities = [
    "Київ", "Рівне", "Луцьк", "Житомир", "Львів", "Харків", "Одеса", "Дніпро", "Запоріжжя",
    "Івано-Франківськ", "Тернопіль", "Кривий Ріг", "Ужгород", 
]

# Додати вершини до графа
G.add_nodes_from(cities)

# Ребра з вагами (приблизні відстані в км)
edges = [
    ("Київ", "Харків"),
    ("Київ", "Житомир"),
    ("Київ", "Дніпро"),
    ("Рівне", "Луцьк"),
    ("Рівне", "Тернопіль"),
    ("Рівне", "Львів"),
    ("Рівне", "Житомир"),
    ("Кривий Ріг", "Запоріжжя"),
    ("Кривий Ріг", "Одеса"),
    ("Кривий Ріг", "Київ"),
    ("Житомир", "Рівне"),
    ("Житомир", "Тернопіль"),
    ("Луцьк", "Львів"),
    ("Львів", "Івано-Франківськ"),
    ("Львів", "Тернопіль"),
    ("Тернопіль", "Івано-Франківськ"),
    ("Дніпро", "Запоріжжя"),
    ("Ужгород", "Львів"),
]

# Додати ребра до графа
G.add_edges_from(edges)


def dfs_recursive(graph, vertex, visited=None, path=None, parant=None):
    if visited is None:
        visited = set()
        path = []
    visited.add(vertex)
    # print(vertex, end=' ')  # Відвідуємо вершину
    if parant is not None:
        path.append((parant, vertex))
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, path, vertex)
    return path

def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])
    path = []
    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                # print(neighbor, end=" ")
                visited.add(neighbor)
                queue.append(neighbor)
                path.append((vertex, neighbor))
    return path

print(dfs_recursive(G, 'Рівне'))
print()
print(bfs_iterative(G, 'Рівне'))
