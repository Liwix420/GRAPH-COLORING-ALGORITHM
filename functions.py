def read_file(f):
    # f - name of file
    edges = []
    with open(f, "r") as file:
        for line in file:
            edges.append(tuple(([int(x) for x in line.strip().split()])))
    edges = tuple(edges[1:])
    return edges

def create_list_of_neighbours(e):
    # e - list of pairs of vertices that are connected
    neighbours = dict()
    for edge in e:
        v1, v2 = edge
        if v1 not in neighbours.keys():
            neighbours[v1] = []
        neighbours[v1].append(v2)
        if v2 not in neighbours.keys():
            neighbours[v2] = []
        neighbours[v2].append(v1)
    neighbours = {
        key: neighbours[key]
        for key in sorted(neighbours.keys())
    }
    return neighbours

def generate_graph(n, d):
    # d - density of the graph
    # n - number of vertices
    import random
    possible_edges = [(i,j) for i in range(1,n+1) for j in range(i+1, n+1)]
    return tuple(random.sample(possible_edges, int(d*len(possible_edges)))) #returns edges

def greedy_color_graph(g):
    # g - graph (list of neighbours)
    colors = dict()
    for i in g.keys():
        unavailable_colors = [colors[v] for v in g[i] if v in colors.keys()]
        picked_color = 1
        while picked_color in unavailable_colors:
            picked_color += 1
        colors[i] = picked_color
    return colors

def print_color_vertices(c):
    # c - colored vertices (dictionary where key is vertex and value is color)
    colors = list(set(c.values()))
    color_vertices = dict()
    for color in colors:
        if color not in color_vertices.keys():
            color_vertices[color] = []
        for i in c:
            if c[i] == color:
                color_vertices[color].append(i)
    print(color_vertices)

def tabu_color_graph()