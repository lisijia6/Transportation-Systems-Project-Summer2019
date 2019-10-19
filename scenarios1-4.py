# Writing Python code to directly create the rou.xml file
# @Used some code from: http://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/
# @Author: Sijia Li

#Idea: No GPS --> shortest route (unweighted edges); Has GPS --> fastest route (weighted edges)
import random
from collections import defaultdict

# Randomly generate nodes/intersections
def generateInCityNode():
    return random.randint(1,25)

def generateOutCityNode():
    return random.randint(26,45)



# http://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/
# class for constructing road graph
class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        #self.weights[(to_node, from_node)] = weight



# construct traffict grid with unweighted edges/roads (no GPS)
unweighted_graph = Graph()
unweighted_edges = [
    ('1', '35', 1),
    ('1', '6', 1),
    ('1', '36', 1),
    ('1', '2', 1),

    ('2', '34', 1),
    ('2', '7', 1),
    ('2', '1', 1),
    ('2', '3', 1),

    ('3', '33', 1),
    ('3', '8', 1),
    ('3', '2', 1),
    ('3', '4', 1),

    ('4', '32', 1),
    ('4', '9', 1),
    ('4', '3', 1),
    ('4', '5', 1),

    ('5', '31', 1),
    ('5', '10', 1),
    ('5', '4', 1),
    ('5', '30', 1),

    ('6', '1', 1),
    ('6', '11', 1),
    ('6', '37', 1),
    ('6', '7', 1),

    ('7', '2', 1),
    ('7', '12', 1),
    ('7', '6', 1),
    ('7', '8', 1),

    ('8', '3', 1),
    ('8', '13', 1),
    ('8', '7', 1),
    ('8', '9', 1),

    ('9', '4', 1),
    ('9', '14', 1),
    ('9', '8', 1),
    ('9', '10', 1),

    ('10', '5', 1),
    ('10', '15', 1),
    ('10', '9', 1),
    ('10', '29', 1),

    ('11', '6', 1),
    ('11', '16', 1),
    ('11', '38', 1),
    ('11', '12', 1),

    ('12', '7', 1),
    ('12', '17', 1),
    ('12', '11', 1),
    ('12', '13', 1),

    ('13', '8', 1),
    ('13', '18', 1),
    ('13', '12', 1),
    ('13', '14', 1),

    ('14', '9', 1),
    ('14', '19', 1),
    ('14', '13', 1),
    ('14', '15', 1),

    ('15', '10', 1),
    ('15', '20', 1),
    ('15', '14', 1),
    ('15', '28', 1),

    ('16', '11', 1),
    ('16', '21', 1),
    ('16', '39', 1),
    ('16', '17', 1),

    ('17', '12', 1),
    ('17', '22', 1),
    ('17', '16', 1),
    ('17', '18', 1),

    ('18', '13', 1),
    ('18', '23', 1),
    ('18', '17', 1),
    ('18', '19', 1),

    ('19', '14', 1),
    ('19', '24', 1),
    ('19', '18', 1),
    ('19', '20', 1),

    ('20', '15', 1),
    ('20', '25', 1),
    ('20', '19', 1),
    ('20', '27', 1),

    ('21', '16', 1),
    ('21', '41', 1),
    ('21', '40', 1),
    ('21', '22', 1),

    ('22', '17', 1),
    ('22', '42', 1),
    ('22', '21', 1),
    ('22', '23', 1),

    ('23', '18', 1),
    ('23', '43', 1),
    ('23', '22', 1),
    ('23', '24', 1),

    ('24', '19', 1),
    ('24', '44', 1),
    ('24', '23', 1),
    ('24', '25', 1),

    ('25', '20', 1),
    ('25', '45', 1),
    ('25', '24', 1),
    ('25', '26', 1),

    ('26', '25', 1),
    ('27', '20', 1),
    ('28', '15', 1),
    ('29', '10', 1),
    ('30', '5', 1),

    ('31', '5', 1),
    ('32', '4', 1),
    ('33', '3', 1),
    ('34', '2', 1),
    ('35', '1', 1),

    ('36', '1', 1),
    ('37', '6', 1),
    ('38', '11', 1),
    ('39', '16', 1),
    ('40', '21', 1),

    ('41', '21', 1),
    ('42', '22', 1),
    ('43', '23', 1),
    ('44', '24', 1),
    ('45', '25', 1),
]

for edge in unweighted_edges:
    unweighted_graph.add_edge(*edge) # star is used as an assignment


# Only gives output of the first shortest path that the algorithm finds
# modified last line for output required
def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    # We only need to keep a note of the previous destination node and the total weight to get there
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible: node{} to node{}".format(initial,end)
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path and convert string list to integer list
    path = list(map(int,path[::-1]))
    return pathToEdges(path)




# Convert node paths to edge paths, i.e. [21, 22, 23] --> "e1 e3"
def pathToEdges(path):
    d = {
        "2122": "e1",
        "2221": "e2",

        "2223": "e3",
        "2322": "e4",

        "2324": "e5",
        "2423": "e6",

        "2425": "e7",
        "2524": "e8",

        "1621": "e9",
        "2116": "e10",

        "1722": "e11",
        "2217": "e12",

        "1823": "e13",
        "2318": "e14",

        "1924": "e15",
        "2419": "e16",

        "2025": "e17",
        "2520": "e18",

        "1617": "e19",
        "1716": "e20",

        "1718": "e21",
        "1817": "e22",

        "1819": "e23",
        "1918": "e24",

        "1920": "e25",
        "2019": "e26",

        "1116": "e27",
        "1611": "e28",

        "1217": "e29",
        "1712": "e30",

        "1318": "e31",
        "1813": "e32",

        "1419": "e33",
        "1914": "e34",

        "1520": "e35",
        "2015": "e36",

        "1112": "e37",
        "1211": "e38",

        "1213": "e39",
        "1312": "e40",

        "1314": "e41",
        "1413": "e42",

        "1415": "e43",
        "1514": "e44",

        "611": "e45",
        "116": "e46",

        "712": "e47",
        "127": "e48",

        "813": "e49",
        "138": "e50",

        "914": "e51",
        "149": "e52",

        "1015": "e53",
        "1510": "e54",

        "67": "e55",
        "76": "e56",

        "78": "e57",
        "87": "e58",

        "89": "e59",
        "98": "e60",

        "910": "e61",
        "109": "e62",

        "16": "e63",
        "61": "e64",

        "27": "e65",
        "72": "e66",

        "38": "e67",
        "83": "e68",

        "49": "e69",
        "94": "e70",

        "510": "e71",
        "105": "e72",

        "12": "e73",
        "21": "e74",

        "23": "e75",
        "32": "e76",

        "34": "e77",
        "43": "e78",

        "45": "e79",
        "54": "e80",

        "2526": "i26",
        "2625": "o26",
        "2027": "i27",
        "2720": "o27",
        "1528": "i28",
        "2815": "o28",
        "1029": "i29",
        "2910": "o29",
        "530": "i30",
        "305": "o30",

        "531": "i31",
        "315": "o31",
        "432": "i32",
        "324": "o32",
        "0333": "i33", #Special
        "3303": "o33", #Special
        "234": "i34",
        "342": "o34",
        "135": "i35",
        "351": "o35",

        "136": "i36",
        "361": "o36",
        "637": "i37",
        "376": "o37",
        "1138": "i38",
        "3811": "o38",
        "1639": "i39",
        "3916": "o39",
        "2140": "i40",
        "4021": "o40",

        "2141": "i41",
        "4121": "o41",
        "2242": "i42",
        "4222": "o42",
        "2343": "i43",
        "4323": "o43",
        "2444": "i44",
        "4424": "o44",
        "2545": "i45",
        "4525": "o45",

    }
    rVal = ""
    while len(path) > 1:
        # Special case: 0333
        if (path[0] == 3 and path[1] == 33):
            string = str(0) + str(path[0]) + str(path[1])
        # Special case: 3303
        elif (path[0] == 33 and path[1] == 3):
            string = str(path[0]) + str(0) + str(path[1])
        else:
            string = str(path[0]) + str(path[1])
        rVal = rVal + d[string] + " " 
        del path[0]
    return rVal[:len(rVal)-1]








# Get user input:
# 1. Length of simulation time
# 2. Percentage of each scenario
while True:
    try:
        Sim_Time = int(input("Enter simulation time in seconds: "))
        if (Sim_Time%100 != 0):
            print("Time must be a multiple of 100. Please try again.")
            continue
    except ValueError:
        print("Not an integer. Please try again.")
        continue
    else:
        break
Scenario_print = """
Scenarios:
1. depart from & arrive in the city (no GPS)
2. depart from outside the city & pass through the city (no GPS)
3. depart from outside the city & arrive in the city (no GPS)
4. depart from city and arrive outside (no GPS)
"""
print(Scenario_print)

percentage = 100
Scenario_list = [0,0,0,0,0,0,0,0]
for i in range(1,5): #Notice range here contains only 4 scenarios
    while True:
        try:
            Scenario = int(input("Enter the percentage of vehicles (between 0 and {}) with scenario {}: ".format(percentage,(i))))
            if (Scenario < 0 or Scenario > percentage):
                print("Percentage choice is not appropriate.")
                continue
            Scenario_list[i-1] = Scenario
            percentage = percentage - Scenario
        except ValueError:
            print("Input is not an integer. Please try again.")
            continue
        else:
            break
    i = i + 1
    if(percentage == 0):
        break

# Generate rou.xml file based on user inputs
print("<routes>")
time = 0.0

# Scenario 1: depart from & arrive in the city (no GPS)
previous_index = 0
index = int(Scenario_list[0]*Sim_Time/100)
route = ""
for a in range (previous_index+1,index+1):
    while True:
        fromNode = generateInCityNode()
        toNode = generateInCityNode()
        route = dijsktra(unweighted_graph,'{}'.format(fromNode),'{}'.format(toNode))
        if len(route) != 0:
            break
    print("<vehicle id=\"{0}\" depart=\"{1:.2f}\"> \n     <route edges=\"{2}\"/>\n</vehicle>".format(a,time,route))
    time = time + 1
    #time = 0.0 + random.randint(0,Sim_Time)


# Scenario 2: depart from outside the city & pass through the city (no GPS)
previous_index = index
index = index + int(Scenario_list[1]*Sim_Time/100)
route = ""
for b in range (previous_index+1, index+1):
    while True:
        fromNode = generateOutCityNode()
        toNode = generateOutCityNode()
        route = dijsktra(unweighted_graph,'{}'.format(fromNode),'{}'.format(toNode))
        if len(route) != 0:
            break
    print("<vehicle id=\"{0}\" depart=\"{1:.2f}\"> \n     <route edges=\"{2}\"/>\n</vehicle>".format(b,time,route))
    time = time + 1


# Scenario 3: depart from outside the city & arrive in the city (no GPS)
previous_index = index
index = index + int(Scenario_list[2]*Sim_Time/100)
route = ""
for c in range (previous_index+1, index+1):
    while True:
        fromNode = generateOutCityNode()
        toNode = generateInCityNode()
        route = dijsktra(unweighted_graph,'{}'.format(fromNode),'{}'.format(toNode))
        if len(route) != 0:
            break
    print("<vehicle id=\"{0}\" depart=\"{1:.2f}\"> \n     <route edges=\"{2}\"/>\n</vehicle>".format(c,time,route))
    time = time + 1


# Scenario 4: depart from city and arrive outside (no GPS)
previous_index = index
index = index + int(Scenario_list[3]*Sim_Time/100)
route = ""
for d in range (previous_index+1,index+1):
    while True:
        fromNode = generateInCityNode()
        toNode = generateOutCityNode()
        route = dijsktra(unweighted_graph,'{}'.format(fromNode),'{}'.format(toNode))
        if len(route) != 0:
            break
    print("<vehicle id=\"{0}\" depart=\"{1:.2f}\"> \n     <route edges=\"{2}\"/>\n</vehicle>".format(d,time,route))
    time = time + 1

print("</routes>")