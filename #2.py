from queue import PriorityQueue
import networkx as nx

G = nx.Graph()

G.add_node('S', hv=5)
G.add_node('A', hv=3)
G.add_node('B', hv=4)
G.add_node('C', hv=2)
G.add_node('D', hv=6)
G.add_node('G', hv=0)

G.add_edge('S', 'A', weight=1)
G.add_edge('A', 'B', weight=2)
G.add_edge('A', 'C', weight=1)
G.add_edge('B', 'D', weight=5)
G.add_edge('C', 'D', weight=3)
G.add_edge('C', 'G', weight=4)
G.add_edge('D', 'G', weight=2)
G.add_edge('S', 'G', weight=10)

def a_star_search(start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 5)  # set start node
    came_from = {}  # parent node
    cost_so_far = {}  # lowest cumulative cost
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()  # get from priority queue

        if current == goal:  # base case
            break
        print(current)
        for next in G.neighbors(current):  # successors
            new_cost = cost_so_far[current] + G[current][next]['weight']  # cost(start to current) + cost(current to next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:   # if new_cost lower than cost_so_far
                cost_so_far[next] = new_cost
                priority = new_cost + nx.get_node_attributes(G,'hv')[next]   # G[next]['hv']    # f = g + h
                frontier.put(next, priority)
                came_from[next] = current   # set parent
                print(current + " " + next)
    return goal

print(a_star_search('S', 'G'))