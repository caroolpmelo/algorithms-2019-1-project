# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set() # build an unordored collection of unique elements
    
    visited.add(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    
    return visited

dfs(graph, 'C') # {'E', 'D', 'F', 'A', 'C', 'B'}

def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    
    if start == goal:
        yield path
    
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])
    
list(dfs_paths(graph, 'C', 'F')) # [['C', 'F'], ['C', 'A', 'B', 'E', 'F']]

######################

