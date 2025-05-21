import networkx as nx
from collections import deque
from itertools import zip_longest

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
    visited = set(start)
    queue = deque([start])
    path = []
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                # print(neighbor, end=" ")
                visited.add(neighbor)
                queue.append(neighbor)
                path.append((vertex, neighbor))
    return path

print('-'*65)
print(f'|          Шлях DFS             |          Шлях BFS             |')
print('-'*65)
for dfs, bfs in zip_longest(dfs_recursive(G, 'Рівне'), bfs_iterative(G, 'Рівне'), fillvalue=(None, None)):
    if dfs[0] and dfs[1]:
        dfs = f'{dfs[0]} - {dfs[1]}'
    else:
        dfs = ''
    if bfs[0] and bfs[1]:
        bfs = f'{bfs[0]} - {bfs[1]}'
    else:
        bfs = ''
    print(f'|{dfs:30} | {bfs:30}|')
print('-'*65)
