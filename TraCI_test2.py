#!/usr/bin/env python
# @file: TraCI_test2.py
# @Author: Sijia Li
# @adapted some code from: https://github.com/avcourt/traci-demo
# @adapted some code from: http://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/

import os
import sys
import optparse
from collections import defaultdict

# import some python modules from the SUMO_HOME/tools directory
if 'SUMO_HOME' in os.environ:
    #tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    #sys.path.append(tools)
    sys.path.append('/Users/lsjnancy/Documents/sumo-1.2.0/tools')
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

'''
#   The following segments of code are adapted from: 
#   Author: Andrew Vcourt
#   Availability: https://github.com/avcourt/traci-demo
'''

from sumolib import checkBinary  # Checks for the binary in environ vars
import traci

def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = opt_parser.parse_args()
    return options
'''
#   End of adapted code from: https://github.com/avcourt/traci-demo
'''


'''
#   The following segments of code are adapted from: 
#   Title: IMPLEMENTING DJIKSTRA'S SHORTEST PATH ALGORITHM WITH PYTHON
#   Author: Ben Keen
#   Date: 2011-01-11
#   Availability: http://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/
'''
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




# modified dijsktra's algorithm implementation
# takes in 4 parameters: road graph, fromNode, toNode, and the first departing edge
def dijsktra(graph, initial, end, departingEdge):
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
    return pathToEdges(path,departingEdge)
'''
#   End of adapted code from: http://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/
'''



# 5 by 5 road network nodes and edges dictionary
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
# list of keys of d
dKeys = list(d.keys())
# list of values of d
dValues = list(d.values())
# tuples of (key, value) pairs
dItems = list(d.items())




# Convert node paths to a list of edges, i.e. [21, 22, 23] --> ['e1', 'e3']
def pathToEdges(path, departingEdge):
    pathEdgeList = []
    pathEdgeList.append(departingEdge)
    string = {}
    while len(path) > 1:
        # Special case: 0333
        if (path[0] == 3 and path[1] == 33):
            string = str(0) + str(path[0]) + str(path[1])
        # Special case: 3303
        elif (path[0] == 33 and path[1] == 3):
            string = str(path[0]) + str(0) + str(path[1])
        else:
            string = str(path[0]) + str(path[1])
        pathEdgeList.append(d[string])
        del path[0]
    return pathEdgeList



# Convert edges to nodes (departing and arriving)
def edgesToNodes(departingEdgeIndex, arrivingEdgeIndex):
    edgesToNodesList = [] #index = 0: fromNode; index = 1: toNode

    departingKey = dItems[departingEdgeIndex][0]
    edgesToNodesList.append(twoNodesFormAnEdge(departingKey)[1])

    arrivingKey = dItems[arrivingEdgeIndex][0]
    edgesToNodesList.append(twoNodesFormAnEdge(arrivingKey)[1])

    return edgesToNodesList




# Return the two nodes that will form the edge based on the key provided
def twoNodesFormAnEdge(key):
    twoNodesFormAnEdgeList = [] #index = 0: fromNode; index = 1: toNode
    if len(key) == 2:
        twoNodesFormAnEdgeList.append((key)[0])
        twoNodesFormAnEdgeList.append((key)[1])
    elif len(key) == 4:
        twoNodesFormAnEdgeList.append((key)[0:2])
        twoNodesFormAnEdgeList.append((key)[2:4])
    # 4-digit special case
    elif key == "3303":
        twoNodesFormAnEdgeList.append(key[0:2])
        twoNodesFormAnEdgeList.append(key[3])
    # 4-digit special case
    elif key == "0333":
        twoNodesFormAnEdgeList.append((key)[1:2])
        twoNodesFormAnEdgeList.append((key)[2:4])
    # 3-digit cases
    # fromNode: first 2 digits; toNode: 3rd digit
    elif key == "127" or key == "116" or key == "138" or key == "149" or key == "109" or key == "105" or key == "315" or key == "324" or key == "342" or key == "351" or key == "361" or key == "376":
        twoNodesFormAnEdgeList.append((key)[0:2])
        twoNodesFormAnEdgeList.append((key)[2])
    # fromNode: 1st digit; toNode: last 2 digits
    elif key == "611" or key == "712" or key == "813" or key == "914" or key == "910" or key == "510" or key == "531" or key == "432" or key == "234" or key == "135" or key == "136" or key == "637":
        twoNodesFormAnEdgeList.append((key)[0])
        twoNodesFormAnEdgeList.append((key)[1:3])

    return twoNodesFormAnEdgeList




# main entry point
if __name__ == "__main__":
    options = get_options()

    # check binary
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # traci starts sumo as a subprocess and then this script connects and runs
    traci.start([sumoBinary, "-c", "/Users/lsjnancy/Desktop/Summer2019/7_miscellaneous/2019-06-14/UI_designV3test.sumo.cfg",
                             "--full-output", "/Users/lsjnancy/Desktop/TraCI_test2-output.xml"])
    step = 0

    ###################### Assuming for every 2 cars with NO GPS, there is one car HAS GPS ########################
    weighted_graph = Graph()
    # the simulation will actually run 300*3 = 900 seconds
    for i in range(0,300):
        '''
        When running simulation, after every 2 seconds:
        1. use the vehicle id (=time step), get its departing and arriving edges, convert to nodes
        2. get # vehicles in last time step, construct a weighted graph
        3. use weighted graph, from and to nodes, generate and set new route for the vehicle
        '''
        # 1st second
        traci.simulationStep()
        step += 1
        print("\nstep",step)
        if step == 5:
            print("route of vehicle 4:", traci.vehicle.getRoute("5")[0]) #--> printing for checking correctness
            print("route of vehicle 4:", traci.vehicle.getRoute("5")[-1]) #--> printing for checking correctness

        # 2nd second
        traci.simulationStep()
        step += 1
        print("\nstep",step)
        
        # 3rd second --> Car HAS GPS --> need to change the route of this vehicle that is about to depart depending on current traffic
        traci.simulationStep()
        step += 1
        print("\nstep",step)

        # getting information about the vehicle HAS GPS that is about to depart (before changing its route)
        vehicleID = int(traci.simulation.getTime())
        departingEdge = traci.vehicle.getRoute("{}".format(vehicleID))[0]
        arrivingEdge = traci.vehicle.getRoute("{}".format(vehicleID))[-1]

        # if there is only 1 edge in the edges list in the originial route, no changes need to be made
        if departingEdge == arrivingEdge:
            continue;

        # otherwise
        # converting to departing node and arriving node
        departingEdgeIndex = dValues.index("{}".format(departingEdge))
        arrivingEdgeIndex = dValues.index("{}".format(arrivingEdge))
        nodesList = edgesToNodes(departingEdgeIndex,arrivingEdgeIndex)
        # note: for dijsktra's algorithm, fromNode is the toNode of the first edge and the toNode is the toNdoe of the last edge in the orginal route
        # however, the value returned after calling dijsktra's algorithm will contain the original first edge as the first edge in the new route/edges list
        fromNode = nodesList[0]
        toNode = nodesList[1]

        # get the number of vehicles on each edge in the last time step --> these are the weights
        n135 = traci.edge.getLastStepVehicleNumber("i35") + 1
        n16 = traci.edge.getLastStepVehicleNumber("e63") + 1
        n136 = traci.edge.getLastStepVehicleNumber("i36") + 1
        n12 = traci.edge.getLastStepVehicleNumber("e73") + 1

        n234 = traci.edge.getLastStepVehicleNumber("i34") + 1
        n27 = traci.edge.getLastStepVehicleNumber("e65") + 1
        n21 = traci.edge.getLastStepVehicleNumber("e74") + 1
        n23 = traci.edge.getLastStepVehicleNumber("e75") + 1

        n0333 = traci.edge.getLastStepVehicleNumber("i33") + 1
        n38 = traci.edge.getLastStepVehicleNumber("e67") + 1
        n32 = traci.edge.getLastStepVehicleNumber("e76") + 1
        n34 = traci.edge.getLastStepVehicleNumber("e77") + 1

        n432 = traci.edge.getLastStepVehicleNumber("i32") + 1
        n49 = traci.edge.getLastStepVehicleNumber("e69") + 1
        n43 = traci.edge.getLastStepVehicleNumber("e78") + 1
        n45 = traci.edge.getLastStepVehicleNumber("e79") + 1

        n531 = traci.edge.getLastStepVehicleNumber("i31") + 1
        n510 = traci.edge.getLastStepVehicleNumber("e71") + 1
        n54 = traci.edge.getLastStepVehicleNumber("e80") + 1
        n530 = traci.edge.getLastStepVehicleNumber("i30") + 1

        n61 = traci.edge.getLastStepVehicleNumber("e64") + 1
        n611 = traci.edge.getLastStepVehicleNumber("e45") + 1
        n637 = traci.edge.getLastStepVehicleNumber("i37") + 1
        n67 = traci.edge.getLastStepVehicleNumber("e55") + 1

        n72 = traci.edge.getLastStepVehicleNumber("e66") + 1
        n712 = traci.edge.getLastStepVehicleNumber("e47") + 1
        n76 = traci.edge.getLastStepVehicleNumber("e56") + 1
        n78 = traci.edge.getLastStepVehicleNumber("e57") + 1

        n83 = traci.edge.getLastStepVehicleNumber("e68") + 1
        n813 = traci.edge.getLastStepVehicleNumber("e49") + 1
        n87 = traci.edge.getLastStepVehicleNumber("e58") + 1
        n89 = traci.edge.getLastStepVehicleNumber("e59") + 1
        
        n94 = traci.edge.getLastStepVehicleNumber("e70") + 1
        n914 = traci.edge.getLastStepVehicleNumber("e51") + 1
        n98 = traci.edge.getLastStepVehicleNumber("e60") + 1
        n910 = traci.edge.getLastStepVehicleNumber("e61") + 1
        
        n105 = traci.edge.getLastStepVehicleNumber("e72") + 1
        n1015 = traci.edge.getLastStepVehicleNumber("e53") + 1
        n109 = traci.edge.getLastStepVehicleNumber("e62") + 1
        n1029 = traci.edge.getLastStepVehicleNumber("i29") + 1

        n116 = traci.edge.getLastStepVehicleNumber("e46") + 1
        n1116 = traci.edge.getLastStepVehicleNumber("e27") + 1
        n1138 = traci.edge.getLastStepVehicleNumber("i38") + 1
        n1112 = traci.edge.getLastStepVehicleNumber("e37") + 1

        n127 = traci.edge.getLastStepVehicleNumber("e48") + 1
        n1217 = traci.edge.getLastStepVehicleNumber("e29") + 1
        n1211 = traci.edge.getLastStepVehicleNumber("e38") + 1
        n1213 = traci.edge.getLastStepVehicleNumber("e39") + 1

        n138 = traci.edge.getLastStepVehicleNumber("e50") + 1
        n1318 = traci.edge.getLastStepVehicleNumber("e31") + 1
        n1312 = traci.edge.getLastStepVehicleNumber("e40") + 1
        n1314 = traci.edge.getLastStepVehicleNumber("e41") + 1

        n149 = traci.edge.getLastStepVehicleNumber("e52") + 1
        n1419 = traci.edge.getLastStepVehicleNumber("e33") + 1
        n1413 = traci.edge.getLastStepVehicleNumber("e42") + 1
        n1415 = traci.edge.getLastStepVehicleNumber("e43") + 1

        n1510 = traci.edge.getLastStepVehicleNumber("e54") + 1
        n1520 = traci.edge.getLastStepVehicleNumber("e35") + 1
        n1514 = traci.edge.getLastStepVehicleNumber("e44") + 1
        n1528 = traci.edge.getLastStepVehicleNumber("i28") + 1

        n1611 = traci.edge.getLastStepVehicleNumber("e28") + 1
        n1621 = traci.edge.getLastStepVehicleNumber("e9") + 1
        n1639 = traci.edge.getLastStepVehicleNumber("i39") + 1
        n1617 = traci.edge.getLastStepVehicleNumber("e19") + 1

        n1712 = traci.edge.getLastStepVehicleNumber("e30") + 1
        n1722 = traci.edge.getLastStepVehicleNumber("e11") + 1
        n1716 = traci.edge.getLastStepVehicleNumber("e20") + 1
        n1718 = traci.edge.getLastStepVehicleNumber("e21") + 1

        n1813 = traci.edge.getLastStepVehicleNumber("e32") + 1
        n1823 = traci.edge.getLastStepVehicleNumber("e13") + 1
        n1817 = traci.edge.getLastStepVehicleNumber("e22") + 1
        n1819 = traci.edge.getLastStepVehicleNumber("e23") + 1
        
        n1914 = traci.edge.getLastStepVehicleNumber("e34") + 1
        n1924 = traci.edge.getLastStepVehicleNumber("e15") + 1
        n1918 = traci.edge.getLastStepVehicleNumber("e24") + 1
        n1920 = traci.edge.getLastStepVehicleNumber("e25") + 1
        
        n2015 = traci.edge.getLastStepVehicleNumber("e36") + 1
        n2025 = traci.edge.getLastStepVehicleNumber("e17") + 1
        n2019 = traci.edge.getLastStepVehicleNumber("e26") + 1
        n2027 = traci.edge.getLastStepVehicleNumber("i27") + 1

        n2116 = traci.edge.getLastStepVehicleNumber("e10") + 1
        n2141 = traci.edge.getLastStepVehicleNumber("i41") + 1
        n2140 = traci.edge.getLastStepVehicleNumber("i40") + 1
        n2122 = traci.edge.getLastStepVehicleNumber("e1") + 1

        n2217 = traci.edge.getLastStepVehicleNumber("e12") + 1
        n2242 = traci.edge.getLastStepVehicleNumber("i42") + 1
        n2221 = traci.edge.getLastStepVehicleNumber("e2") + 1
        n2223 = traci.edge.getLastStepVehicleNumber("e3") + 1

        n2318 = traci.edge.getLastStepVehicleNumber("e14") + 1
        n2343 = traci.edge.getLastStepVehicleNumber("i43") + 1
        n2322 = traci.edge.getLastStepVehicleNumber("e4") + 1
        n2324 = traci.edge.getLastStepVehicleNumber("e5") + 1

        n2419 = traci.edge.getLastStepVehicleNumber("e16") + 1
        n2444 = traci.edge.getLastStepVehicleNumber("i44") + 1
        n2423 = traci.edge.getLastStepVehicleNumber("e6") + 1
        n2425 = traci.edge.getLastStepVehicleNumber("e7") + 1

        n2520 = traci.edge.getLastStepVehicleNumber("e18") + 1
        n2545 = traci.edge.getLastStepVehicleNumber("i45") + 1
        n2524 = traci.edge.getLastStepVehicleNumber("e8") + 1
        n2526 = traci.edge.getLastStepVehicleNumber("i26") + 1

        n2625 = traci.edge.getLastStepVehicleNumber("o26") + 1
        n2720 = traci.edge.getLastStepVehicleNumber("o27") + 1
        n2815 = traci.edge.getLastStepVehicleNumber("o28") + 1
        n2910 = traci.edge.getLastStepVehicleNumber("o29") + 1
        n305 = traci.edge.getLastStepVehicleNumber("o30") + 1

        n315 = traci.edge.getLastStepVehicleNumber("o31") + 1
        n324 = traci.edge.getLastStepVehicleNumber("o32") + 1
        n3303 = traci.edge.getLastStepVehicleNumber("o33") + 1
        n342 = traci.edge.getLastStepVehicleNumber("o34") + 1
        n351 = traci.edge.getLastStepVehicleNumber("o35") + 1

        n361 = traci.edge.getLastStepVehicleNumber("o36") + 1
        n376 = traci.edge.getLastStepVehicleNumber("o37") + 1
        n3811 = traci.edge.getLastStepVehicleNumber("o38") + 1
        n3916 = traci.edge.getLastStepVehicleNumber("o39") + 1
        n4021 = traci.edge.getLastStepVehicleNumber("o40") + 1

        n4121 = traci.edge.getLastStepVehicleNumber("o41") + 1
        n4222 = traci.edge.getLastStepVehicleNumber("o42") + 1
        n4323 = traci.edge.getLastStepVehicleNumber("o43") + 1
        n4424 = traci.edge.getLastStepVehicleNumber("o44") + 1
        n4525 = traci.edge.getLastStepVehicleNumber("o45") + 1

        # add weighted edges to the weighted graph
        weighted_edges = [
            ('1', '35', n135),
            ('1', '6', n16),
            ('1', '36', n136),
            ('1', '2', n12),

            ('2', '34', n234),
            ('2', '7', n27),
            ('2', '1', n21),
            ('2', '3', n23),

            ('3', '33', n0333), #-->special
            ('3', '8', n38),
            ('3', '2', n32),
            ('3', '4', n34),

            ('4', '32', n432),
            ('4', '9', n49),
            ('4', '3', n43),
            ('4', '5', n45),

            ('5', '31', n531),
            ('5', '10', n510),
            ('5', '4', n54),
            ('5', '30', n530),

            ('6', '1', n61),
            ('6', '11', n611),
            ('6', '37', n637),
            ('6', '7', n67),

            ('7', '2', n72),
            ('7', '12', n712),
            ('7', '6', n76),
            ('7', '8', n78),

            ('8', '3', n83),
            ('8', '13', n813),
            ('8', '7', n87),
            ('8', '9', n89),

            ('9', '4', n94),
            ('9', '14', n914),
            ('9', '8', n98),
            ('9', '10', n910),

            ('10', '5', n105),
            ('10', '15', n1015),
            ('10', '9', n109),
            ('10', '29', n1029),

            ('11', '6', n116),
            ('11', '16', n1116),
            ('11', '38', n1138),
            ('11', '12', n1112),

            ('12', '7', n127),
            ('12', '17', n1217),
            ('12', '11', n1211),
            ('12', '13', n1213),

            ('13', '8', n138),
            ('13', '18', n1318),
            ('13', '12', n1312),
            ('13', '14', n1314),

            ('14', '9', n149),
            ('14', '19', n1419),
            ('14', '13', n1413),
            ('14', '15', n1415),

            ('15', '10', n1510),
            ('15', '20', n1520),
            ('15', '14', n1514),
            ('15', '28', n1528),

            ('16', '11', n1611),
            ('16', '21', n1621),
            ('16', '39', n1639),
            ('16', '17', n1617),

            ('17', '12', n1712),
            ('17', '22', n1722),
            ('17', '16', n1716),
            ('17', '18', n1718),

            ('18', '13', n1813),
            ('18', '23', n1823),
            ('18', '17', n1817),
            ('18', '19', n1819),

            ('19', '14', n1914),
            ('19', '24', n1924),
            ('19', '18', n1918),
            ('19', '20', n1920),

            ('20', '15', n2015),
            ('20', '25', n2025),
            ('20', '19', n2019),
            ('20', '27', n2027),

            ('21', '16', n2116),
            ('21', '41', n2141),
            ('21', '40', n2140),
            ('21', '22', n2122),

            ('22', '17', n2217),
            ('22', '42', n2242),
            ('22', '21', n2221),
            ('22', '23', n2223),

            ('23', '18', n2318),
            ('23', '43', n2343),
            ('23', '22', n2322),
            ('23', '24', n2324),

            ('24', '19', n2419),
            ('24', '44', n2444),
            ('24', '23', n2423),
            ('24', '25', n2425),

            ('25', '20', n2520),
            ('25', '45', n2545),
            ('25', '24', n2524),
            ('25', '26', n2526),

            ('26', '25', n2625),
            ('27', '20', n2720),
            ('28', '15', n2815),
            ('29', '10', n2910),
            ('30', '5', n305),

            ('31', '5', n315),
            ('32', '4', n324),
            ('33', '3', n3303), #-->special
            ('34', '2', n342),
            ('35', '1', n351),

            ('36', '1', n361),
            ('37', '6', n376),
            ('38', '11', n3811),
            ('39', '16', n3916),
            ('40', '21', n4021),

            ('41', '21', n4121),
            ('42', '22', n4222),
            ('43', '23', n4323),
            ('44', '24', n4424),
            ('45', '25', n4525),
        ]

        for edge in weighted_edges:
            weighted_graph.add_edge(*edge) # star is used as an assignment
        
        # find the shortest path for this vehicle HAS GPS that is going to depart
        newRoute = dijsktra(weighted_graph, fromNode, toNode, departingEdge)

        # set the new route of this vehicle
        print("original route:", traci.vehicle.getRoute("{}".format(vehicleID))) #--> printing for checking correctness
        #traci.vehicle.setRoute(str(3),['e60', 'e58'])
        #traci.vehicle.setRoute(str(3),['e60', 'e58'])
        traci.vehicle.setRoute(str(vehicleID), newRoute)
        print("new route:", traci.vehicle.getRoute("{}".format(vehicleID))) #--> printing for checking correctness

        ################### CAN ALSO ADD OTHER TRACI COMMANDS HERE #####################

    traci.close()
    sys.stdout.flush()
