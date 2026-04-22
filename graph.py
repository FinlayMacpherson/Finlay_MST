# --- Finlay Macpherson --- Data Structures and Algorithms Assessment ---
#The Graph will take in a collection of points

import numpy as np

class Graph:
    def __init__(Self): # Initialise an empty list to store all the points
        Self.Points = []

    def AddPoints(Self, Point):
        Self.Points.append(Point)  # Append a new point

    def GetEdges(Self):
        Edges = [] # This will hold all the edges as tuples with both points connected by distance
        for i in range(len(Self.Points)):
            for j in range(i + 1, len(Self.Points)):
                P1 = Self.Points[i]
                P2 = Self.Points[j]
                Distance = np.linalg.norm(P1 - P2) #Turns arrays into numpy arrays
                Edges.append([Distance, P1, P2])
        return Edges