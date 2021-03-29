
# Graph Representation
adj_list = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["B", "F"],
    "D": [],
    "E": ["F"],
    "F": []
}

# Required array and dictionary
color = {}  # W, G, B
parent = {}
travel_time = {}  # [start, end]
dfs_traversal_output = []

# intialize
for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    travel_time[node] = [-1, -1]


time = 0


def dfs(x):
    global time
    color[x] = "G"
    travel_time[x][0] = time
    dfs_traversal_output.append(x)
    time += 1

    for v in adj_list[x]:
        if color[v] == "W":
            parent[v] = x
            dfs(v)
    color[x] = "B"
    travel_time[x][1] = time
    time += 1


dfs("A")
