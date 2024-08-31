import networkx as nxx
import matplotlib.pyplot as plt1

G1 = nxx.Graph()
input = "6,10\nu,v,2\nu,w,5\nu,x,1\nx,v,2\nv,w,3\nx,w,3\nw,y,1\nx,y,1\nw,z,5\ny,z,2\n"
lines = input.split("\n")
#print(len(lines))
first_line = lines[0].split(",")
n = first_line[0]
m = first_line[1]
#print(m)
for i in range(1, int(m)+1):
    line = lines[i].split(",")
    node1 = line[0]
    node2 = line[1]
    cost = line[2]
    G1.add_edge(node1, node2, weight=cost)

pos = nxx.circular_layout(G1)
nxx.draw(G1, pos, with_labels=True)
edge_weight_ = nxx.get_edge_attributes(G1, 'weight')
nxx.draw_networkx_edge_labels(G1, pos, edge_labels=edge_weight_)
nodes = G1.nodes()

current_node = "u"
neighbours = G1.neighbors(current_node)
dictionary = {}
predecessor = {}

N_dash = [current_node]

for node in nodes:
    if node == current_node:
        continue
    x = node in G1.neighbors(current_node)
    if x:
        cost = G1.get_edge_data(current_node, node)
        dictionary[node] = int(cost['weight'])
        predecessor[node] = current_node
    else:
        dictionary[node] = 1000000

while len(N_dash) <= len(nodes):
    #print("node: ", current_node)
    min_value = 1000000
    for node in nodes:
        if node in N_dash:
            continue

        if dictionary[node] < min_value:
            min_value = dictionary[node]
            min_node = node

    #print("min node: ", min_node)
    #print("min value: ", min_value)
    N_dash.append(min_node)
    for node in nodes:
        if (node != current_node) and (node not in N_dash) and (node in G1.neighbors(min_node)):
            #print("node2: ", node)
            cost = G1.get_edge_data(min_node, node)
            x = int(cost['weight'])
            #print("current cost: ", dictionary[node])
            #print("acc cost: ", dictionary[min_node] + x)

            if dictionary[node] > dictionary[min_node] + x:
                predecessor[node] = min_node
                dictionary[node] = dictionary[min_node] + x
    current_node = min_node

print(predecessor)

print("Destination   Link")
current_node = "u"
for node in nodes:
    #print("current node: ", node)
    if node == current_node:
        continue
    #print("here")
    t = predecessor[node]
    x = t in G1.neighbors(current_node)
    if x:
        print(node, "           ", current_node, ",", predecessor[node])
    elif t == current_node:
        print(node, "           ", current_node, ",", node)
    else:
        while x == 0:
            temp = predecessor[predecessor[node]]
            if temp == current_node:
                break
            x = temp in G1.neighbors(current_node)
        print(node, "           ", current_node, ",", temp)


plt1.show()


#nxx.dijkstra_path(G1, "u", "z")
