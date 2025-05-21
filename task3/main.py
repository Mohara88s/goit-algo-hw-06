import networkx as nx
import matplotlib.pyplot as plt

# Створити граф
G = nx.Graph()

# Вершини (міста)
cities = [
    "Київ", "Рівне", "Луцьк", "Житомир", "Львів", "Харків", "Одеса", "Дніпро", "Запоріжжя",
    "Івано-Франківськ", "Тернопіль", "Кривий Ріг", "Ужгород", 
]
G.add_nodes_from(cities)

# Ребра з вагами (приблизні відстані в км)
edges = [
    ("Київ", "Харків", 480),
    ("Київ", "Житомир", 140),
    ("Київ", "Дніпро", 480),
    ("Рівне", "Луцьк", 70),
    ("Рівне", "Тернопіль", 160),
    ("Рівне", "Львів", 210),
    ("Рівне", "Житомир", 200),
    ("Кривий Ріг", "Запоріжжя", 220),
    ("Кривий Ріг", "Одеса", 300),
    ("Кривий Ріг", "Київ", 410),
    ("Житомир", "Рівне", 200),
    ("Житомир", "Тернопіль", 250),
    ("Луцьк", "Львів", 150),
    ("Львів", "Івано-Франківськ", 130),
    ("Львів", "Тернопіль", 120),
    ("Тернопіль", "Івано-Франківськ", 105),
    ("Дніпро", "Запоріжжя", 85),
    ("Ужгород", "Львів", 270),
]

# Додати ребра до графа з вагами
for city1, city2, distance in edges:
    G.add_edge(city1, city2, weight=distance)


def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: {'distance':float('infinity'),'path':[]} for vertex in graph}
    distances[start]['distance'] = 0
    distances[start]['path'] = [start]
    unvisited = list(graph.nodes())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex]['distance'])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex]['distance'] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            # print(f'{neighbor} - {weight}')
            # print(distances[current_vertex])
            distance = distances[current_vertex]['distance'] + weight['weight']

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]['distance']:
                distances[neighbor]['distance'] = distance
                distances[neighbor]['path'] = distances[current_vertex]['path'] + [neighbor]

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances

# print(dijkstra(G, 'Рівне'))

print('\n             Таблиця відстаней та найкоротших шляхів до м Рівне')
print('-'*77)
print('|        Місто       |Відстань|                    Шлях                     |')
print('-'*77)
for city, info in dijkstra(G, 'Рівне').items():
    print(f'|{city:20}|{info['distance']:8}|{' → '.join(info['path']):45}|')
print('-'*77)

# Візуалізація графа
plt.figure(figsize=(12, 8)) 
options = {
    "node_color": "yellow",
    "edge_color": "lightblue",
    "node_size": 500,
    "width": 3,
    "with_labels": True,
}
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, **options)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Граф міст України")
plt.show()