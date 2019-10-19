#!/usr/bin/env python
# @file: TraCI_test.py
# @adapted from: https://github.com/avcourt/traci-demo

import os
import sys
import optparse

# we need to import some python modules from the $SUMO_HOME/tools directory
if 'SUMO_HOME' in os.environ:
    #tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    #sys.path.append(tools)
    #sys.path.append('/opt/local/sumo/tools')
    sys.path.append('/Users/lsjnancy/Documents/sumo-1.2.0/tools')
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")


from sumolib import checkBinary  # Checks for the binary in environ vars
import traci

def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = opt_parser.parse_args()
    return options


# Change paths of configuration file and any other files
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
                             "--full-output", "/Users/lsjnancy/Desktop/TraCI_test-output.xml"])
    step = 0
    
    for step in range(1000):
        traci.simulationStep()
        step += 1
        print("current time step:",step)
        # Switches to the phase with the given index in the list of all phases for the current program.
        # Change traffic light phase for intersection 1:
        if step == 1:
            traci.trafficlight.setPhase("n1",1)
        # Set the remaining phase duration of the current phase in seconds. No effect on subsquent repetitions of this phase.
        if step == 2:
            traci.trafficlight.setPhaseDuration("n3", 2.0)
        print("traffic phase of intersection 1:", traci.trafficlight.getPhase("n1"))
        print("traffic phase of intersection 2:", traci.trafficlight.getPhase("n2"))
        print("current travel time on edge e20:", traci.edge.getTraveltime("e20"))
        print("total number of vehicles for the last time step on lane e20_1 (straight ahead):", traci.lane.getLastStepVehicleNumber("e20_1"))
        ################### CAN ALSO ADD OTHER TRACI COMMANDS IN THE FOR LOOP ####################

    traci.close()
    sys.stdout.flush()
