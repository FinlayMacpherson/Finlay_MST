# --- Finlay Macpherson --- Data Structures and Algorithms Assessment ---
#Takes the final edges and points and renders them as a visual graph using SVG graphics

import matplotlib.pyplot as plt

class SVGRenderer:
    def __init__(Self, Edges):
        Self.Edges = Edges

    def render(Self, filename="output.svg"):
        for _, P1, P2 in Self.Edges:
            plt.plot([P1[0], P2[0]], [P1[1], P2[1]], 'b-')

        points = {tuple(p) for _, P1, P2 in Self.Edges for p in (P1, P2)}
        for p in points:
            plt.plot(p[0], p[1], 'ro',)

        plt.savefig(filename)
        plt.show()
