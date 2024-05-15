import networkx as nx
import matplotlib.pyplot as plt
import time

# Read the graph from the GraphML file
G = nx.read_graphml('abilene.graphml')

# Create an empty directed graph
DG = nx.DiGraph()

# Add nodes from the undirected graph
DG.add_nodes_from(G.nodes(data=True))

# Lists to store iteration numbers and corresponding time taken
iteration_numbers_raw = []
time_taken_list_raw = []

for i in range(22):
    start_time = time.time()
    # Add edges with directions
    for edge in G.edges(data=True):
        source, target, attrs = edge
        DG.add_edge(source, target, **attrs)

    end_time = time.time();
    time_taken = int((end_time - start_time) * 1000000)
    print(i ,",",time_taken, ",")
    iteration_numbers_raw.append(i)
    time_taken_list_raw.append(time_taken)

# Draw the directed graph using Matplotlib
pos = nx.spring_layout(DG)  # Position nodes using a spring layout
nx.draw(DG, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
edge_labels = nx.get_edge_attributes(DG, 'LinkLabel')
nx.draw_networkx_edge_labels(DG, pos, edge_labels=edge_labels)

# Show the plot
#plt.show('directed_graph.png')

#plt.figure()
#plt.plot(iteration_numbers_raw, time_taken_list_raw, marker='o')
#plt.xticks(range(len(iteration_numbers)), iteration_numbers)  # Set x-axis ticks to match iteration numbers
#plt.xlabel('Iterations')
#plt.ylabel('Time Taken (microseconds)')
#plt.title('Time Taken vs Iterations')
#plt.grid(True)
#plt.show()
