from queue import PriorityQueue

graph = {
  'A': ['B'],
  'B': ['A', 'C', 'E'],
  'C': ['B', 'D'],
  'D': ['C'],
  'E': ['B', 'F'],
  'F': ['E'],
}

weights = {
  ('A', 'B'): 3,
  ('B', 'C'): 1,
  ('C', 'D'): 3,
  ('B', 'E'): 2,
  ('E', 'F'): 3
}


def bfs(graph, start):
  visit = list()
  queue = list()
  queue.append(start)
  while queue:
      node = queue.pop(0)
      if node not in visit:
          visit.append(node)
          queue.extend(graph[node])
  return visit

def dfs(graph, start):
  visit = list()
  stack = list()
  stack.append(start)
  while stack:
      node = stack.pop()
      if node not in visit:
          visit.append(node)
          stack.extend(graph[node])
  return visit

def ucs(graph, start, goal):
  visit = list()
  pq = PriorityQueue()
  pq.put((0, start))
  while pq:
      cost, node = pq.get()
      if node not in visit:
          visit.append(node)
          if node == goal:
              return visit, cost
          for i in graph[node]:
              if i not in visit:
                  total_cost = cost + weights[(node, i)]
                  pq.put((total_cost, i))

print(bfs(graph, 'A'))
print(dfs(graph, 'A'))
print(ucs(graph, 'A', 'F'))