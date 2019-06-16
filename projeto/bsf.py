# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

# Grafo original da professora (aula 2, slide 10):
# grafo = {
#     'R': set(['S', 'V']),
#     'S': set(['R', 'W']),
#     'T': set(['W', 'X', 'U']),
#     'U': set(['T', 'X', 'Y']),
#     'V': set(['R']),
#     'X': set(['T', 'U', 'Y']),
#     'Y': set(['U', 'X']),
#     'W': set(['S', 'T', 'X'])
#     }

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

bfs(graph, 'A') # {'B', 'C', 'A', 'F', 'D', 'E'}

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

list(bfs_paths(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

